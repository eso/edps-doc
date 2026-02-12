
a. Press `Raw Data`.
	
   ````{figure} figures/raw_data_img.jpg
   :alt: raw_data_img
   :name: fig_raw_data_img
   ````
 	
b. Press `Select Inputs`. A selection window will appear that allows to select data that are stored on a local disk.

   ````{figure} figures/select_inputs_img.jpg
   :alt: select_inputs_img
   :name: fig_select_inputs_img
   ````


c. (Optional). Select the reduction target and the association preferences (either raw or master calibrations).

d. Press `Create Datasets`. A list of datasets appears, one line for each set of science data.
	
   ````{figure} figures/create_datasets_img.jpg
   :alt: create_datasets_img
   :name: fig_create_datasets_img
   ```` 

e. Choose the datasets that should be processed 
	
   ````{figure} figures/send_img.jpg
   :alt: send_img
   :name: fig_send_img
   ```` 
and send them to the data reduction queue by pressing `Submit to Reduction Queue`.

### 3. Start the reduction

a. Press `Reduction Queue`.

   ````{figure} figures/processing_queue.jpg
   :alt: processing_queue
   :name: fig_processing_queue
   ```` 
	
b.  Press the `Reduce` button. The selected data will now be processed with the default parameters.
	
   ````{figure} figures/reduce_img.jpg
   :alt: reduce_img
   :name: fig_reduce_img
   ```` 


Congratulations, you reduced your first data with the `EDPS` dashboard! All the reduced data are saved in the EDPS_data directory specified when executing `edps-gui` for the first time.
	