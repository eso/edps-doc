# List of workflow tasks
This is the list of all the tasks and associated recipes in the SPHERE-IRDIS workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK                              | RECIPE                         | Used in <br/> science reduction | Notes                                                                                                   |
|-----------------------------------|--------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------|
| irdis_coronagraph_center          | sph_ird_star_center            | yes (coronagraphic data)        | Determines stellar position behind coronagraph using waffle images; outputs center table for registration. |
| irdis_dark_imaging                | sph_ird_master_dark            | yes                             | Creates `MASTER_DARK` by combining dark frames and produces hot/static bad-pixel map.                  |
| irdis_distortion_map              | sph_ird_distortion_map         | optional                        | Derives geometric distortion solution via point-pattern matching; outputs polynomial distortion model. |
| irdis_flat_field                  | sph_ird_master_detector_flat   | yes                             | Generates detector master flat; includes linearity fit and updated bad-pixel map.                      |
| irdis_instrument_background       | sph_ird_ins_bg                 | yes                             | Produces instrumental background (`INS_BG`) used for subtraction when darks are unavailable.           |
| irdis_science_flux_imaging        | sph_ird_science_dbi            | optional                        | Reduces off-axis flux frames for coronagraphic observations; not applied to final science calibration. |
| irdis_science_flux_polarimetry    | sph_ird_science_dpi            | optional                        | Flux reduction equivalent for DPI mode; output not used in science calibration.                        |
| irdis_science_imaging             | sph_ird_science_dbi            | yes (DBI/CI modes)              | Main DBI science reduction with dark/background subtraction, flat-fielding, optional ADI/SDI.          |
| irdis_science_polarimetry         | sph_ird_science_dpi            | yes (DPI mode)                  | Produces polarization (P) and intensity (I) products.                                                   |
| irdis_science_spectroscopy        | sph_ird_science_spectroscopy   | yes (LSS mode)                  | Reduces spectroscopy data via dark subtraction, flat-fielding, and frame combination.                  |
| irdis_sky_background              | sph_ird_sky_bg                 | optional                        | Creates sky background (`SKY_BG`) calibration used for science background subtraction.                 |
| irdis_standard_astrometry_imaging | sph_ird_science_dbi            | optional                        | Processes astrometric standard observations for calibration monitoring.                                |
| irdis_standard_flux_imaging       | sph_ird_science_imaging        | optional                        | Reduces photometric standards for zero-point calibration.                                               |
| irdis_static_bad_pixel_map        | sph_ird_master_dark            | yes                             | Static bad pixels identified during master dark creation and propagated to later reductions.           |
| irdis_wavecal_spectroscopy        | sph_ird_wave_calib             | yes (LSS only)                  | Computes wavelength solution and updates Pixel Description Table (PDT).                                |
