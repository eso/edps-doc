Almost all processing tasks can display the input raw frames and the products in the so called "quality plots".
By default, only the plots that refer to the products and the target task are generated.
If one is interested in the generation of other quality reports, change the "Graphical reports" configuration  in the 
configuration editor as the figure below.

   ````{figure} ../common/figures/select_reports.jpg
   :alt: reports
   :name: fig_reports
   ```` 
Quality reports can be inspected from the `Reduction Queue` window.
Those associated for the main product can be inspected by pressing the magnifying glass symbol at the right side of each dataset.
To inspect those associated to each individual job (if created), 

 - Expand the desired dataset by pressing the black arrow on its left. The list of jobs will appear with the associated status (COMPLETED, RUNNING, PENDING)
 - Press the  magnifying glass symbol at the right side of the job you want to inspect. Only plots for completed jobs can be inspected.


   ````{figure} figures/show_reports.jpg
   :alt: reports
   :name: show_reports
   ```` 