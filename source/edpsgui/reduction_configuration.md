<a name="association_levels"></a>
# Association levels

```{include} ../common/association_levels.md
```
<a name="reduction_configuration_editor"></a>
# Reduction configuration editor

This editor allows to configure the data reduction for a given dataset by specifying workflow and recipe
parameters.
Note: some workflow parameters were already configured before creating the dataset and sending it to the reduction queue.
Here, they can be changed again. Please, note that the parameters have an effect only on the files that are already in the dataset. 
If one specifies a parameter that should include extra files in the dataset (e.g., the inclusion of more calibrations), files are not added and the reduction might fail. 
If you need to change a parameter that modifies the dataset content, please go back to the Raw data tab and create a new dataset.

To open the editor, click on
the wheel button ![](figures/configure_dataset.jpg) next to the dataset you desire to configure the reduction for. A window with the
configuration editor appears as shown the figure below.

```{figure} figures/configuration_editor_0.jpg
   :alt: configuration_editor_0
   :name: configuration_editor_0
   :figclass: left-caption

The Reduction Configuration editor.
```

The editor is divided into 4 parts, which can be accessed pressing the corresponding expansion arrow. 

**Current configuration** It indicates the name of the selected configuration for a given dataset.
```{figure} figures/configuration_editor_1.jpg
   :alt: configuration_editor_1
   :name: configuration_editor_1
```
**Other configurations** It allows to specify other configurations, to which the changes shall be copied to.
```{figure} figures/configuration_editor_2.jpg
   :alt: configuration_editor_2
   :name: configuration_editor_2
```
**Comment** It allows to specify a comment to describe the configuration. It is possible to append or replace a comment.
Comments can be changed on all configurations. It is possible to save the comment for the current configuration only, or for all
the selected configurations.

```{figure} figures/configuration_editor_3.jpg
   :alt: configuration_editor_3
   :name: configuration_editor_3
```
**Parameters**

This window allows to: 

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


```{figure} figures/configuration_editor_4.jpg
   :alt: configuration_editor_4
   :name: configuration_editor_4
```



