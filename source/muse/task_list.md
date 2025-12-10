# List of workflow tasks
This is the list of all the tasks and associated recipes in the muse workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK                            | 	RECIPE            | Used in  <br/>  science reduction | 	Notes                                                             |            
|---------------------------------|---------------------|-------------------------------------|--------------------------------------------------------------------|
| alignment	                      | muse_exp_align	  | yes	                                | Aligns a set of exposures for combination.                         |
| alignment_sky	                  | muse_exp_align	  | no	                                 | Aligns a set of sky exposures for combination.                     |
| astrometry	                     | muse_astrometry	  | no	                                 | Computes astrometry.                                               |
| autocalibration_from_object_sky | none		          | no	                                 | Selects sky expousres for additional slice-to-slice flat fielding. |
| bias	                           | muse_bias	          | yes	                                | Computes the masterbias.                                           |
| dark			                         | muse_dark	     |optional| 	 Computes the master dark.                                        |
| geometry		                      | muse_geometry    |optional| 	Generates geometry calibrations.			                               |
| lamp_flat		                     | muse_flat	     |yes     | 	Computes master flat field.				                                   |
| line_spread_function_arc        | muse_lsf	     |yes     | 	Computes LSF from arc exposures.			                               |
| line_spread_function_lsf        | muse_lsf	     |optional| 	Computes LSF from dedicated calibrations.		                       |
| linearity_and_gain	             | muse_lingain     |no      | 	Computes linearity and gain correction.			                        |
| object			                       | muse_scipost     |yes     | 	Creates a datacube from individual scientific observations.       |
| object_combination	             | muse_exp_combine |yes     | 	Creates a datacube from combined scientific observations.         |
| object_sky		                    | muse_scipost     |no      | 	Processes sky exposures as they were science exposures.	          |
| preprocess_astrometry	          | muse_scibasic    |optional| 	Reduces astrometric calibrations.			                              |
| preprocess_science	             | muse_scibasic    |yes     | 	Reduces science exposures.				                                    |
| preprocess_sky		                | muse_scibasic    |yes     | 	Reduces sky exposures.					                                       |
| preprocess_sky_sci	             | muse_scibasic    |no      | 	Reduces sky exposures as they were science exposures.	            |
| preprocess_standard	            | muse_scibasic    |yes     | 	Reduces standard star observations.			                            |
| response		                      | muse_standard    |yes     | 	Computes the response function and atmospheric transmission.      |
| sky			                          | muse_create_sky  |yes     | 	Computes the sky background from dedicated sky exposures.         |
| sky_combination	                | muse_exp_combine |no      | 	Combines sky frames as they were science exposures.	              |
| sky_flat		                      | muse_twilight    |optional| 	Processes skyflats for illumination correction.		                 |
| throughput		                    | muse_ampl	     |no      | 	Computes the throughput.				                                      |
| wavelength		                    | muse_wavecal     |yes     | 	Computes wavelength calibration.			                               |


---
Go to MUSE EDPS tutorial [index](../muse/index)