# List of workflow tasks
This is the list of all the tasks and associated recipes in the EFOSC workflows. 


| TASK                       | 	RECIPE            | Used in  <br/>  science reduction | 	Notes                                                     |
|----------------------------|--------------------|-----------------------------------|------------------------------------------------------------|
| bias                       | efosc_bias  	      | yes (both)	                       | Creates MASTER_BIAS                                        |
| photometric_standard	      | efosc_zeropoint    | yes (imaging)	                    | Computes photometric zeropoint and processes standard star |
 | science_imaging            | efosc_img_science  | yes (imaging)                     | Reduces raw images                                         |
| science_spectrum           | efosc_science      | yes (spectroscopy)                | Reduces raw spectra (long-slit and MOS)                    |
| sky_flat                   | efosc_img_sky_flat | yes (imaging)                     | Reduces sky flats                                          |
| spectroscopic_calibrations | efosc_calib        | yes (spectroscopy)                | Process spectroscopic calibrations (flats and arcs)        |
| spectroscopic_standard     | efosc_science      | yes (spectroscopy)                | Reduces raw standard stars                                 |


    | spectroscopic_standard     |
    | sky_flat                   |
