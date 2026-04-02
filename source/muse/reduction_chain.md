# The MUSE data reduction flow.

The overall data flow of the MUSE pipeline is displayed [here](figures/muse_cascade.jpg).

The reduction cascade is organized in tasks, which represent well-defined steps in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The EDPS workflow is designed to execute the tasks that deliver
the final reduced data cube for each dataset. It can be either the product of a single exposure, or the combination of
multiple exposures. Only calibrations needed by the selected the scientific exposures are processed.

It is possible to set EDPS to perform the data reduction until a certain step of the reduction chain (e.g. to reduce
only standar stars, or only flat fields).
This is done by specifying the desired tasks in the field **Select reduction target** of the **Raw Data** tab.

The reduction steps of the MUSE workflow are listed below. Before starting the reduction, 
the parameters of the recipes associated to each task can be configured by pressing the button ![](../edpsgui/figures/configure_dataset.jpg) close to each dataset configuration.
See [here](configure_reduction.md) for more information.

## Bias subtraction

The task **bias** reduces raw bias frames to generate a combined masterbias. It
runs the recipe **muse_bias**.

## Computation of dark current

The task **dark** runs the recipe **muse_dark**. If raw dark frames are
present, the actor processes them and creates a master dark. This product is
currently used only for instrument monitoring but not for scientific reduction. Dark
frames are taken monthly, therefore they might not represent the dark current at the time of the observations, and they
add
noise to the final products. If needed, darks can be used in the reduction cascade by setting
the workflow parameter **use_darks** to "yes" in the **science_parameters** parameter set.

## Flat field correction

The task **lamp_flat** runs the recipe **muse_ﬂat**. It processes the raw ﬂat-ﬁelds
exposures, producing a master ﬂat and a trace table.

## Wavelength correction

The task **arc** executes the recipe muse_wavecal. It processes the raw arc frames,
producing a table with the wavelength solution.

## Characterization of the line spread function.

