"""
Methods to format and print summary data on merger enforcement patterns.

"""

import enum
import shutil
import subprocess
from collections.abc import Mapping, Sequence
from importlib.metadata import version
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import re2 as re  # type: ignore
from jinja2 import Environment, FileSystemLoader, Template, select_autoescape
from numpy.typing import NDArray
from scipy.interpolate import interp1d  # type: ignore

from .. import _PKG_NAME, DATA_DIR  # noqa: TID252
from ..core import ftc_merger_investigations_data as fid  # noqa: TID252
from ..core.proportions_tests import propn_ci  # noqa: TID252
from . import TF, TI, INVResolution

__version__ = version(_PKG_NAME)


@enum.unique
class INDGRPConstants(enum.StrEnum):
    ALL = "All Markets"
    GRO = "Grocery Markets"
    OIL = "Oil Markets"
    CHM = "Chemical Markets"
    PHM = "Pharmaceuticals Markets"
    HOS = "Hospital Markets"
    EDS = "Electronically-Controlled Devices and Systems Markets"
    BRD = "Branded Consumer Goods Markets"
    OTH = '"Other" Markets'
    IIC = "Industries in Common"


@enum.unique
class EVIDENConstants(enum.StrEnum):
    HD = "Hot Documents Identified"
    CC = "Strong Customer Complaints"
    NE = "No Entry Evidence"
    ED = "Entry Difficult"
    EE = "Entry Easy"
    UR = "Unrestricted on additional evidence"


@enum.unique
class StatsGrpSelector(enum.StrEnum):
    FC = "ByFirmCount"
    HD = "ByHHIandDelta"
    DL = "ByDelta"
    ZN = "ByConcZone"


@enum.unique
class StatsReturnSelector(enum.StrEnum):
    CNT = "count"
    RPT = "rate, point"
    RIN = "rate, interval"


@enum.unique
class SortSelector(enum.StrEnum):
    UCH = "unchanged"
    REV = "reversed"


cnt_format_str = R"{: >5,.0f}"
pct_format_str = R"{: >6.1f}\%"
ci_format_str = R"{0: >5.1f} [{2: >4.1f},{3: >5.1f}] \%"

moe_tmpl = Template(R"""
    {% if (rv[2] - rv[0]) | abs == (rv[3] - rv[0]) | abs %}
         {{- "[\pm {:.1f}]".format(rv[3] - rv[0]) -}}
    {% else %}
         {{- "[{:.1f}/+{:.1f}]".format(rv[2] - rv[0], rv[3] - rv[0]) -}}
    {% endif %}
    """)

LTX_ARRAY_LINEEND = R"\\" "\n"
latex_hrdcoldesc_format_str = "{}\n{}\n{}".format(
    "".join((
        R"\matrix[hcol, above=0pt of {}, nodes = {{",
        R"text width={}, text depth=10pt, inner sep=3pt, minimum height=25pt,",
        R"}},] ",
        R"({}) ",
        R"{{",
    )),
    R"\node[align = {},] {{ {} }}; \\",
    R"}};",
)


class StatsContainer(SimpleNamespace):
    """A container for passing content to jinja2 templates

    Other attributes added later, to fully populate selected jinja2 templates
    """

    invdata_hdrstr: str
    invdata_datstr: str


# Define the latex jinja environment
# http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
latex_jinja_env = Environment(
    block_start_string=R"((*",
    block_end_string="*))",
    variable_start_string=R"\JINVAR{",
    variable_end_string="}",
    comment_start_string=R"((#",  # r'#{',
    comment_end_string=R"#))",  # '}',
    line_statement_prefix="##",
    line_comment_prefix="%#",
    trim_blocks=True,
    lstrip_blocks=True,
    autoescape=select_autoescape(disabled_extensions=("tex.jinja2",)),
    loader=FileSystemLoader(Path(__file__).parents[1] / "jinja_LaTex_templates"),
)

