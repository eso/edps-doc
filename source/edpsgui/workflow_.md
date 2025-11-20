This tab gives information about the workflow, that can be accessed by clicking on the available sub-tabs:

- **Task dependencies**. It shows the connection between each task
  and sub-workflows. The tasks are the individual processing steps
  that run a specific pipeline recipe. A sub-workflow groups tasks
  of similar purposes to simplify the overall data flow structure.
  Each sub-workflow is also illustrated with the relations between the
  tasks within it.

  The tasks descriptor indicates the name of the task, the recipe,
  the main input and the associated inputs. The descriptor also
  indicates whether an associated input has to satisfy a certain
  condition to be associated (e.g., a calibration X is associated only
  if the user specifies it in the preferences, or if the main input is
  obtained with a certain instrument setup). Descriptor for the
  subworkflows indicates the tasks within it, and the corresponding
  main inputs and recipes.

  The color of the lines connecting tasks and subworkflows mirror the
  color they have inside the descriptors. {numref}`fig-workflow-tab` shows an example of this tab.

   ```{figure} figures/workflow-tab.jpg
   :alt: workflow-tab
   :name: fig-workflow-tab
   :figclass: left-caption

   The EDPS dashboard, showing part of the task dependencies within the FORS2 spectroscopic workflow.
   ```


- **Dataflow**. It is a simpler representation of the workflow. It
  shows the categories of the data sources of the raw data, the
  individual tasks (in green) and the subworkflows (in orange). It
  provides a global view of the data reduction chain.
  {numref}`fig-load-flow` shows an example of this tab.

   ```{figure} figures/load-flow.jpg
   :alt: load-flow
   :name: fig-load-flow
   :figclass: left-caption

   The EDPS dashboard, showing the top-level data flow structure of the FORS2 spectroscopic workflow.
   ```

- **Data sources**. It shows the association map, with the definition of the various datasources, their properties
  such as

    * **Classification**. The types of files that belong to this
      datasource. The classification is the tag assigned to the file
      used by the processing recipe. Note that a single datasource
      (e.g. SCIENCE) can include files with different classifications
      (e.g., SCIENCE_LSS, SCIENCE_MOS, SCIENCE_MXU), as they are
      processed by different algorithms by the pipeline recipe (fors_science).

    * **setup**. The list of header keywords used to recognize the
      instrumental setup used to obtain those observations.

    * **grouping**. The list of header keywords used to group the files
      within the same classification. Files of the same group (e.g. that
      have the same value of the header keywords in this list) are input
      to the same recipe execution.

    * **Task**. The name of the task that have that datasource as main
      input. Note that a datasource can be the main input of more than
      one task.

    * **Recipe**. The name of the recipe executed to process that
      datasource. Because a datasource can be the main input of more
      than one task, it can be processed by more than one recipe.

    * **Static calibrations**. Association map between static
      calibrations, datasources, and tasks. An `x` indicates that that
      static calibration is needed by a given task to process a given
      datasource.

- **Documentation**. Links to the relevant documentation files for
  that pipeline.

- **Code**. It shows the Python code of each file in the
  workflow. The dropdown menu `Select file` allows to select the
  file to inspect. Files cannot be edited from the GUI. If changes are needed, edit the file with an external editor, 
  close and reopen the EDP-GUI for the modification to have an effect.