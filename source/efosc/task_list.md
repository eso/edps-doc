# List of workflow tasks
This is the list of all the tasks and associated recipes in the EFOSC workflows. 


| TASK                       | 	RECIPE            | Used in workflow  | 	Notes                                                     |
|----------------------------|--------------------|-------------------|------------------------------------------------------------|
| bias                       | efosc_bias  	      | both	        | Creates MASTER_BIAS                                        |
| photometric_standard	      | efosc_zeropoint    | imaging	    | Computes photometric zeropoint and processes standard star |
 | science_imaging            | efosc_img_science  | imaging     | Reduces raw images                                         |
| science_spectrum           | efosc_science      | spectroscopy | Reduces raw spectra (long-slit and MOS)                    |
| sky_flat                   | efosc_img_sky_flat | imaging     | Reduces sky flats                                          |
| spectroscopic_calibrations | efosc_calib        | spectroscopy | Process spectroscopic calibrations (flats and arcs)        |
| spectroscopic_standard     | efosc_science      | spectroscopy | Reduces raw standard stars                                 |
