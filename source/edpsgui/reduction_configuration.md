# Reduction configuration editor

This editor allows to select the data reduction strategy for a given dataset by specifying workflow and recipe
parameters.
To open the editor, go on the <a href="gui.html#processing_queue">Processing Queue</a> tab and click on
the ![](figures/configure_dataset.jpg) button next to the dataset you desire to configure the reduction for.

The editor is divided into 2 parts. The first is shown in {numfig}`reduction_configuration_editor_1`. It displays the
dataset the configuration refers to and it allows to load, save, edit, and select different configurations for the same
dataset. Comments describing the characteristics of the configuration can be written in the apposite field and copied
into the selected configuration.

```{figure} figures/reduction_configuration_editor_1.jpg
   :alt: reduction_configuration
   :name: fig-reduction_configuration_editor_1
   :figclass: left-caption

   The Reduction Configuration editor (upper part), where the dataset and the associated configurations are visible.
   ```

The second part of the editor shown in {numfig}`reduction_configuration_editor_2` lists the workflow and recipe
parameters that can be modified to customize the data reduction.

```{figure} figures/reduction_configuration_editor_2.jpg
   :alt: reduction_configuration
   :name: fig-reduction_configuration_editor_2
   :figclass: left-caption

   The Reduction Configuration editor (lower part), where workflow and recipe parameters can be edited.
   ```

There are several parameters sets available, that are configured to serve specific purposes. The `science_parameters` (
default) set is the one set for general reduction purposes, the `qc0_parameters` defines a strategy for quick analysis,
that is typically carried on at the Observatory during night observations. The `idp_parameters` set is configured for
the automatic archival data reduction carried on at ESO. For the general users purposes, the default is the best choice.

The various parameters present in the selected set are divided in workflow parameters and recipe parameters. Workflow
parameters are for general purpose, e.g. they
can regulate which data reduction step to include in the process (e.g. whether to apply telluric correction or not) or
which calibration to avoid in the process
(e.g. do not perform dark current correction). Each workflow has different workflow parameters.
The recipe parameters are grouped in tasks. Each task is associated to a given recipe. The table shows the recipe
parameters for the
recipe associated to that task. Default parameters are shown (albeit some parameters can be dynamic, e.g. `EDPS` change
their value depending on the type of input data). The user can specify the value to use for each parameter. The user choice overrides any
recipe default value or any dynamic value the workflow sets automatically.
Each workflow has a different set of tasks and different recipes.

Note: the recipe parameters can be configured differently even for the tasks that run the same recipe.



