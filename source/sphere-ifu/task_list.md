# List of workflow tasks
This is the list of all the tasks and associated recipes in the SPHERE-IFS workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK                       | RECIPE                        | Used in <br/> science reduction | Notes                                                                                                             |
|----------------------------|-------------------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ifs_coronagraph_center     | sph_ifs_science_dr           | optional                        | Reduces center frames to determine stellar position behind coronagraph.                                           |
| ifs_dark                   | sph_ifs_master_dark          | yes                             | Creates master dark (`IFS_MASTER_DARK`) and bad-pixel map.                                                        |
| ifs_det_flat_broad_band    | sph_ifs_master_detector_flat | yes                             | Generates broadband detector flat used for small-scale pixel-to-pixel correction.                                 |
| ifs_det_flat_narrow_band1  | sph_ifs_master_detector_flat | yes                             | Produces narrow-band detector flat component.                                                                     |
| ifs_det_flat_narrow_band2  | sph_ifs_master_detector_flat | yes                             | Produces narrow-band detector flat component.                                                                     |
| ifs_det_flat_narrow_band3  | sph_ifs_master_detector_flat | yes                             | Produces narrow-band detector flat component.                                                                     |
| ifs_det_flat_narrow_band4  | sph_ifs_master_detector_flat | yes                             | Produces narrow-band detector flat component.                                                                     |
| ifs_distortion_map         | sph_ifs_distortion_map       | yes                             | Measures geometric distortion via point-pattern comparison; outputs distortion map and optional residual map.     |
| ifs_ifu_flat               | sph_ifs_instrument_flat      | yes                             | Produces total instrument flat and/or IFU (lenslet) flat.                                                         |
| ifs_instrument_background  | sph_ifs_cal_background       | yes                             | Measures instrumental background in counts/s per pixel.                                                           |
| ifs_science                | sph_ifs_science_dr           | yes                             | Main science reduction task; applies flats, background/dark subtraction, optional ADI and spectral deconvolution. |
| ifs_science_flux           | sph_ifs_science_dr           | optional                        | Processes FLUX frames (star offset from coronagraph) to measure stellar flux.                                     |
| ifs_sky_background         | sph_ifs_cal_background       | yes                             | Processes sky background frames for background calibration.                                                       |
| ifs_spectra_positions      | sph_ifs_spectra_positions    | yes                             | Associates pixels with lenslets and assigns initial wavelength solution; produces Pixel Description Table (PDT).  |
| ifs_standard_astrometry    | sph_ifs_science_dr           | optional                        | Reduces astrometric standard observations (currently treated as science data).                                    |
| ifs_standard_flux          | sph_ifs_science_dr           | optional                        | Reduces flux standard observations (currently treated as science data).                                         |
| ifs_static_bad_pixel_map   | sph_ifs_master_dark          | yes                             | Produces static bad-pixel map (`IFS_STATIC_BADPIXELMAP`) from master dark.                                        |
| ifs_wavelength_calibration | sph_ifs_wave_calib           | yes                             | Refines pixel-to-wavelength solution using calibration lines; updates PDT and QC metrics.                         |
