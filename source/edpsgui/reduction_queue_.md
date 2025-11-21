The **Reduction Queue* main page is shown in  {numref}`fig-processing_queue`:
The main table shown in this page lists all the datasets that are in the queue.
Each dataset has a list of "configurations", e.g. the individual reductions 
of that same dataset with different parameters.
Each dataset configuration has a status, that could be either: 
  - "new": the configuration has never been processed yet.
  - "completed": the reduction of that dataset with that configuration has been sucessfully executed.
  - "pending": the reduction is scheduled but no jobs has been executed yet
  - "running": the reduction has started, some jobs have been completed, some jobs are running and other pending.
  - "failed": the reduction terminated but some jobs have failed.

Only "new" or "failed" configurations can be reduced. "Completed" configurations can be modified: in this way a new 
configuration is created and can be processed.


At the end of the raw of each configuration, the button ![](figures/configure_dataset.jpg) allows to specify the 
data reduction parameters for a given dataset, and therefore it allows to create a different configuration for the same dataset. 
See [here](reduction_configuration.md#reduction-configuration-editor) for more details on how to configure the reduction.

   ```{figure} figures/processing_queue.jpg
   :alt: processing_queue
   :name: fig-processing_queue
   :figclass: left-caption

   The Processing Queue main tab. The top part shows the datasets and their configuration listed for 
   processing and the main command buttons. The configuration status is reported.
   The lower part indicates the reduction progress.
   ```


After creating a new configuration, press the button ![](figures/start_reduction_all.jpg) to start the reduction of all the selected
datasets.
The expand button  ![](figures/expand.jpg) next to each configuration, allows to see the list of the tasks and their status.
The button with
the magnifying lens ![](figures/magnifying.jpg) next to each task, shows the graphic report associated to that specific
reduction step.
On the other hand, the same button next to the dataset, shows the graphic report of the last step of the data reduction.

The button ![](figures/inspect.jpg) next to each dataset allows to inspect the various products of the reduction, as done for the input data (see [here](#inspect)).

The results of a reduction can be stored in a desired location by pressing the button ![](figures/archive.jpg) (see
Section ZZ for further information).