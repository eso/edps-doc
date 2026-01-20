## The EFOSC imaging data reduction flow.

The overall data flow of the EFOSC imaging pipeline is displayed in {numref}`fig_reduction_cascade_img`.

	
   ````{figure} figures/reduction_cascade_img.jpg
   :alt: reduction_cascade_img
   :name: fig_reduction_cascade_img
   ````


The reduction cascade is organized in tasks, which represent well defined steps in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The `EDPS` workflow is designed to execute the tasks that deliver
the final reduced image for each dataset. Only calibrations needed by the selected the scientific exposures are processed.

It is possible to set `EDPS` to perform the data reduction until a certain step of the reduction chain (e.g. to reduce
only standard stars, or only flat fields).
This is done by specifying the desired tasks in the field `Select reduction target` of the `Raw Data` tab.

The reduction steps are:

###  Bias subtraction

The task **bias** runs the recipe **efosc_bias** to generate a MASTER_BIAS calibration.
Typically, default recipe paraemters deliver good results. 

### Sky flats

The task **sky_flat** runs the recipe **efosc_img_sky_flat** to  reduce the sky flats and generate a MASTER_SKY_FLAT_IMG correction.
Typically, default recipe parameters deliver good results. 

### Photometric standard

The task **photometric_standard** runs the recipe **efosc_zeropoint** to process observations of standard stars and compute the photometric zeropoint.
The recipe runs sextractor to identify objects and perform aperture photometry. Typically, default recipe parameters deliver good results. 
Standard stars are used to determine the zeropoint only for filters "U#640" (using catalogue from Landolt 1992, 2007), and filters
"B#639", "V#641", "R#642", "i#705" (using catalogs from Stetson 2000). See [here](https://www.eso.org/sci/facilities/lasilla/instruments/efosc/doc/PhotStds.pdf) for more information.


### Science imaging

The task **science_imaging** runs the recipe **efosc_img_science** to reduce the raw image, and compiles a catalogue of extracted sources using sextractor.

