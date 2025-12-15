# List of workflow tasks
This is the list of all the tasks and associated recipes in the XSHOOTER workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK                                              | 	RECIPE                | Used in  <br/>  science reduction | 	Notes                                                                                    |
|---------------------------------------------------|------------------------|-----------------------------------|-------------------------------------------------------------------------------------------|
| acquisition_camera_flat                           | xsh_mflat              | yes      | Create master flat for acquisition camera.                                                |
| arc                                               | xsh_wavecal            | yes      | Compute arc-line tilts and instrument resolution.                                         |
| atmospheric_model_on_science_flux_standard_nod    | xsh_molecfit_model     | optional | Run molecfit_model on the input spectrum.                                                 |
| atmospheric_model_on_science_flux_standard_offset | xsh_molecfit_model     | optional | Note 2.                                                                                   |
| atmospheric_model_on_science_flux_standard_stare  | xsh_molecfit_model     | optional | Note 2.                                                                                   |
| atmospheric_model_on_science_science_nod          | xsh_molecfit_model     | optional | Note 2.                                                                                   |
| atmospheric_model_on_science_science_offset       | xsh_molecfit_model     | optional | Note 2.                                                                                   |
| atmospheric_model_on_science_science_stare        | xsh_molecfit_model     | optional | Note 2.                                                                                   |
| atmospheric_model_on_science_telluric_standard_nod | xsh_molecfit_model     | optional | Note 2.                                                                                   |
| atmospheric_model_on_science_telluric_standard_offset | xsh_molecfit_model     | optional | Note 2.                                                                                   |
| atmospheric_model_on_science_telluric_standard_stare | xsh_molecfit_model     | optional | Note 2.                                                                                   |
| atmospheric_model_on_standard_nod                 | xsh_molecfit_model     | optional | Run molecfit_model on telluric standard spectrum in nod mode.                             |
| atmospheric_model_on_standard_offset              | xsh_molecfit_model     | optional | Run molecfit_model on telluric standard spectrum in offset mode.                          |
| atmospheric_model_on_standard_stare               | xsh_molecfit_model     | optional | Run molecfit_model on telluric standard spectrum in stare mode.                           |
| atmospheric_transmission_for_flux_standard_nod    | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| atmospheric_transmission_for_flux_standard_offset | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| atmospheric_transmission_for_flux_standard_stare  | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| atmospheric_transmission_for_science_nod          | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| atmospheric_transmission_for_science_offset       | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| atmospheric_transmission_for_science_stare        | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| atmospheric_transmission_for_telluric_standard_nod | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| atmospheric_transmission_for_telluric_standard_offset | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| atmospheric_transmission_for_telluric_standard_stare | xsh_molecfit_calctrans | optional | Note 2.                                                                                   |
| bias                                              | xsh_mbias              | yes      | Create master bias.                                                                       |
| dark                                              | xsh_mdark              | optional | Create master dark.                                                                       |
| detmon_nir                                        | detmon_ir_lg           | no       | Compute detector gain and linearity-map, flag abnormal pixels (NIR).                      |
| detmon_optical                                    | detmon_opt_lg          | no       | Compute detector gain and linearity-map, flag abnormal pixels (VIS).                      |
| flats_science                                     | -                      | yes      | Select flats associated with science observations for flat-fielding the flux calibrator.  |
| flats_standard                                    | -                      | yes      | Select flats closer in time to the flux calibrator for flat-fielding the flux calibrator. |
| flexures                                          | xsh_flexcomp           | yes      | Refine the wavelength solution to account for flexure.                                    |
| flux_standard_combination                         | -                      | yes      | Note 2.                                                                                   |
| flux_standard_slit_nod                            | xsh_scired_slit_nod    | yes      | Reduces flux-standard exposure in slit nod mode.                                          |
| flux_standard_slit_offset                         | xsh_scired_slit_offset | yes      | Reduces flux-standard exposure in slit offet mode.                                        |
| flux_standard_slit_stare                          | xsh_scired_slit_stare  | yes      | Reduces flux-standard exposure in slit stare mode.                                        |
| lamp_flat                                         | xsh_mflat              | yes      | Create master flat and order edge traces table frame.                                     |
| lamp_flat_hc                                      | xsh_mflat              | yes      | Create master flat (high counts).                                                         |
| order_definition                                  | xsh_orderpos           | yes      | Trace orders location and curvature.                                                      |
| order_prediction                                  | xsh_predict            | yes      | Compute a first guess dispersion solution and order trace.                                |
| response_offset                                   | xsh_respon_slit_offset | yes      | Compute the instrument response in slit offset mode.                                      |
| response_slit_nod                                 | xsh_respon_slit_nod    | yes      | Compute the instrument response in slit nod mode.                                         |
| response_slit_stare                               | xsh_respon_slit_stare  | yes      | Compute the instrument response in slit stare mode.                                       |
| science_combination                               | -                      | yes      | Note 2.                                                                                   |
| science_ifu_offset                                | science_ifu_offset     | yes      | Reduce science exposure in IFU offset mode.                                               |
| science_ifu_stare                                 | science_ifu_stare      | yes      | Reduce science exposure in IFU stare mode.                                                |
| science_slit_nod                                  | xsh_scired_slit_nod    | yes      | Reduce science exposure in IFU nod mode.                                                  |
| science_slit_offset                               | xsh_scired_slit_offset | yes      | Reduce science exposure in slit offset mode.                                              |
| science_slit_stare                                | xsh_scired_slit_stare  | yes      | Reduce science exposure in slit stare mode.                                               |
| select_flux_standard_to_combine                   | -                      | yes      | Note 2.                                                                                   |
| select_science_to_combine                         | -                      | yes      | Note 2.                                                                                   |
| select_telluric_standard_to_combine               | -                      | yes      | Note 2.                                                                                   |
| telluric_corrected_flux_standard_nod              | xsh_molecfit_correct | optional | Apply telluric correction to flux-standard spectrum observed in nod mode.                 |
| telluric_corrected_flux_standard_offset           | xsh_molecfit_correct | optional | Apply telluric correction to flux-standard spectrum observed in offset mode.              |
| telluric_corrected_flux_standard_stare            | xsh_molecfit_correct | optional | Apply telluric correction to flux-standard spectrum observed in stare mode.               |
| telluric_corrected_science_nod                    | xsh_molecfit_correct | optional | Apply telluric correction to science spectrum in nod mode.                                |
| telluric_corrected_science_offset                 | xsh_molecfit_correct | optional | Apply telluric correction to science spectrum in offset mode.                             |
| telluric_corrected_science_stare                  | xsh_molecfit_correct | optional | Apply telluric correction to science spectrum in stare mode.                              |
| telluric_corrected_telluric_standard_nod          | xsh_molecfit_correct | optional | Apply telluric correction to telluric-standard spectrum observed in nod mode.             |
| telluric_corrected_telluric_standard_offset       | xsh_molecfit_correct | optional | Apply telluric correction to telluric-standard spectrum observed in offset mode.          |
| telluric_corrected_telluric_standard_stare        | xsh_molecfit_correct | optional | Apply telluric correction to telluric-standard spectrum observed in stare mode.           |
| telluric_standard_combination                     | -                      | yes      | Note 2.                                                                                   |
| telluric_standard_slit_nod                        | xsh_scired_slit_nod    | yes      | Reduce telluric exposure in slit nod mode.                                                |
| telluric_standard_slit_offset                     | xsh_scired_slit_offset | yes      | Reduce telluric exposure in slit offset mode.                                             |
| telluric_standard_slit_stare                      | xsh_scired_slit_stare  | yes      | Reduce telluric exposure in slit stare mode.                                              |
| wavelength_calibration_2d                         | xsh_2dmap              | yes      | Compute wavelength and spatial resampling solution.                                       |
