This tab allows to specify and inspect the input data, to specify how deep into the reduction cascade to go
(reduction target), to configure the association preference, and, finally, to create the dataset to reduce.

There are 4 main buttons:

- **Select the input data**. The button "Select Inputs" opens a window that allows to specify the
  directory where the input data are located. 

   ````{figure} figures/select-inputs-dialog.jpg
   :alt: select-inputs-dialog
   :name: fig_select-inputs-dialog
   ```` 
<a name="inspect"></a>
- **`Inspect the input data`**. The button "Inspect Inputs" allows to inspect the input files. Press this button and a table with the the
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

- **Select reduction target**. This window allows to specify the final steps of the reduction cascade, the so-called
  "target tasks".
  The tasks, i.e. the various steps of the reduction flow, are grouped by categories, which can be selected from the
  drop-down menu "Target Category".

  EDPS processes all the data until the specified target tasks, and triggers all the tasks down in the reduction cascade
  that are needed
  to trigger the target task. For example, if the target task is "science", and the reduction cascade foresees that also
  the "bias" and "flat_field" tasks are needed to provide the necessary calibrations, then EDPS will process
  all and only the biases and the flat fields that are needed to reduce the science data. If there are other biases or
  flat fields that are
  not needed for the specified science exposure, they are not reduced. On the other hand, if the specified target task
  is
  "flat field", then EDPS will reduce all the flat field exposures, plus all and only the biases that are needed for
  those flat fields.

   ````{figure} figures/select_reduction_target.jpg
   :alt: select_reduction_target
   :name: fig_select_reduction_target
   ```` 

  Individual tasks within that category are listed in the "Targets" bar. In the figure below,
  the "Science" category is shown, that contains the tasks called science_spectra and telluric_correction. The
  categories and the tasks depends on the loaded workflow. Typically, the category "science" is specified by default.
  The category "all" shows all the tasks in that workflow. Tasks that are not desired, can be removed from the list.
  The category "qc1calib" triggers all the calibration and instrument monitoring tasks, but it does not process
  scientific
  images.
  Other target categories are specific for Paranal operations, and are not needed for the general user.


- **Create Dataset**. This steps creates the datasets to be reduced until the specified reduction target.
  Datasets, together with all the calibrations needed to process them, are listed in a table. Press the "Create Dataset"
  blue button
  to create the datasets. Selected datasets can be send to the processing queue by pressing
  the "Submit to Reduction Queue" blue button.
  
  ````{figure} figures/create-dataset.jpg
   :alt: create-dataset
   :name: fig_create-dataset
   ```` 

  The content and the file association within a dataset can be inspected by pressing the button ![](figures/inspect.jpg)
  at the end of each dataset row. This shows the association tree as in the figure below.
  Incomplete datasets are marked in red, with the indication of what is missing.

     ````{figure} figures/dataset-tree.jpg
      :alt: dataset-tree
      :name: fig_dataset-tree
      ```` 
