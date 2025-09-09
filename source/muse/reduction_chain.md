# The MUSE data reduction flow.

The overall data flow of the MUSE pipeline is displayed [here](figures/muse_cascade.jpg).

The reduction cascade is organized in tasks, which represent a well defined step in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The `EDPS` workflow is designed to execute the tasks that deliver
the final reduced data cube for each dataset. It can be either the product of a single exposure, or the combination of
multiple exposures. Only calibrations needed by the selected the scientific exposures are processed.

It is possible to set `EDPS` to perform the data reduction until a certain step of the reduction chain (e.g. to reduce
only standar stars, or only flat fields).
This is done by specifying the desired tasks in the field `Select reduction target` of the `Raw Data` tab.

The reduction steps of the MUSE workflow are:

##  Bias subtraction

The task `bias` reduces raw bias frames to generate a combined masterbias. It
runs the recipe `muse_bias`.

**Apply the same format below**

## `dark`

This task runs the recipe `muse_dark`. If raw dark frames are
present, the actor processes them and creates a master dark. It
requires the products of task `bias` as inputs. Important: the use of
dark frames is not recommended for the scientific reduction; dark
frames are taken on a monthly base (therefore they do not represent in
detail the dark current at the time of the observations) and they add
noise to the final products. Currently, this task is not included in
the scientific reduction. To include it, set the workflow parameter
`use_darks` to `yes` in the `science_parameters` parameter set.

## `lamp_flat`

This task executes the recipe `muse_ﬂat`. It processes the raw ﬂat-ﬁelds
exposures, producing a master ﬂat and a trace table. It requires the
products of the task `bias` (and, optionally, of the task `dark`, if
executed).

## `wavelength` (task)

This task executes the recipe muse_wavecal. It processes the raw arc frames,
produc-ing a table with the wavelength solution. It requires the
products of the task `bias`, `lamp_flat` (and `dark`, if executed).

## `line_spread_function` (subworkflow)

This subworkflow is designed to run the recipe `muse_lsf`
to produce a calibration that characterize the line spread function.
In MUSE, the generation of the line spread function can be done by
processing raw arc frames (done by the task
`line_spread_function_arc`) or by dedicated calibrations (done by the
task `line_spread_function_lsf`). Alternatively, a static calibration
is used. The behavior is determined by the workflow parameter
`lsfmode`, which is described [here](../muse/configure_reduction.md#lsf).

## `Monitoring_and_long_term_calibs`, `Astrometry` (subworkflows)

This subworkflow contains tasks aimed at creating long term calibrations, such as geometry calibrations  (
task `geometry`,
recipe `muse_geometry`), astrometric calibrations (tasks `preprocess_astrometry`, `astrometry`,
recipes `muse_scibasic`, `muse_astrometry`). These calibrations
are distributed by the ESO archive together with the scientific data. It is anyway possible
to recreate these calibrations from raw data by setting the workflow parameters
`recompute_geometry` and `recompute_astrometry` to "yes".

Additionally, the subworkflow contains tasks aimed at monitoring the instrument performance
such as the throughput (task throughput, recipe `muse_ampl`), the instrument
linearity and gain (task linearity_and_gain, recipe `muse_lingain`). These tasks however, are executed only at the
observatory, and they are not used in the data reduction flow.

## `Process and combine sky` (subworkflow)

This subworkflow contains the tasks in charge of evaluating the sky background from dedicated sky exposures.
They are

- `preprocess_sky`. It runs the recipe muse_scibasic on dedicated sky exposures
- `sky`. It runs the recipe muse_create_sky to generate SKY_LINES and SKY_CONTINUUM calibrations.

The strategy to compute the sky background using dedicated sky exposures is
described [here](../muse/configure_reduction.md#skysub).

This subworkflow contains also the tasks that consider dedicated sky exposures as self-contained science exposures and
processes and combine them as such
(tasks `preoprocess_sky_sky`, `object_sky`, `alignment_sky`, and `combine_sky`).
The strategy to combine sky exposures is the same as for the regular science exposures.

## `Response` (subworkflow)

This subworkflow contains the tasks to process standard stars and create the response and telluric corrections. They are:
- `preprocess_standard`. It runs the recipe muse_scibasic on raw standard stars
- `response`. It runs the recipe muse_standard and generate STD_RESPONSE and STD_TELLURIC calibrations. To disable telluric correction
on your data, set the workflow parameter `telluric_correction` to `FALSE` (see [here](../muse/configure_reduction.md#telluric)).



## `Process and combine object` (subworkflow)

This subworkflow contains the tasks in charge of aligning and combining scientific exposures. They are:

- `preprocess_science`. This task runs the recipe muse_scibasic on scientific exposures.
- `autocalibration_from_object_sky`. This tasks select autocalibration coefficients computed from sky exposures, if
  requested. It is not directly associated to any recipe.
  See [here](../muse/configure_reduction.md#autocalibration).
- `object`. This task runs the recipe muse_scipost to reduce a single scientific exposure.
- `alignment`. This tasks runs the recipe muse_exp_align to correct for coordinate offsets the exposures that are meant
  to be combined together (see [here](../muse/configure_reduction.md#combination)
- `object_combination`. This tasks runs the recipe muse_exp_combine and combines individual exposures to produce the
  final datacube

---
Go to MUSE EDPS tutorial [index](../muse/index)