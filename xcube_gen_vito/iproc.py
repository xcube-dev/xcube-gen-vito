# The MIT License (MIT)
# Copyright (c) 2019 by the xcube development team and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Any, Collection, Dict, Optional, Tuple

import xarray as xr
from xcube.core.gen.iproc import DefaultInputProcessor, XYInputProcessor


class VitoS2PlusInputProcessor(XYInputProcessor):
    """
    Input processor for VITO's Sentinel-2 Plus Level-2 NetCDF inputs.
    """

    def __init__(self, **parameters):
        super().__init__('vito-s2plus-l2', **parameters)

    @property
    def default_parameters(self) -> Dict[str, Any]:
        default_parameters = super().default_parameters
        default_parameters.update(input_reader='netcdf4')
        return default_parameters

    def get_time_range(self, dataset: xr.Dataset) -> Tuple[float, float]:
        return DefaultInputProcessor().get_time_range(dataset)

    def get_extra_vars(self, dataset: xr.Dataset) -> Optional[Collection[str]]:
        return ["transverse_mercator"]

    def pre_process(self, dataset: xr.Dataset) -> xr.Dataset:
        # TODO (forman): clarify with VITO how to correctly mask the S2+ variables
        return super().pre_process(dataset)
