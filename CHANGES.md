# xcube-gen-vito changes

## Changes

* the xcube input processor 'vito-s2plus-l2' now uses the functions `process` and `pre_process` 
  from `xcube.core.gen.iproc.XYInputProcessor`. This is due to the need of using `xcube.core.rectify.rectify_dataset`
  for reprojecting sentinel-2 products provided by vito in order to omit memory errors which have been faced when using 
  `xcube.core.reproject.reproject_crs_to_wgs84`. Tile sizes for rectification in `xcube gen` are now derived from
  `output_writer_params` if given in configuration and if it contains a `chunksizes` parameter for 'lat' or 'lon'. 
  This will force the generation of a chunked xcube dataset and will utilize Dask arrays for out-of-core computations. 
  This is very useful for large data cubes whose time slices would otherwise not fit into memory.