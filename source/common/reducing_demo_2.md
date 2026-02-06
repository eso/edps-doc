
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

c. (Optional). Select the reduction target, configure the workflow parameter and specify the association preferences. 
Thise steps are optional. For more information please consult the full 
edps-gui guide [here](../edpsgui/raw_data_.md#select_reduction_target).

d. Press `Create Datasets`. A list of datasets appears, one line for each set of science data.
	
   ````{figure} figures/create_datasets.jpg
   :alt: create_datasets
   :name: fig_create_datasets
   ```` 

e. Choose the datasets that should be processed 
	
   ````{figure} figures/send.jpg
   :alt: send
   :name: fig_send
   ```` 
and send them to the data reduction queue by pressing `Submit to Reduction Queue`. Note that this action does not start the 
reduction automatically.

## 3. Start the reduction

a. Press `Reduction Queue`.

   ````{figure} figures/processing_queue.jpg
   :alt: processing_queue
   :name: fig_processing_queue
   ```` 
	
b.  Press the `Reduce` button. The selected data will now be processed with the default parameters.
	
   ````{figure} figures/reduce.jpg
   :alt: reduce
   :name: fig_reduce
   ```` 


Congratulations! You reduced your first data with the `EDPS` dashboard! All the reduced data are saved in the EDPS_data directory specified when executing `edps-gui` for the first time.
	