# Place files related to rendering latex in output data directory
if not (_out_path := DATA_DIR.joinpath(f"{_PKG_NAME}.cls")).is_file():
    shutil.copyfile(
        Path(__file__).parents[1].joinpath("jinja_LaTex_templates", "mergeron.cls"),
        _out_path,
    )


if not (_DOTTEX := DATA_DIR / Rf"{_PKG_NAME}_TikZTableSettings.tex").is_file():
    # Write to dottex
    with _DOTTEX.open("w", encoding="UTF-8") as _table_helper_dottex:
        _table_helper_dottex.write(
            latex_jinja_env.get_template("setup_tikz_tables.tex.jinja2").render(
                tmpl_data=StatsContainer()
            )
        )
        print("\n", file=_table_helper_dottex)


# Parameters and functions to interpolate selected HHI and ΔHHI values
#   recorded in fractions to ranges of values in points on the HHI scale
HHI_DELTA_KNOTS = np.array(
    [0, 100, 200, 300, 500, 800, 1200, 2500, 5001], dtype=np.int64
)
HHI_POST_ZONE_KNOTS = np.array([0, 1800, 2400, 10001], dtype=np.int64)
hhi_delta_ranger, hhi_zone_post_ranger = (
    interp1d(_f / 1e4, _f, kind="previous", assume_sorted=True)
    for _f in (HHI_DELTA_KNOTS, HHI_POST_ZONE_KNOTS)
)

HMG_PRESUMPTION_ZONE_DICT = {
    HHI_POST_ZONE_KNOTS[0]: {
        HHI_DELTA_KNOTS[0]: (0, 0, 0),
        HHI_DELTA_KNOTS[1]: (0, 0, 0),
        HHI_DELTA_KNOTS[2]: (0, 0, 0),
    },
    HHI_POST_ZONE_KNOTS[1]: {
        HHI_DELTA_KNOTS[0]: (0, 1, 1),
        HHI_DELTA_KNOTS[1]: (1, 1, 2),
        HHI_DELTA_KNOTS[2]: (1, 1, 2),
    },
    HHI_POST_ZONE_KNOTS[2]: {
        HHI_DELTA_KNOTS[0]: (0, 2, 1),
        HHI_DELTA_KNOTS[1]: (1, 2, 3),
        HHI_DELTA_KNOTS[2]: (2, 2, 4),
    },
}

ZONE_VALS = np.unique(
    np.row_stack([
        tuple(HMG_PRESUMPTION_ZONE_DICT[_k].values())
        for _k in HMG_PRESUMPTION_ZONE_DICT
    ]),
    axis=0,
)

ZONE_STRINGS = {
    0: R"\node[align = left, fill=BrightGreen] {Green Zone (Safeharbor)};",
    1: R"\node[align = left, fill=HiCoYellow] {Yellow Zone};",
    2: R"\node[align = left, fill=VibrRed] {Red Zone (SLC Presumption)};",
    fid.TTL_KEY: R"\node[align = left, fill=OBSHDRFill] {TOTAL};",
}

ZONE_DETAIL_STRINGS_HHI = {
    0: Rf"HHI_{{post}} < \text{{{HHI_POST_ZONE_KNOTS[1]} pts.}}",
    1: R"HHI_{{post}} \in \text{{[{}, {}) pts. and }} ".format(
        *HHI_POST_ZONE_KNOTS[1:3]
    ),
    2: Rf"HHI_{{post}} \geqslant \text{{{HHI_POST_ZONE_KNOTS[2]} pts. and }} ",
}

ZONE_DETAIL_STRINGS_DELTA = {
    0: "",
    1: Rf"\Delta HHI < \text{{{HHI_DELTA_KNOTS[1]} pts.}}",
    2: Rf"\Delta HHI \geqslant \text{{{HHI_DELTA_KNOTS[1]} pts.}}",
    3: R"\Delta HHI \in \text{{[{}, {}) pts.}}".format(*HHI_DELTA_KNOTS[1:3]),
    4: Rf"\Delta HHI \geqslant \text{{{HHI_DELTA_KNOTS[2]} pts.}}",
}


