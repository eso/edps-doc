# Quick start

This Quick Start Guide walks through the steps to reduce data using the default setup. 

## 1. Setting the workflow

a. After installation and while still in the installation virtual environment (if not, activate it again), start the `EDPS` dashboard by typing:

		edps-gui

The `EDPS` dashboard will start in a browser window. 
	
   ````{figure} figures/dashboard.jpg
   :alt: dashboard
   :name: fig_dashboard
   ```` 

b. On the browser window with the `EDPS` dashboard, press the button `Start EDPS`.

   ````{figure} figures/start_edps.jpg
   :alt: start_edps
   :name: fig_start_edps
   ```` 

c. Choose a pipeline workflow that matches the data to be reduced. The workflows offered in this selector depend on the installed pipelines.

   ````{figure} figures/select_workflow.jpg
   :alt: select_workflow
   :name: fig_select_workflow
   ````

## 2. Selecting the input data

a. Press `Raw Data`.
	
   ````{figure} figures/raw_data.jpg
   :alt: raw_data
   :name: fig_raw_data
   ````
 	
b. Press `Select Inputs`. A selection window will appear that allows to select data that are stored on a local disk.

   ````{figure} figures/select_input.jpg
   :alt: select_input
   :name: fig_select_input
   ````

c. Press `Create Datasets`. A list of datasets appears, one line for each set of science data.
	
   ````{figure} figures/create_datasets.jpg
   :alt: create_datasets
   :name: fig_create_datasets
   ```` 

d. Choose the datasets that should be processed 
	
   ````{figure} figures/send.jpg
   :alt: send
   :name: fig_send
   ```` 
and send them to the processing queue by pressing `Send to Processing Queue`.

## 3. Start the reduction

a. Press `Processing Queue`.

   ````{figure} figures/processing_queue.jpg
   :alt: processing_queue
   :name: fig_processing_queue
   ```` 
	
b.  Press the `Reduce` button. The selected data will now be processed with the default parameters.
	
   ````{figure} figures/reduce.jpg
   :alt: reduce
   :name: fig_reduce
   ```` 


Congratulations, you reduced your first data with the `EDPS` dashboard! All the reduced data are saved in the EDPS_data directory specified when executing `edps-gui` for the first time.
	
---
Go to EDPS quick-start guide [index](../quick/index)
