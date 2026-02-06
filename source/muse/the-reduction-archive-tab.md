## The **Reduction Archive** tab.

All the products (final and intermediate) of all reduced configuration for all datasets are saved into
the EDPS_data directory. In addition, EDPS offers the possibility to "archive" a desired reduction (e.g., the one
that gives the best results) by "exporting" only the final reduction products into another location.

Select the desired reduced configurations and press the "Archive button". This configuration disappears from the
Reduction Queue and appear in the tab "Reduction Archive".

The content of the "Reduction Archive", e.g. the list of archived reductions, can be inspected by pressing the
**Reduction Archive" tab.

   ````{figure} figures/archive.jpg
   :alt: archive
   :name: archive
   ```` 

Each configuration and its jobs can be inspected, unarchived and eventually deleted.
In order to copy the final products into a desired location, press the Export button. A window will appear
allowing 
 - to select all or just the last configuration for the selected datasets  
 - to specify a directory where to save the files. A check is done 

Press **Export** to save the files.
The types of files to copy depend on each workflow. Typically, only most important files of the 
scientific tasks are saved. Other files can be found in the EDPS_data directory.
The operation can take several minutes, depending on the sizes of the files.
The default structure is `<dataset_name>/<reduction_time_stamp>/<category>.fits`.

   ````{figure} figures/export2.jpg
   :alt: archive2
   :name: archive2
   ````  
---