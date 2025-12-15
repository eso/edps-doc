# The KMOS data reduction flow.

The overall data flow of the KMOS pipeline is displayed [here](figures/reduction_cascade.png).

The reduction cascade is organized in tasks, which represent well-defined steps in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The `EDPS` workflow is designed to execute the tasks that deliver
the final reduced data cube for each dataset. It can be either the product of a single exposure, or the combination of
multiple exposures. Only calibrations needed by the selected the scientific exposures are processed.

It is possible to set `EDPS` to perform the data reduction until a certain step of the reduction chain (e.g. to reduce
only standard stars, or only flat fields).
This is done by specifying the desired tasks in the field `Select reduction target` of the `Raw Data` tab.

The reduction steps are listed below. Before starting the reduction, the parameters of the recipes
associated to each task can be configured by clicking on ![](../edpsgui/figures/configure_dataset.jpg) close to each dataset configuration.
See [here](configure_reduction.md) for more information.

##  Process dark exposure

This step is carried out by the task **dark** using the pipeline recipe **kmos_dark**. 
It produces a MASTER_DARK and a BADPIXEL_DARK frame. Per default, only the bad pixel map from this step
is used in the reduction chain.

## Create Master Flat

Task: **lamp_flat**. Recipe: **kmos_flat**. 

This step uses exposures with the flat-field lamp to create a MASTER_FLAT, files that describe the geometry 
of the IFU slitlets on the detector (**XCAL**, **YCAL**, and **SLIT_EDGE**), and a BADPIXEL_FLAT frame.

## Wavelength Calibration

Task: **arc**. Recipe: **kmos_wave_cal**. 

This step uses exposures with the Argon and Neon arc lamps to create the wavelength calibration **LCAL**.
A useful product for verifying the wavelength calibration is DET_IMG_WAVE which contains the wavelength-calibrated
images of the input frames.

## Illumination Correction

Task: **illumination**. Recipe: **kmos_illumination**. 

This step can be run on lamp-flat or sky-flat exposures. It creates for each IFU an image
(product **ILLUM_CORR**) for correcting the
sensitivity variation within the IFU. It is recommended to execute this step on lamp flats (which is the
default workflow setup).

This step can be customized by setting the workflow parameter `use_sky_flats` to 'false' (default, recommended) or 
'true'.

## Standard star

Task: **standard**. Recipe: **kmos_std_star**. 

This step processes a telluric standard exposure and extracts a spectrum for each IFU that was used.
Products:
- **STAR_SPEC**: extracted spectrum
- **TELLURIC**: normalized telluric spectrum
- **STD_IMAGE**: reconstructed IFU field-of-view image
- **STD_MASK**: mask for extracting the standard star.

The further usage of the products is controlled via the workflow parameter `molecfit` which can have the values:
- 'standard': Atmospheric features are modeled with the molecfit algorithm using the telluric standard as
                reference. The results are used to construct the full atmospheric transmission to correct
                science exposures. A static response curve is used to correct the relative instrumental 
                efficiency with wavelength. The zeropoint computed on the observed telluric standard is used for
                absolute spectrophotometric calibration.
- 'science': Atmospheric features are modeled with the molecfit algorithm using the scientific exposure itself
                as reference. To be used only if the science exposure has a bright continuum that allows
                a proper fit to the atmospheric features. A static response curve is used to correct the
                relative instrumental efficiency with wavelength. The zeropoint computed
                on the observed telluric standard is used for absolute spectrophotometric calibration.
- 'false': The observations of the telluric standard stars are compared with a model spectrum for that star.
                This generates a combined correction that includes response curve and telluric features, which is then
                used to correct scientific exposures.



---
Go to KMOS EDPS tutorial [index](../kmos/index)