def invres_stats_output(
    _data_array_dict: fid.INVData,
    _data_period: str = "1996-2003",
    _table_ind_group: INDGRPConstants = INDGRPConstants.ALL,
    _table_evid_cond: EVIDENConstants = EVIDENConstants.UR,
    _stats_group: StatsGrpSelector = StatsGrpSelector.FC,
    _invres_spec: INVResolution = INVResolution.CLRN,
    /,
    *,
    return_type_sel: StatsReturnSelector = StatsReturnSelector.RPT,
    sort_order: SortSelector = SortSelector.UCH,
    print_to_screen: bool = True,
) -> tuple[list[str], list[list[str]]]:
    if _data_period not in _data_array_dict:
        raise ValueError(
            f"Value of _data_period, {f'"{_data_period}"'} is invalid.",
            f"Must be in, {list(_data_array_dict.keys())!r}",
        )

    match _stats_group:
        case StatsGrpSelector.ZN:
            _latex_tbl_invres_stats_func = latex_tbl_invres_stats_byzone
        case StatsGrpSelector.FC:
            _latex_tbl_invres_stats_func = latex_tbl_invres_stats_1dim
        case StatsGrpSelector.DL:
            _latex_tbl_invres_stats_func = latex_tbl_invres_stats_1dim
        case _:
            raise ValueError(
                'Statistics formatted, "{_stats_group}" not available here.'
            )

    _invres_stats_cnts = invres_stats_cnts_by_group(
        _data_array_dict,
        _data_period,
        _table_ind_group,
        _table_evid_cond,
        _stats_group,
        _invres_spec,
    )

    _invres_stats_hdr_list, _invres_stats_dat_list = _latex_tbl_invres_stats_func(
        _invres_stats_cnts, None, return_type_sel=return_type_sel, sort_order=sort_order
    )

    if print_to_screen:
        print(
            f"{_invres_spec.capitalize()} stats ({return_type_sel})",
            f"for Period: {_data_period}",
            "\u2014",
            f"{_table_ind_group};",
            _table_evid_cond,
        )
        stats_print_rows(_invres_stats_hdr_list, _invres_stats_dat_list)

    return _invres_stats_hdr_list, _invres_stats_dat_list


def invres_stats_cnts_by_group(
    _invdata_array_dict: Mapping[str, Mapping[str, Mapping[str, fid.INVTableData]]],
    _study_period: str,
    _table_ind_grp: INDGRPConstants,
    _table_evid_cond: EVIDENConstants,
    _stats_group: StatsGrpSelector,
    _invres_spec: INVResolution,
    /,
) -> NDArray[np.int64]:
    if _stats_group == StatsGrpSelector.HD:
        raise ValueError(
            f"Clearance/enforcement statistics, '{_stats_group}' not valied here."
        )

    match _stats_group:
        case StatsGrpSelector.FC:
            _cnts_func = invres_cnts_byfirmcount
            _cnts_listing_func = invres_cnts_listing_byfirmcount
        case StatsGrpSelector.DL:
            _cnts_func = invres_cnts_bydelta
            _cnts_listing_func = invres_cnts_listing_byhhianddelta
        case StatsGrpSelector.ZN:
            _cnts_func = invres_cnts_byconczone
            _cnts_listing_func = invres_cnts_listing_byhhianddelta

    return _cnts_func(
        _cnts_listing_func(
            _invdata_array_dict,
            _study_period,
            _table_ind_grp,
            _table_evid_cond,
            _invres_spec,
        )
    )


