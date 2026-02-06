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

**Parameters**

T.B.D.


%
%There are several parameters sets available, that are configured to serve specific purposes. The `science_parameters` (
%default) set is the one set for general reduction purposes, the `qc0_parameters` defines a strategy for quick analysis,
%that is typically carried on at the Observatory during night observations. The `idp_parameters` set is configured for
%the automatic archival data reduction carried on at ESO. For the general users purposes, the default is the best choice.
%
%The various parameters present in the selected set are divided in workflow parameters and recipe parameters. Workflow
%parameters are for general purpose, e.g. they
%can regulate which data reduction step to include in the process (e.g. whether to apply telluric correction or not) or
%which calibration to avoid in the process
%(e.g. do not perform dark current correction). Each workflow has different workflow parameters.
%The recipe parameters are grouped in tasks. Each task is associated to a given recipe. The table shows the recipe
%parameters for the
%recipe associated to that task. Default parameters are shown (albeit some parameters can be dynamic, e.g. `EDPS` change
%their value depending on the type of input data). The user can specify the value to use for each parameter. The user choice overrides any
%recipe default value or any dynamic value the workflow sets automatically.
%Each workflow has a different set of tasks and different recipes.
%
%Note: the recipe parameters can be configured differently even for the tasks that run the same recipe.



