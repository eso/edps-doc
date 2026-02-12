
This window is visible allows to: 

- Select the parameter set. A pre-determined list of workflow parameters and recipe parameters for a given 
  use case. For the majority of the cases, the "science" parameter set can be used.

- Edit the workflow parameters. These are parameters that regulates the reduction strategy, e.g. whether to 
  use a given calibration or not, or to trigger a certain reduction step. Note that if the changes imply that 
  some files not in the dataset are needed, the reduction might fail. In case, go back to the raw data tab, edit the 
  workflow parameters there, and recreate the datasets.

- Edit the recipe parameters. These are parameters associated to the recipe of a given task. 
  Note: the same recipe parameters can be configured differently for the tasks that run the same recipe.
  Default parameters are shown (albeit some parameters can be dynamic, e.g. `EDPS` changes
  their value depending on the type of input data).  

Change the values according to the needs and then select whether to save it to the current or the selected configurations. 
Note, complete configurations cannot be modified, new configurations will be automatically created instead.