def invres_cnts_listing_byfirmcount(
    _data_array_dict: Mapping[str, Mapping[str, Mapping[str, fid.INVTableData]]],
    _data_period: str = "1996-2003",
    _table_ind_group: INDGRPConstants = INDGRPConstants.ALL,
    _table_evid_cond: EVIDENConstants = EVIDENConstants.UR,
    _invres_spec: INVResolution = INVResolution.CLRN,
    /,
) -> NDArray[np.int64]:
    if _data_period not in _data_array_dict:
        raise ValueError(
            f"Invalid value of data period, {f'"{_data_period}"'}."
            f"Must be one of, {tuple(_data_array_dict.keys())!r}."
        )

    _data_array_dict_sub = _data_array_dict[_data_period][fid.TABLE_TYPES[1]]

    _table_no = table_no_lku(_data_array_dict_sub, _table_ind_group, _table_evid_cond)

    _cnts_array = _data_array_dict_sub[_table_no].data_array

    _ndim_in = 1
    _stats_kept_indxs = []
    match _invres_spec:
        case INVResolution.CLRN:
            _stats_kept_indxs = [-1, -2]
        case INVResolution.ENFT:
            _stats_kept_indxs = [-1, -3]
        case INVResolution.BOTH:
            _stats_kept_indxs = [-1, -3, -2]

    return np.column_stack([
        _cnts_array[:, :_ndim_in],
        _cnts_array[:, _stats_kept_indxs],
    ])


def invres_cnts_listing_byhhianddelta(
    _data_array_dict: Mapping[str, Mapping[str, Mapping[str, fid.INVTableData]]],
    _data_period: str = "1996-2003",
    _table_ind_group: INDGRPConstants = INDGRPConstants.ALL,
    _table_evid_cond: EVIDENConstants = EVIDENConstants.UR,
    _invres_spec: INVResolution = INVResolution.CLRN,
    /,
) -> NDArray[np.int64]:
    if _data_period not in _data_array_dict:
        raise ValueError(
            f"Invalid value of data period, {f'"{_data_period}"'}."
            f"Must be one of, {tuple(_data_array_dict.keys())!r}."
        )

    _data_array_dict_sub = _data_array_dict[_data_period][fid.TABLE_TYPES[0]]

    _table_no = table_no_lku(_data_array_dict_sub, _table_ind_group, _table_evid_cond)

    _cnts_array = _data_array_dict_sub[_table_no].data_array

    _ndim_in = 2
    _stats_kept_indxs = []
    match _invres_spec:
        case INVResolution.CLRN:
            _stats_kept_indxs = [-1, -2]
        case INVResolution.ENFT:
            _stats_kept_indxs = [-1, -3]
        case INVResolution.BOTH:
            _stats_kept_indxs = [-1, -3, -2]

    return np.column_stack([
        _cnts_array[:, :_ndim_in],
        _cnts_array[:, _stats_kept_indxs],
    ])


def table_no_lku(
    _data_array_dict_sub: Mapping[str, fid.INVTableData],
    _table_ind_group: INDGRPConstants = INDGRPConstants.ALL,
    _table_evid_cond: EVIDENConstants = EVIDENConstants.UR,
    /,
) -> str:
    if _table_ind_group not in (
        _igl := [_data_array_dict_sub[_v].ind_grp for _v in _data_array_dict_sub]
    ):
        raise ValueError(
            f"Invalid value for industry group, {f'"{_table_ind_group}"'}."
            f"Must be one of {_igl!r}"
        )

    _tno = next(
        _t
        for _t in _data_array_dict_sub
        if all((
            _data_array_dict_sub[_t].ind_grp == _table_ind_group,
            _data_array_dict_sub[_t].evid_cond == _table_evid_cond,
        ))
    )

    return _tno


