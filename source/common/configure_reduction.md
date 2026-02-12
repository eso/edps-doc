The data reduction of each dataset can be configured according to the scientific needs using an appropriate configuration editor.
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

```{include} ../common/workflow_parameters.md
```

```{figure} figures/configuration_editor_4.jpg
   :alt: configuration_editor_4
   :name: configuration_editor_4
```





