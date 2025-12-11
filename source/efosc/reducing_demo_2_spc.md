
a. Press `Raw Data`.
	
   ````{figure} figures/raw_data_spc.jpg
   :alt: raw_data_spc
   :name: fig_raw_data_spc
   ````
 	
b. Press `Select Inputs`. A selection window will appear that allows to select data that are stored on a local disk.

   ````{figure} figures/select_inputs_spc.jpg
   :alt: select_inputs_spc
   :name: fig_select_inputs_spc
   ````

c. Press `Create Datasets`. A list of datasets appears, one line for each set of science data.
	
   ````{figure} figures/create_datasets_spc.jpg
   :alt: create_datasets_spc
   :name: fig_create_datasets_spc
   ```` 

d. Choose the datasets that should be processed 
	
   ````{figure} figures/send_spc.jpg
   :alt: send_spc
   :name: fig_send_spc
   ```` 
and send them to the data reduction queue by pressing `Submit to Reduction Queue`.

## 3. Start the reduction

a. Press `Reduction Queue`.

   ````{figure} figures/processing_queue.jpg
   :alt: processing_queue
   :name: fig_processing_queue
   ```` 
	
b.  Press the `Reduce` button. The selected data will now be processed with the default parameters.
	
   ````{figure} figures/reduce_spc.jpg
   :alt: reduce_spc
   :name: fig_reduce_spc
   ```` 


Congratulations, you reduced your first data with the `EDPS` dashboard! All the reduced data are saved in the EDPS_data directory specified when executing `edps-gui` for the first time.
	