def invres_cnts_byfirmcount(
    _cnts_array: NDArray[np.integer[TI]], /
) -> NDArray[np.int64]:
    _ndim_in = 1
    return np.row_stack([
        np.concatenate([
            (f,),
            np.einsum("ij->j", _cnts_array[_cnts_array[:, 0] == f][:, _ndim_in:]),
        ])
        for f in np.unique(_cnts_array[:, 0])
    ])


def invres_cnts_bydelta(_cnts_array: NDArray[np.integer[TI]], /) -> NDArray[np.int64]:
    _ndim_in = 2
    return np.row_stack([
        np.concatenate([
            (f,),
            np.einsum("ij->j", _cnts_array[_cnts_array[:, 1] == f][:, _ndim_in:]),
        ])
        for f in HHI_DELTA_KNOTS[:-1]
    ])


def invres_cnts_byconczone(
    _cnts_array: NDArray[np.integer[TI]], /
) -> NDArray[np.int64]:
    # Prepare to tag clearance stats by presumption zone
    _hhi_zone_post_ranged = hhi_zone_post_ranger(_cnts_array[:, 0] / 1e4)
    _hhi_delta_ranged = hhi_delta_ranger(_cnts_array[:, 1] / 1e4)

    # Step 1: Tag and agg. from HHI-post and Delta to zone triple
    # NOTE: Although you could just map and not (partially) aggregate in this step,
    # the mapped array is a copy, and is larger without partial aggregation, so
    # aggregation reduces the footprint of this step in memory. Although this point
    # is more relevant for generated than observed data, using the same coding pattern
    # in both cases does make life easier
    _ndim_in = 2
    _nkeys = 3
    _cnts_byhhipostanddelta = -1 * np.ones(
        _nkeys + _cnts_array.shape[1] - _ndim_in, dtype=np.int64
    )
    _cnts_byconczone = -1 * np.ones_like(_cnts_byhhipostanddelta)
    for _hhi_zone_post_lim in HHI_POST_ZONE_KNOTS[:-1]:
        _level_test = _hhi_zone_post_ranged == _hhi_zone_post_lim

        for _hhi_zone_delta_lim in HHI_DELTA_KNOTS[:3]:
            _delta_test = (
                (_hhi_delta_ranged > HHI_DELTA_KNOTS[1])
                if _hhi_zone_delta_lim == HHI_DELTA_KNOTS[2]
                else (_hhi_delta_ranged == _hhi_zone_delta_lim)
            )

            _zone_val = HMG_PRESUMPTION_ZONE_DICT[_hhi_zone_post_lim][
                _hhi_zone_delta_lim
            ]

            _conc_test = _level_test & _delta_test

            _cnts_byhhipostanddelta = np.row_stack((
                _cnts_byhhipostanddelta,
                np.array(
                    (
                        *_zone_val,
                        *np.einsum("ij->j", _cnts_array[:, _ndim_in:][_conc_test]),
                    ),
                    dtype=np.int64,
                ),
            ))
    _cnts_byhhipostanddelta = _cnts_byhhipostanddelta[1:]

    for _zone_val in ZONE_VALS:
        # Logical-and of multiple vectors:
        _hhi_zone_test = (
            1
            * np.column_stack([
                _cnts_byhhipostanddelta[:, _idx] == _val
                for _idx, _val in enumerate(_zone_val)
            ])
        ).prod(axis=1) == 1

        _cnts_byconczone = np.row_stack((
            _cnts_byconczone,
            np.concatenate(
                (
                    _zone_val,
                    np.einsum(
                        "ij->j", _cnts_byhhipostanddelta[_hhi_zone_test][:, _nkeys:]
                    ),
                ),
                dtype=np.int64,
            ),
        ))

    return _cnts_byconczone[1:]


