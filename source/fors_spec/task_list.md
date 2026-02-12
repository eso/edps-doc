# List of workflow tasks
This is the list of all the tasks and associated recipes in the FORS workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK        | 	RECIPE       | Used in  <br/>  science reduction     | 	Notes                          |
|-------------|----------------------|---------------------------------------|---------------------------------|
| task 1      | recipeadfgadfg	     | yes/no/optional	                     | Note 1.                          |
| task        | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| calibration_std | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| telluric_correction | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| calibration_hc_lss | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| bias | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| calibration_hc_std | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| standard_mos | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| calibration_lss | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| science_spectra | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| lamp_monitor | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| calibration_mos | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| standard_lss | recipe 2 	     | yes/no/optional	                     | Note 2.                          |
| calibration_mxu | recipe 2 	     | yes/no/optional	                     | Note 2.                          |


