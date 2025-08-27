# The MUSE data reduction flow.

The overall data flow of the MUSE pipeline is displayed [here](figures/muse_cascade.jpg).

Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The reduction steps of the MUSE workflow are:

## `bias`

This task reduces raw bias frames to generate a masterbias. It
runs the recipe `muse_bias`.

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

## `wavelength`

This task executes the recipe muse_wavecal. It processes the raw arc frames,
produc-ing a table with the wavelength solution. It requires the
products of the task `bias`, `lamp_flat` (and `dark`, if executed).

## `line_spread_function`.

This subworkflow is designed to run the recipe `muse_lsf`
to produce a calibration that characterize the line spread function.
In MUSE, the generation of the line spread function can be done by
processing raw arc frames (done by the task
`line_spread_function_arc`) or by dedicated calibrations (done by the
task `line_spread_function_lsf`). Alternatively, a static calibration
is used. The behavior is determined by the workflow parameter
`lsfmode`. Possible values are:

    "any"    Characterize the LSF from dedicated lsf raw exposures. If not
             available, use arc raw exposures. If not available, use static
             calibration from the pipeline distribution.
	     
    "lsf"    Characterize the LSF from dedicated lsf raw exposures. If not
             available, use static calibration from the pipeline distribution.
	     
    "arc"    Characterize the LSF from dedicated arc raw exposures. If not
             available, use static calibration from the pipeline distribution.
	     
    "static" Use static calibration from the pipeline distribution."

For scientific reduction, the parameter is set to "any" in the
`science_parameters` parameter set.

## `Monitoring_and_long_term_calibs`

This subworkflow  contains tasks aimed at creating long term calibrations, such as geometry calibrations  (task geometry,
recipe `muse_geometry`), astrometric calibrations (task astrometry, `recipe muse_astrometry`). These calibrations
are distributed by the ESO archive together with the scientific data. It is anyway possible
to recreate these calibrations from raw data by setting the workflow parameters
`recompute_geometry` and `recompute_astrometry` to "yes".

Additionally, the subworkflow contains tasks aimed at monitoring the instrument performance
such as the throughput (task throughput, recipe `muse_ampl`), the instrument
linearity and gain (task linearity_and_gain, recipe `muse_lingain`). These tasks however, are executed only at the
observatory, and they are not used in the data reduction flow.

---
Go to MUSE EDPS tutorial [index](../muse/index)