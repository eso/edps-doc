# Datareduction configuration  <a name="configuration"></a>

The data reduction of each dataset can be configured according to the scientific needs. In order to configure a
reduction,
go in the `Processing Queue` tab, which lists the datasets that are listed for reduction,
and press the button ![](../edpsgui/figures/configure_dataset.jpg). The configuration window appears (see
{numref}`fig-reduction_configuration_muse_1` and {numref}`fig-reduction_configuration_muse_2`)
It is possible to configure `workflow parameters`, that specify the strategy of the data reduction, as well as the
`recipe parameters` associated to each individual task. Predefined sets are configured, for normal scientific reduction
the default set `science_parameters` can be used.
The main data reduction strategies that can be configured via `workflow parameters` are:

```{figure} figures/reduction_configuration_muse_1.jpg
:alt: reduction_configuration_muse_1
:name: fig-reduction_configuration_muse_1
:figclass: left-caption

The top part of the reduction configuration window of the MUSE workflow, where the workflow parameters can be configured.

```

```{figure} figures/reduction_configuration_muse_2.jpg
:alt: reduction_configuration_muse_2
:name: fig-reduction_configuration_muse_2
:figclass: left-caption

The lower part of the reduction configuration window of the MUSE workflow, where the recipe parameters per each task can be configured.

```

<a name="lsf"> </a>
## **`lsfmode`**: parametrization of the Line Spread Function

The `MUSE` pipeline uses a model of the Line Spread Function (LSF) to model emission sky lines for the sky subtraction.
An accurate knowledge of the LSF is crucial for a good removal of sky lines. The strategy for computing the LSF is
regulated by the workflow parameter **`lsfmode`**.
The best results are generally obtained by setting it to `arc`, which
uses the arc lines of the wavelength calibrations to model the line spread function. Possible values of **`lsfmode`**
are:

- `any`  Characterize the LSF from dedicated lsf raw exposures. If not
  available, use arc raw exposures. If not available, use static
  calibration from the pipeline distribution.

- `lsf`  Characterize the LSF from dedicated lsf raw exposures. If not
  available, use static calibration from the pipeline distribution.

- `arc`  Characterize the LSF from dedicated arc raw exposures. If not
  available, use static calibration from the pipeline distribution.

- `static` Use static calibration from the pipeline distribution.

<a name="skysub"> </a>
## **`skysubtraction`**: sky subtraction.
A crucial aspect of the `MUSE` data reduction is the sky subtraction. The workflow supports several strategies, which are determined by the value of the workflow parameter **`skysubtraction`**. Possible values are:

- `model`. It uses fluxes indicated in an input SKY_LINES table (either static calibration, or coming from a dedicated
  sky
  exposures) as starting estimates, but re-fits them on the global sky spectrum created from the science exposure. If a
  SKY_CONTINUUM is computed
  from dedicated sky exposures, it is directly subtracted from the data. Otherwise, the sky continuum is computed
  directly from teh science exposure. The portion
  of the field of view of the science exposures it uses to fit the sky lines and compute the continuum is regulated by
  the recipe parameters
  `skymodel_fraction` and `skymodel_ignore`. Select this option if no dedicated sky exposures are available (sky lines
  and sky continuum will be computed on the target field of view), or if dedicated sky exposures are present and enough
  empty sky regions are
  available in the target field of view (sky continumm is
  computed on dedicated sky exposures, sky lines are re-fitted on the target field of view). To discard completely
  dedicated sky exposures, remove them from the pool of input data.

- `subtract-model`. It uses sky emission lines and sky continuum determined on the field of view of dedicated sky
  exposures. Select this option
  if dedicated sky exposures are present and the target field of view does not contain enough empty portions to ensure a
  reliable fit of the sky emission lines.

- `auto`. It automatically set the parameter **`skysubtraction`** to `model` if no dedicated sky exposures are present
  in the dataset, and to `subtract-model` if dedicated sky exposures are present.


- `simple`. It creates a sky spectrum from the science data, and directly subtracts it, without taking
  the LSF into account (LSF_PROFILE and input SKY files are ignored).

- `none`. It does not perform a sky subtraction.

The following recipe parameters of the tasks `object` and `object_sky`, also have an impact on the quality of the sky
subtraction. They can be accessed by selecting the corresponding task from the `Recipe parameters` section of the
configuration window.

- `skymodel_fraction`. It specifies the fraction of the field of view (or of the SKY_MASK, if present among the inputs)
  to be used when calculating the sky continuum and sky emission lines.
- `skymodel_ignore`. It specifies the fraction of the field of view (or of the SKY_MASK, if present among the inputs) to
  exclude when calculating the sky continuum and sky emission lines.
  These parameters are applied to the histogram of the flux values of the pixels. For example, if `skymodel_ignore=0.05`
  and `skymodel_fraction=0.8`, then the brighter 80% of the pixels, with the exclusion of the fainter 5%, are included
  in the computation. They refer to the full field of view of the input frame, or only to the part
  specified by the input sky mask.
-

The following recipe parameters of the task `sky`, also have an impact on the quality of the sky subtraction. They can
be accessed by selecting the corresponding task from the `Recipe parameters` section of the configuration window.

- `fraction`. As `skymodel-fraction`, but it is applied to the dedicated sky exposure.
- `ignore`. As `skymodel_ignore`, but it is applied to the dedicated sky exposure.

*Important note*: The `MUSE` `EDPS` workflow automatically sets skymode-fraction and skymodel-ignore according to the
following schema.

- `skymodel-ignore=0.05` always.

- If no dedicated sky exposures are present: `skymodel-fraction=0.4`.

- If `skysubtraction=model` (or `skysubtraction=auto` but no dedicated sky exposures are
  present): `skymodel-fraction=0.75` (i.e. the majority of the field of view is supposed to be free from object
  contamination).

- For all other cases, `skymodel-fraction=0.2` (only 20% of the field of view is supposed to be free from object
  contamination).

To override these values, specify the values in the `Override value` field of the configuration window.

### Creation of a SKY_MASK

It is possible to specify a sky mask, e.g. a fits file per exposure that specifies the regions in the field of view to
consider as pure sky.
The best way for doing it is to start the reduction without sky mask and specify the targets `object` and `sky`. The
product folder will contain the SKY_MASK automatically computed by the
pipeline. Edit them with your favourite fits editor and copy them in the input directory. Restart the reduction. EDPS
will associate to each target and dedicated sky frame the SKY_MASK with the same mjd-obs (so, make sure you have the
correct mjd-obs correspondence).
To use the entire SKY_MASK set `skymodel_fraction` and `fraction` to 1, and `skymodel_ignore` and `ignore` to 0.

 ---
Go to MUSE EDPS tutorial [index](../muse/index)