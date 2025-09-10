# Customizing the data reduction  <a name="configuration"></a>

## Selection of most appropriate calibrations

```{include} ../common/appropriate_calibrations.md
```


## Configuration of parameters
The data reduction of each dataset can be configured according to the scientific needs. In order to configure a
reduction, go in the `Processing Queue` tab, which lists the datasets that are listed for reduction,
and press the button ![](../edpsgui/figures/configure_dataset.jpg) (see {numref}`fig-reduction_configuration_muse_0`).

```{figure} figures/reduction_configuration_muse_0.jpg
:alt: reduction_configuration_muse_0
:name: fig-reduction_configuration_muse_0
:figclass: left-caption

How to open the dataset configuration menu to customize data reduction.
```

The configuration window appears (see
{numref}`fig-reduction_configuration_muse_1` and {numref}`fig-reduction_configuration_muse_2`)
It is possible to configure `workflow parameters`, that specify the strategy of the data reduction, as well as the
`recipe parameters` associated to each individual task. Predefined sets are configured, for normal scientific reduction
the default set `science_parameters` can be used.
The main data reduction steps for which one can modify the predefined strategy by editing the workflow parameters are:

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

## Parametrization of the Line Spread Function

The `MUSE` pipeline uses a model of the Line Spread Function (LSF) to model emission sky lines for the sky subtraction.
An accurate knowledge of the LSF is crucial for a good removal of sky lines. The strategy for computing the LSF is
set by the workflow parameter **`lsfmode`**.
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

**When the defaults have to be changed?** T.B.D.

 ---
