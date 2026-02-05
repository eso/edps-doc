# The KMOS data reduction flow

The overall data flow of the KMOS pipeline is displayed [here](figures/reduction_cascade.jpg).

The reduction cascade is organized in tasks, which represent well-defined steps in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The `EDPS` workflow is designed to execute the tasks that deliver the final reduced data cube for each dataset. 
Only calibrations needed by the selected scientific exposures are processed.

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

The further usage of the products depends on the workflow parameters `telluric_correction` and `molecfit`.
The parameter `telluric_correcton` can have the values:
- 'true': The science spectra are corrected for telluric absorption using the strategy which is defined by the parameter `molecfit`. This is the default.
- 'false': The science spectra are not corrected for telluric absorption.

The workflow parameter `molecfit` can have the values:
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

## Response

This step involves either the task **response** or the task **telluric_and_response**. Both use the pipeline recipe
**kmos_gen_telluric**.

If the workflow parameter `molecfit` is set to 'false' (and `telluric_correction` is 'true'), 
then the task **telluric_and_response** is used. 
The telluric spectrum as calculated from the **standard** task and the response are passed to the science reduction.
For the other values of `molecfit` or if `telluric_correction` is 'false', only the response is used.

## Science reduction

Task: **object**. Recipe: **kmos_sci_red**.

In this step, the basic data reduction of the science data is executed. The data from the IFUs are extracted, 
calibrated, and reconstructed into data cubes. If the workflow parameter `molecfit` is set to 'false', then the 
products are flux-calibrated and corrected for telluric absorption. Otherwise, the products are only
flux-calibrated. The telluric correction is then executed in the following workflow steps.

Main products:
- **SCI_RECONSTRUCTED**: one file for each exposure that contains IFUs on objects (no file for pure sky exposures). Each file has 24 extensions with data cubes.
- **SCI_RECONSTRUCTED_COLL**: files with 24 extensions containing the reconstructed field-of-view images for each IFU.

## Telluric model

This step either involves the tasks **model_on_standard** and **transmission_on_standard** 
or the tasks **model_on_science** and **transmission_on_science**. The tasks are encapsulated in the
sub workflows telluric_on_standard and telluric_on science, respectively.
The pipeline recipes **kmos_molecfit_model** and **kmos_molecfit_calctrans** are used.

If the workflow parameter `molecfit` is set to 'standard', then 
the atmospheric model is fit to the extracted spectra from the **reponse** task. 
With the parameter set to `science`, the fit is executed on the science data themselves.
In both cases, the actual transmission curve is calculated using the model and the information from the science data.

## Telluric correction

Task: **telluric_correction**. Recipe: **kmos_molecfit_correct**.

In this step, the science data are corrected for telluric absorption using the transmission from the previous step.

## Object combination

Task: **object_combination**. Recipe: **kmos_combine**.

The different exposures for each object are combined. The final products are:
- One combined data cube for each object in the dataset, coming in two different formats as
  `COMBINED_CUBE` and `IDP_COMBINED_CUBE`. Both products have the same data content. 
  The latter file has the needed metadata information for ingestion into the ESO archive.
- A field-of-view image `COMBINED_IMAGE` and an exposure mask image `EXP_MASK` for each object.

## Cubes combination

Task: **cubes_combination**. Recipe: **kmos_combine**.

If data have already been processed then the resulting cubes can be combined
for each object. This is useful for combining observations of the same targets which have been measured
using different Observation Blocks.

---
Go to KMOS EDPS tutorial [index](../kmos/index)