def latex_tbl_invres_stats_1dim(
    _inparr: NDArray[np.floating[TF] | np.integer[TI]],
    _totals_row: int | None = None,
    /,
    *,
    return_type_sel: StatsReturnSelector = StatsReturnSelector.CNT,
    sort_order: SortSelector = SortSelector.UCH,
) -> tuple[list[str], list[list[str]]]:
    _ndim_in: int = 1
    _dim_hdr_dict = {
        _v: (_k if _k == "TOTAL" else f"{{{_k}}}")
        for _k, _v in fid.CNT_FCOUNT_DICT.items()
    } | {
        _v: (
            "{[2500, 5000]}"
            if _k == "2,500 +"
            else f"{{[{_k.replace(",", "").replace(" - ", ", ")})}}"
        )
        for _k, _v in fid.CONC_DELTA_DICT.items()
        if _k != "TOTAL"
    }

    if _totals_row:
        _in_totals_row = _inparr[_totals_row, :]
        _inparr_mask = np.ones(len(_inparr), dtype=bool)
        _inparr_mask[_in_totals_row] = False
        _inparr = _inparr[_inparr_mask]
    else:
        _in_totals_row = np.concatenate((
            [fid.TTL_KEY],
            np.einsum("ij->j", _inparr[:, _ndim_in:]),
        ))

    if sort_order == SortSelector.REV:
        _inparr = _inparr[::-1]

    _inparr = np.row_stack((_inparr, _in_totals_row))

    _stats_hdr_list, _stats_dat_list = [], []
    for _stats_row in _inparr:
        _stats_hdr_list += [_dim_hdr_dict[_stats_row[0]]]

        _stats_cnt = _stats_row[_ndim_in:]
        _stats_tot = np.concatenate((
            [_inparr[-1][_ndim_in]],
            _stats_cnt[0] * np.ones_like(_stats_cnt[1:]),
        ))
        _stats_dat_list += _stats_formatted_row(_stats_cnt, _stats_tot, return_type_sel)

    return _stats_hdr_list, _stats_dat_list


def latex_tbl_invres_stats_byzone(
    _inparr: NDArray[np.floating[TF] | np.integer[TI]],
    _totals_row: int | None = None,
    /,
    *,
    return_type_sel: StatsReturnSelector = StatsReturnSelector.CNT,
    sort_order: SortSelector = SortSelector.UCH,
) -> tuple[list[str], list[list[str]]]:
    _ndim_in: int = ZONE_VALS.shape[1]

    _zone_str_keys = list(ZONE_STRINGS)
    if sort_order == SortSelector.REV:
        _inparr = _inparr[::-1]
        _zone_str_keys = _zone_str_keys[:-1][::-1] + [_zone_str_keys[-1]]

    if _totals_row is None:
        _inparr = np.row_stack((
            _inparr,
            np.concatenate((
                [fid.TTL_KEY, -1, -1],
                np.einsum("ij->j", _inparr[:, _ndim_in:]),
            )),
        ))

    _stats_hdr_list, _stats_dat_list = ([], [])
    for _conc_zone in _zone_str_keys:
        _stats_byzone_it = _inparr[_inparr[:, 0] == _conc_zone]
        _stats_hdr_list += [ZONE_STRINGS[_conc_zone]]

        _stats_cnt = np.einsum("ij->j", _stats_byzone_it[:, _ndim_in:])
        _stats_tot = np.concatenate((
            [_inparr[-1][_ndim_in]],
            _stats_cnt[0] * np.ones_like(_stats_cnt[1:]),
        ))
        _stats_dat_list += _stats_formatted_row(_stats_cnt, _stats_tot, return_type_sel)

        if _conc_zone in (2, fid.TTL_KEY):
            continue

        for _stats_byzone_detail in _stats_byzone_it:
            # Only two sets of subtotals detail, so
            # a conditional expression will do here
            _stats_text_color = "HiCoYellow" if _conc_zone == 1 else "BrightGreen"
            _stats_hdr_list += [
                R"{} {{ \({}{}\) }};".format(
                    rf"\node[text = {_stats_text_color}, fill = white, align = right]",
                    ZONE_DETAIL_STRINGS_HHI[_stats_byzone_detail[1]],
                    (
                        ""
                        if _stats_byzone_detail[2] == 0
                        else Rf"{ZONE_DETAIL_STRINGS_DELTA[_stats_byzone_detail[2]]}"
                    ),
                )
            ]

            _stats_cnt = _stats_byzone_detail[_ndim_in:]
            _stats_tot = np.concatenate((
                [_inparr[-1][_ndim_in]],
                _stats_cnt[0] * np.ones_like(_stats_cnt[1:]),
            ))
            _stats_dat_list += _stats_formatted_row(
                _stats_cnt, _stats_tot, return_type_sel
            )

    return _stats_hdr_list, _stats_dat_list


