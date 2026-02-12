# List of workflow tasks
This is the list of all the tasks and associated recipes in the KMOS workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK                        | RECIPE                  | Used in  <br/>  science reduction | Notes                                                                        |            
|-----------------------------|-------------------------|-----------------------------------|------------------------------------------------------------------------------|
| acquisition_image           | kmo_make_image          | no                                | Creates white-light images for acquisition data                              |
| acquisition_profile         | kmo_fit_profile         | no                                | Fits profiles to white-light images for acquisition                          |
| acquisition_reconstruct     | kmos_reconstruct        | no                                | Creates data cubes from acquisition data                                     |
| arc                         | kmos_wave_cal           | yes                               | Computes the wavelength calibration                                          |
| astrometry_make_image       | kmo_make_image          | no                                | Creates white-light images for astrometry                                    |
| astrometry_profile          | kmo_fit_profile         | no                                | Fits profiles to white-light images for astrometry                           |
| astrometry_reconstruct      | kmos_reconstruct        | no                                | Creates data cubes from astrometry observations                              |
| cubes_combination           | kmos_combine            | optional                          | Combines already reduced data cubes                                          |
| dark                        | kmos_dark               | yes                               | Processes dark exposures                                                     |
| extract_spectra             | kmos_extract_spec       | optional                          | Extracts spectra from science data as input for molecfit                     |
| illumination                | kmos_illumination       | optional                          | Creates the IFU illumination correction from lamp flats                      |
| lamp_flat                   | kmos_flat               | yes                               | Processes lamp flat-field exposures                                          |
| model_on_science            | kmos_molecfit_model     | optional                          | Fits an atmospheric model to science data                                    |
| model_on_standard           | kmos_molecfit_model     | optional                          | Fits an atmospheric model to a telluric standard                             |
| object                      | kmos_sci_red            | yes                               | Extracts science data and creates data cubes                                 |
| object_combination          | kmos_combine            | optional                          | Combines data cubes per object                                               |
| response                    | kmos_gen_telluric       | optional                          | Creates the response from a standard star if molecfit is used                |
| select_reference            | none                    | optional                          | Selects the data for the atmospheric model fit <br>if fit is on science data |
| sky_flat                    | kmos_illumination       | optional                          | Creates the IFU illumination correction from sky flats                       |
| standard                    | kmos_std_star           | yes                               | Processes telluric/flux standard stars                                       |
| telluric_and_response       | kmos_gen_telluric       | optional                          | Creates response and telluric correction if molecfit is not used             |
| telluric_correction         | kmos_molecfit_correct   | optional                          | Applies the telluric correction if molecfit is used                          |
| transmission_on_science     | kmos_molecfit_calctrans | optional                          | Computes the telluric correction if calculated from science data             |
| transmission_on_standard    | kmos_molecfit_calctrans | optional                          | Computes the telluric correction if calculated from standard star            |
