# List of workflow tasks
This is the list of all the tasks and associated recipes in the XSHOOTER workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK        | 	RECIPE          | Used in  <br/>  science reduction     | 	Notes                          |
|-------------|--------------------|---------------------------------------|----------------------------------|
| task 1      | recipe 1  	        | yes/no/optional	                    | Note 1.                          |
| task 2	   | recipe 2 	        | yes/no/optional	                    | Note 2.                          |