Go to [top](#configuration)

<a name="skysub"> </a>

## Sky subtraction

**Things to consider, when to change defaults. If this happens, do this, if that happens do that**

A crucial aspect of the `MUSE` data reduction is the sky subtraction. The workflow supports several strategies, which
are determined by the value of the workflow parameter **`skysubtraction`**. Possible values are:

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

The following recipe parameters of the task `sky`, also have an impact on the quality of the sky subtraction. They can
be accessed by selecting the corresponding task from the `Recipe parameters` section of the configuration window (
{numref}`fig-reduction_configuration_muse_2`).

- `fraction`. As `skymodel-fraction`, but it is applied to the dedicated sky exposure.
- `ignore`. As `skymodel_ignore`, but it is applied to the dedicated sky exposure.

*Important note*: The `MUSE` `EDPS` workflow automatically sets `skymode-fraction` and `skymodel-ignore` according to
the
following schema.

- `skymodel-ignore=0.05` always.

- If no dedicated sky exposures are present: `skymodel-fraction=0.4`.

- If `skysubtraction=model` (or `skysubtraction=auto` but no dedicated sky exposures are
  present): `skymodel-fraction=0.75` (i.e. the majority of the field of view is supposed to be free from object
  contamination).

- For all other cases, `skymodel-fraction=0.2` (only 20% of the field of view is supposed to be free from object
  contamination).

To override these values, specify the values in the `Override value` field of the configuration window shown in
{numref}`fig-reduction_configuration_muse_2`.

### Creation of a SKY_MASK

It is possible to specify a sky mask, e.g. a fits file per exposure that specifies the regions in the field of view to
consider as pure sky.
The best way for doing it is to start the reduction without sky mask and specify the targets `object` and `sky`. The
product folder will contain the SKY_MASK automatically computed by the
pipeline. Edit them with your favourite fits editor and copy them in the input directory. Restart the reduction. EDPS
will associate to each target and dedicated sky frame the SKY_MASK with the same mjd-obs (so, make sure you have the
correct mjd-obs correspondence).
To use the entire SKY_MASK set `skymodel_fraction` and `fraction` to 1, and `skymodel_ignore` and `ignore` to 0 in the
desired actor (e.g.: `object` for regular science frames, `sky` for the dedicated sky exposures), of the configuration
panel shown in {numref}`fig-reduction_configuration_muse_2`.


 ---
Go to [top](#configuration)

## Combination of exposures <a name="combination"> </a>

The `MUSE` pipeline allows to align and combine scientific exposures belonging to the same target.
It is possible to specify the method how to identify the exposures that are meant to be combined, this is regulated by
the workflow parameters
`combine_science`, `max_diameter_WFM`, `max_separation_WFM`, `max_diameter_NFM`, `max_separation_NFM`.

`EDPS` first groups the scientific exposures present in the input directories by the header keyword specified by the
workflow parameter
`combine_science`. Possible values are:

- `obs.targ.name` group all those exposures that have the same target name and instrumental setup.
- `obs.id` group all those exposures that have the same OB identification and instrumental setup.
- `tpl.start` group all those exposures that have the same template start and instrumental setup.
- `exptime` group all those exposures that have the same exposure time and instrumental setup.
- `night` group all exposures of the same night and the same instrumental setup.
- `instrume` group all exposures of the same instrumental setup.

Then, within each group, `EDPS` creates sub-groups on the basis of their sky coordinates. Exposures in the same
sub-group are aligned and combined together.
The keywords that regulates how exposures in each group are clustered by sky position are:
`max_diameter_WFM` and `max_separation_WFM`, for the Wide Field Mode, and `max_diameter_WFM` and `max_separation_WFM`,
for the Narrow Field Mode.

- `max_diameter_WFM`. It specifies the maximum projected diameter of the sub-group of exposures to combine, in degrees.
  If an exposure would make the sub-group bigger than this value, it is not included in this sub-group.
- `max_separation_WFM`. Is specifies the maximum separation on the sky from an exposure and a sub-group, in degrees. If
  the exposure is more distant than this threshold, it is not included in the sub-group. If it is closer, and if its
  inclusion does not make the sub-group size to exceed `max_diameter_WFM`, then it is added to the sub-group.

The default values ensures that exposures with an overlap of about 1/4 of the field of view are grouped together, and
that the resulting mosaic does not exceed 3 times the MUSE field of view.

Note: To process individual exposures without combining them together, specify the reduction target `object` and
remove `object_combination` when creating the datasets in the `Raw Data` tab.

## Sky flats

By default, the `MUSE` pipeline uses sky flats exposures to account for large scale illumination variations within the
field of view.
The workflow parameter `use_skyflats` specifies whether or not to use skyflats in the data reduction cascade. Possible
values are:

- `no`. Do not use sky flats in the reduction cascade. Set the parameter to 'no' only if the skyflats are not
  available or if they have bad quality.

- `yes` (default). Use sky flats in the reduction cascade. This option requires the skyflats to be present. It is the
  recommended strategy."

 ---
Go to [top](#configuration)

## Autocalibration <a name="autocalibration"> </a>

The `MUSE` pipeline has an algorithm (autocalibration) designed to minimize the non-homogeneities in flux calibration
between different IFUs and slices. It works under the assumption that
the vaste majority of the field of view is dominated by the background sky (e.g., only few nearly point-like sources are
present in the field) and that the sky bakground is constant within the field of view.

The workflow supports several autocalibration strategies, that are defined by the workflow parameter `autocalibration`.
Possible values are:

- `none` Do not apply self-calibration (default).

- `deepfield` Apply the self-calibration on the target field itself, under the condition that the sky background
  is constant and each IFU/slice is dominated by sky background (exposures of small and sparse objects).

- `closest_sky` It applies the self-calibration algorithm to a sky exposure of the same night and instrument setup.
  The self-calibration coefficients determined on the sky exposure are then applied to the scientific
  target exposure. If not available, the dataset is reduced without autocalibration. Results are often sub-optima, hence
  inspect the resulting field of view to assess the outcome.

- `user` It uses the closest in time user-provided calibration table (from the same night). If not
  available among the input data directory, the dataset is incomplete.

 ---
Go to [top](#configuration)

## Telluric correction <a name="telluric"> </a>

The MUSE pipeline derives the atmospheric transmission (category: `STD_TELLURIC`) from the standard star. The correction
is then applied to the entire datacube. This is enabled by default. To avoid telluric correction,
set the workflow parameter `telluric_correction` to `FALSE`.

 ---
Go to [top](#configuration)

## Wavelength range

It is possible to specify the wavelength range of the output by setting the parameters `wavelength_min` (default 4000
angstrom) and - `wavelength_max` (default 10000 angstrom). It could be convenient to specify a shorter wavelength range
to speed up the reduction process, e.g. by concentrating only on the spectra features of scientific interest.

 ---
Go to [top](#configuration)

## Geometric and astrometric calibrations.

By default, the ESO archive provides the closer in time geometric and astrometric calibrations. If one wants to
reprocess them, it has to download the corresponding raw calibrations (`dpr.type` = `WAVE,MASK` and `ASTROMETRY`,
respectively) from the archive and set
the workflow parameters  `recompute_geometry`: "yes" and `recompute_astrometry`: "yes".
Note that the computation of geometry calibration is expensive in terms of computation and RAM.

 ---
Go to [top](#configuration)

## Removal of DARK currents

The DARK current in MUSE detector is very low. Dark calibrations are taken as part of the instrument monitoring and
calibration plan, but it is not advisable to process and remove a master dark from the scientific data, as it increase
the noise in the product.
Therefore, darks are not processed for scientific reduction. To enable and use dark calibrations for scientic reduction,
set the workflow parameter
`use_darks`: "yes"

 ---
Go to [top](#configuration)

 ---
Go to MUSE EDPS tutorial [index](../muse/index)