def _stats_formatted_row(
    _stats_row_cnt: NDArray[np.integer[TI]],
    _stats_row_tot: NDArray[np.integer[TI]],
    _return_type_sel: StatsReturnSelector,
    /,
) -> list[list[str]]:
    _stats_row_pct = _stats_row_cnt / _stats_row_tot

    match _return_type_sel:
        case StatsReturnSelector.RIN:
            _stats_row_ci = np.array([
                propn_ci(*g, method="Wilson")
                for g in zip(_stats_row_cnt[1:], _stats_row_tot[1:], strict=True)
            ])
            return [
                [
                    pct_format_str.format(100 * _stats_row_pct[0]),
                    *[
                        ci_format_str.format(*100 * np.array(f)).replace(
                            R"  nan [ nan,  nan] \%", "---"
                        )
                        for f in _stats_row_ci
                    ],
                ]
            ]
        case StatsReturnSelector.RPT:
            return [
                [
                    pct_format_str.format(f).replace(R"nan\%", "---")
                    for f in 100 * _stats_row_pct
                ]
            ]
        case _:
            return [
                [
                    cnt_format_str.format(f).replace(R"nan", "---")
                    for f in _stats_row_cnt
                ]
            ]


def stats_print_rows(
    _invres_stats_hdr_list: list[str], _invres_stats_dat_list: list[list[str]]
) -> None:
    for _idx, _hdr in enumerate(_invres_stats_hdr_list):
        # _hv = (
        #     re.match(r"^\\node.*?(\{.*\});?", _hdr)[1]
        #     if _hdr.startswith(R"\node")
        #     else _hdr
        # )
        _hdr_str = (
            _hdr if _hdr == "TOTAL" else re.fullmatch(r".*?\{(.*)\};?", _hdr)[1].strip()
        )
        print(
            _hdr_str,
            "&",
            " & ".join(_invres_stats_dat_list[_idx]),
            LTX_ARRAY_LINEEND,
            end="",
        )
    print()


def render_table_pdf(
    _table_dottex_pathlist: Sequence[str], _table_coll_path: str, /
) -> None:
    _table_collection_design = latex_jinja_env.get_template(
        "mergeron_table_collection_template.tex.jinja2"
    )
    _table_collection_content = StatsContainer()

    _table_collection_content.path_list = _table_dottex_pathlist

    with Path(DATA_DIR / _table_coll_path).open(
        "w", encoding="utf8"
    ) as _table_coll_file:
        _table_coll_file.write(
            _table_collection_design.render(tmpl_data=_table_collection_content)
        )
        print("\n", file=_table_coll_file)

    _run_rc = subprocess.run(
        f"latexmk -f -quiet -synctex=0 -interaction=nonstopmode -file-line-error -pdflua {_table_coll_path}".split(),  # noqa: S603
        check=True,
        cwd=DATA_DIR,
    )
    if _run_rc:
        subprocess.run(
            "latexmk -quiet -c".split(),  # noqa: S603
            check=True,
            cwd=DATA_DIR,
        )
    del _run_rc

    print(
        f"Tables rendered to path, {f"{Path(DATA_DIR / _table_coll_path).with_suffix(".pdf")}"}"
    )
