This tab allows to specify and inspect the input data, to specify how deep into the reduction cascade to go
(reduction target), to configure the association preference, and, finally, to create the dataset to reduce.

There are 5 main buttons:

- **`Select input data`**. This button opens a brows window that allows to specify the
  directory where the input data are located. By default, the location of the demo data for the loaded workflow is
  specified.

   ````{figure} figures/select-inputs-dialog.jpg
   :alt: select-inputs-dialog
   :name: fig_select-inputs-dialog
   ```` 
<a name="inspect"></a>
- **`Inspect input data`**. This button allows to inspect the input files. Press this button and a table with the the
  list of input files appears.
  The first part of the table shows the list of the input files, grouped by category. Click on the arrow of each
  category to show the files
  within. Buttons on the left side of each file allows to visualize it
  either with `fv` or `ds9` (if present in your system).

   ````{figure} figures/inspect_1.jpg
   :alt: inspect_1
   :name: fig_inspect_1
   ```` 

  The second part of the table allows to inspect the headers of the various extensions, and also
  it allows to inspect the data extension with interactive Python tools.

   ````{figure} figures/inspect_2.jpg
   :alt: inspect_2
   :name: fig_inspect_2
   ```` 

- **`Select reduction target`**. This window allows to specify the final steps of the reduction cascade, the so-called
  target tasks.
  The tasks, i.e. the various steps of the reduction flow, are grouped by categories, which can be selected from the
  drop
  down menu `Target Category`.

  EDPS processes all the data until the specified target tasks, and triggers all the tasks down in the reduction cascade
  that are needed
  to trigger the target task. For example, if the target task is `science`, and the reduction cascade foresees that also
  the `bias` and `flat_field` tasks are needed to provide the necessary calibrations, then `EDPS` will process
  all and only the biases and the flat fields that are needed to reduce the science data. If there are other biases or
  flat fields that are
  not needed for the specified science exposure, they are not reduced. On the other hand, if the specified target task
  is
  `flat field`, then `EDPS` will reduce all the flat field exposures, plus all and only the biases that are needed for
  those flat fields.

   ````{figure} figures/select_reduction_target.jpg
   :alt: select_reduction_target
   :name: fig_select_reduction_target
   ```` 

  Individual tasks within that category are listed in the `Targets` bar. In the figure below,
  the `Science` category is shown, that contains the tasks called science_spectra and telluric_correction. The
  categories and the tasks depends on the loaded workflow. Tipically, the category `science` is specified by default.
  The category `all` shows all the tasks in that workflow. Tasks that are not desired, can be removed from the list.
  The category `qc1calib` triggers all the calibration and instrument monitoring tasks, but it does not process
  scientific
  images.
  Other target categories are specific for Paranal operations, and are not needed for the general user.

- **`Configure Associations`**. This step allows to specify the basic rules for associating a file to another. The drop
  down menu `Calibration preference` specify the order to follow to look for a calibration that satisfies the
  minimum `Acceptable Calibration Quality`.

  The options of `Calibration preferences` are:

    - `RAW`. First, `EDPS` checks if there are raw calibrations ensuring the best quality level of the
      products. If found, they are associated. If not found, raw calibrations ensuring the second quality
      level of the products are searched. If not found, the next level is searched until the last quality
      level permitted by the specified `Acceptable Calibration Quality`.
      If no raw calibrations are found for none of the quality levels, then `EDPS` searches for master
      calibrations, starting from those ensuring the first quality level. If none are found, the second
      level is searched, and so forth. If no calibrations are found, the association is not done. The detailed rules
      about which type of calibration and with which property to associate
      (e.g. the flat must match the same filter as the science) depends on the specific task and instrument and are
      encoded within the workflow.

    - `MASTER`. Same as `RAW`, but first master calibrations are looked for all the products quality levels
      permitted by the specified `Acceptable Calibration Quality`. Then, if master
      calibrations are not found, the system looks for raw calibrations following all the quality levels. If also no raw
      calibrations are found, then the association is not done.

    - `RAW_PER_QUALITY_LEVEL` (default). First, the system will check if there are raw calibra-
      tions ensuring the first quality level of the products. If not found, MASTER calibrations en-
      suring this level are searched for. If not found, RAW calibrations ensuring the second quality
      level are searched for, if not found MASTER calibrations matching the second quality level are
      searched for. The sequence goes on until the last level permitted by the workflow parameter
      quality_threshold.

    - `MASTER_PER_QUALITY_LEVEL` Same as raw_per_quality_level, but with inverted roles
      for `MASTER` and `RAW` calibrations.

  The options for  `Acceptable Calibration Quality` are:

    - `CALIBRATION PLAN`. This ensures that the time interval between a file and its calibration reflects the
      calibration
      plan foreseen for that instrument. The effective time window depends on each file and instrument.
    - `LEVEL 1`. This uses time intervals a bit larger than what foreseen in the calibration plan, but still within a
      range that ensure product of good quality.
    - `LEVEL 2`. This uses larger time intervals. The final products are good for a quick inspection, but the scientific
      quality of the products might not be the best.
    - `ANY`. This associate the needed calibration, regardless of the time window in the majority of the cases. The
      quality of the products is sub optima; moreover some reduction step might even fail.

  The recommendation for scientific reduction is to use `CALIBRATION PLAN` for scientific reduction, and for a quick
  look is `ANY`.

  ````{figure} figures/configure_associations.jpg
   :alt: configure_associations
   :name: fig_configure_associations
   ```` 
- **`Create Datasets`**. This steps creates the datasets to be reduced until the specified reduction target.
  Datasets, together with all the calibrations needed to process them, are listed in a table. Press the `Create Dataset`
  blue button
  to create the datasets. Selected datasets can be send to the processing queue by pressing
  the `Send to Processing Queue` blue button.
  The datasets can be deleted by pressing the `Delete Dataset` red button. Note that this removes only the dataset
  information, but it does not delete the files from disk.

  ````{figure} figures/create-dataset_2.jpg
   :alt: create-dataset_2
   :name: fig_create-dataset_2
   ```` 

  The content and the file association within a dataset can be inspected by pressing the button ![](figures/inspect.jpg)
  at the end of each dataset row. This shows the association tree as in the figure below.
  Incomplete datasets are marked in red, with the indication of what is missing.

     ````{figure} figures/dataset-tree.jpg
      :alt: dataset-tree
      :name: fig_dataset-tree
      ```` 