This subworkflow is designed to run the recipe **muse_lsf**
to produce a calibration that characterize the line spread function.
In MUSE, the generation of the line spread function can be done by
processing raw arc frames (done by the task
**line_spread_function_arc**) or by dedicated calibrations (done by the
task **line_spread_function_lsf**). Alternatively, a static calibration
is used. The behavior is determined by the workflow parameter
**lsfmode**, which is described [here](../muse/configure_reduction.md#lsf).

## Monitoring calibrations, geometry and astrometry calibrations

The subworkflow "monitoring_and_long_term_calibs" contains tasks aimed at creating long term calibrations,
such as geometry calibrations  (task **geometry**,
recipe **muse_geometry**), astrometric calibrations (tasks **preprocess_astrometry**, **astrometry**,
recipes **muse_scibasic**, **muse_astrometry**). These calibrations
are distributed by the ESO archive together with the scientific data. It is anyway possible
to recreate these calibrations from raw data by setting the workflow parameters
**recompute_geometry** and **recompute_astrometry** to "yes".

Additionally, the subworkflow contains tasks aimed at monitoring the instrument performance
such as the throughput (task throughput, recipe **muse_ampl**), the instrument
linearity and gain (task linearity_and_gain, recipe **muse_lingain**). These tasks however, are executed only at the
observatory, and they are not used in the data reduction flow.

## Sky subtraction

The subworkflow **Process and combine sky** contains the tasks in charge of evaluating the sky background from dedicated
sky exposures.
They are:

- **preprocess_sky**. It runs the recipe muse_scibasic on dedicated sky exposures
- **sky**. It runs the recipe muse_create_sky to generate SKY_LINES and SKY_CONTINUUM calibrations.

Sky subtraction can also be done by evaluating the sky contribution directly on regions in the target field of view that is free from
contamination from astronomical sources.
The most important products to check, regardless of the method used, are the

- SKY_CONTINUUM. It should not contain features that are typical of astronomical objects. 
For example, if the sky region contains HII regions, the Halpha emission lines are not registered as a sky line in the 
input list of sky lines. As a consequence, it will be present in the SKY_CONTINUUM and therefore subtracted from the 
target spectrum.
- SKY_MASK. A comparison between the image field of view and the sky mask should confirm that astronomical sources are not included as sky regions.

If the SKY_MASK overlap with some source or if SKY_CONTINUUM contains astrophysical signal such as nebular emission lines, 
consider to decrease the recipe parameter **skymodel-fraction** or to provide a custom SKY_MASK in the input directory.

SKY_CONTINUUM and SKY_MASK products are available from the tasks sky (if dedicated sky observations are used) and 
object (if the sky was evaluated on the target field of view). Click on the magnifying glass
symbol close to the appropriate task, and select the tab **Output Files**. Products can be inspected via the `fv` fits 
viewer (if available).

More information on the sky background removal are given [here](../muse/configure_reduction.md#skysub).


This subworkflow contains also the tasks that consider dedicated sky exposures as self-contained science exposures and
processes and combine them as such
(tasks **preoprocess_sky_sky**, **object_sky**, **alignment_sky**, and **combine_sky**).
The strategy to combine sky exposures is the same as for the regular science exposures.

## Flux calibration

The subworkflow **response** contains the tasks to process standard stars and create the response and telluric
corrections. They are:

- **preprocess_standard**. It runs the recipe muse_scibasic on raw standard stars
- **response**. It runs the recipe muse_standard and generate STD_RESPONSE and STD_TELLURIC calibrations. To disable
  telluric correction
  on your data, set the workflow parameter **telluric_correction** to **FALSE** (
  see [here](../muse/configure_reduction.md#telluric)).

## Reduction and combination of scientific exposures

The subworkflow **Process and combine object** contains the tasks in charge of aligning and combining scientific
exposures. They are:

- **preprocess_science**. This task runs the recipe muse_scibasic on scientific exposures.
- **autocalibration_from_object_sky**. This tasks select autocalibration coefficients computed from sky exposures, if
  requested. It is not directly associated to any recipe.
  See [here](../muse/configure_reduction.md#autocalibration).
- **object**. This task runs the recipe muse_scipost to reduce a single scientific exposure.
- **source_detection**. This task runs the recipe muse_detection to detect sources in the datacube of each individual 
  exposure and create a source catalog. The source catalogs are used for the alignment of the exposures.
- **alignment**. This tasks runs the recipe muse_alignment to correct for coordinate offsets the exposures that are meant
  to be combined together (see [here](../muse/configure_reduction.md#combination). It uses sources detected in the previous step to compute the offsets.
- **object_combination**. This tasks runs the recipe muse_exp_combine and combines individual exposures to produce the
  final datacube

The most important thing to check in this step is whether or not the images to combine were properly aligned.
In the Reduction Queue tab, locate and expand the reduced dataset you want to check, and click on the magnifying glass
symbol close to the
alignment task as shown below

   ````{figure} figures/alignment_1.jpg
   :alt: alignment_1
   :name: fig_alignment_1
   ````

The following interactive plot will appear, showing the preview of the combination of the
field of views after alignment correction. In the case of good alignment, there are no duplicated sources.

   ````{figure} figures/alignment_2.jpg
   :alt: alignment_2
   :name: fig_alignment_2
   ````

In case of bad alignment, here we provide some tipps that can help in improving the alignment.
Re-configure the reduction of the dataset by pressing the ![](../edpsgui/figures/configure_dataset.jpg)  button and set
the recipe parameter in the configuration window as desired (see [here](../muse/configure_reduction.md#configuration))

- **Task source_detection**.
  - In the case of too many or too few detected sources (e.g. in crowded fields), decrease or increase the parameters **source_min** and **source_max**
    (minimum and maximum number of detections, respectively). Sometimes it helps to change the initial threshold level,
    via the parameter **start_threshold_sigma**. To prevent the threshold to go too low during iterations, one can set 
    the minimum accepted threshold via the parameter **threshold_limit**.
  - A lot of sources are detected in the edges of the field of view. This can be solved by increasing the
    parameter **bpixdistance**.
  
- **Task alignment**.
  - The maximum number of allowed stars is detected, but the alignment is not correct. This can happen
    in crowded fields, and the alignment algorithm does not find the correct matching between the sources
    detected in different frames. There are two tricks to overcome this issue. First, one could either decrease
    the number of maximum sources allowed in the detection. However, this solution is not advisable for
    mosaicing, because the number of reference sources in the overlapping regions could be too small. Second,
    if the offsets are known to be small, the user can decrease value of the first search radius and set
    the corresponding recipe parameter (**search_radii**) to, for example, 10.,4.,2.,0.8`. The first entry (10 in
    this example) forces the matching algorithm to find offsets of at most 10 arcseconds. 
  - Avoid source misidentification across exposures. To avoid to associate the wrong sources, one can specify the maximum
    difference in magnitude or in fwhm between sources in different exposures. This can be done by setting the recipe 
    parameters **threshold_on_mag** and **threshold_on_fwhm**, respectively. 


Tipp: In case of complicated alignment, it might be advisable to specify **alignment** as reduction target when creating the
  datasets in the **Raw Data** tab. In this way the reduction
  stops at this step, without wasting resources to combine the exposures. After the correct recipe parameters set has
  been found, the full reduction cascade can be triggered.

---
Go to MUSE EDPS tutorial [index](../muse/index)