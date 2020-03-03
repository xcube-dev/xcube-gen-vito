import os
import unittest

import numpy as np
import xarray as xr

from test.helpers import get_inputdata_path
from test.sampledata import create_s2plus_dataset
from xcube.core.dsio import rimraf
from xcube.core.gen.gen import gen_cube

INPUT_FILE = get_inputdata_path('s2plus-input.nc')
OUTPUT_FILE = 's2plus-output.nc'
OUTPUT_ZARR = 's2plus-output.zarr'
OUTPUT_ZARR_tiled = 's2plus-output-tiled.zarr'


def clean_up():
    files = [INPUT_FILE, OUTPUT_FILE, OUTPUT_ZARR, OUTPUT_ZARR_tiled]
    for file in files:
        rimraf(os.path.join('.', file))


class VitoS2PlusProcessTest(unittest.TestCase):

    def setUp(self):
        clean_up()
        dataset = create_s2plus_dataset()
        dataset.to_netcdf(INPUT_FILE)
        dataset.close()

    def tearDown(self):
        clean_up()

    # noinspection PyMethodMayBeStatic
    def test_process_inputs_single(self):
        status = process_inputs_wrapper(
            input_paths=[INPUT_FILE],
            output_path='s2plus-output.nc',
            output_writer='netcdf4')
        self.assertEqual(True, status)

    def test_process_with_tile_size(self):
        status = process_inputs_wrapper(
            input_paths=[INPUT_FILE],
            output_path='s2plus-output.zarr',
            output_writer='zarr',
            output_writer_params=None)
        self.assertEqual(True, status)
        status = process_inputs_wrapper(
            input_paths=[INPUT_FILE],
            output_path='s2plus-output-tiled.zarr',
            output_writer='zarr',
            # output_writer_params=None)
            output_writer_params={'chunksizes': {'lon': 3, 'lat': 2}})
        self.assertEqual(True, status)
        ds_unchunked = xr.open_zarr('s2plus-output.zarr')
        ds_tiled = xr.open_zarr('s2plus-output-tiled.zarr')
        expected_data = np.array([[
            [0.014, 0.014, 0.016998, 0.016998, 0.016998, 0.016998],
            [0.014, 0.014, 0.016998, 0.016998, 0.016998, 0.016998],
            [0.019001, 0.019001, 0.016998, 0.016998, 0.016998, 0.016998],
            [0.019001, 0.019001, 0.016998, 0.016998, 0.016998, 0.016998],
        ]])
        np.testing.assert_allclose(ds_tiled.rrs_443.values, expected_data)
        np.testing.assert_allclose(ds_unchunked.rrs_443.values, expected_data)


# noinspection PyShadowingBuiltins
def process_inputs_wrapper(input_paths=None,
                           output_path=None,
                           output_writer=None,
                           output_writer_params=None):
    return gen_cube(input_paths=input_paths,
                    input_processor_name='vito-s2plus-l2',
                    output_size=(6, 4),
                    output_region=(0.2727627754211426, 51.3291015625, 0.273336261510849, 51.329463958740234),
                    output_resampling='Nearest',
                    output_variables=[('rrs_443', None),
                                      ('rrs_665', None)],
                    output_path=output_path,
                    output_writer_name=output_writer,
                    output_writer_params=output_writer_params,
                    dry_run=False,
                    monitor=None)
