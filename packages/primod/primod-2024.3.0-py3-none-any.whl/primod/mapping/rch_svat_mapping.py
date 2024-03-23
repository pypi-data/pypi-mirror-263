import numpy as np
import xarray as xr
from imod import mf6
from imod.msw.fixed_format import VariableMetaData
from numpy.typing import NDArray

from primod.mapping.mappingbase import MetaModMapping
from primod.typing import Int


class RechargeSvatMapping(MetaModMapping):
    """
    This contains the data to connect MODFLOW 6 recharge cells to MetaSWAP
    svats.

    This class is responsible for the file `rchindex2svat.dxc`.

    Parameters
    ----------
    svat: array of floats (xr.DataArray)
        SVAT units. This array must have a subunit coordinate to describe
        different land uses.
    recharge: mf6.Recharge
        Modflow 6 Recharge package to connect to. Note that the recharge rate
        should be provided as a 2D grid with a (y, x) dimension. MetaModMapping
        will throw an error if a grid is provided with different dimensions.
    """

    _file_name = "rchindex2svat.dxc"
    _metadata_dict = {
        "rch_id": VariableMetaData(10, 1, 9999999, int),
        "free": VariableMetaData(2, None, None, str),
        "svat": VariableMetaData(10, 1, 9999999, int),
        "layer": VariableMetaData(5, 0, 9999, int),
    }

    _with_subunit = ("rch_id", "svat", "layer")
    _to_fill = ("free",)

    def __init__(self, svat: xr.DataArray, recharge: mf6.Recharge, index: NDArray[Int]):
        super().__init__()
        self.index = index
        self.dataset["svat"] = svat
        self.dataset["layer"] = xr.full_like(svat, 1)
        rate = recharge.dataset["rate"]
        if "layer" in rate.dims:
            rate_no_layer = rate.squeeze("layer", drop=True)
        else:
            # 'layer' can be still in a coord, so ensure is also dropped
            rate_no_layer = rate.drop_vars("layer", errors="ignore")
        self.dataset["rch_active"] = rate_no_layer.notnull()
        self._pkgcheck()
        self._create_rch_id()

    def _create_rch_id(self) -> None:
        self.dataset["rch_id"] = xr.full_like(
            self.dataset["svat"], fill_value=0, dtype=np.int64
        )

        n_subunit = self.dataset["subunit"].size
        n_rch = self.dataset["rch_active"].sum()

        rch_active = self.dataset["rch_active"].to_numpy()

        # recharge does not have a subunit dimension, so tile for n_subunits
        rch_id: NDArray[np.int_] = np.tile(np.arange(1, n_rch + 1), (n_subunit, 1))

        self.dataset["rch_id"].to_numpy()[:, rch_active] = rch_id

    def _pkgcheck(self) -> None:
        rch_dims = self.dataset["rch_active"].dims
        if rch_dims != ("y", "x"):
            raise ValueError(
                "Recharge grid can only have dimensions ('y', 'x'). Got "
                f"{rch_dims} instead"
            )

        # Check if active msw cell inactive in recharge
        active = self.dataset["svat"] != 0
        inactive_in_rch = active > self.dataset["rch_active"]

        if inactive_in_rch.any():
            raise ValueError(
                "Active MetaSWAP cell detected in inactive cell in Modflow6 recharge"
            )
