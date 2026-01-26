# Overview of all the data reduction configuration options  <a name="configuration"></a>

## Selection of most appropriate calibrations

```{include} ../common/appropriate_calibrations.md
```

## Quality reports
```{include} ../common/quality_plots.md
```

## Configuration of parameters
```{include} ../common/configure_reduction.md
```

## Wavelength calibration <a name="wavelength_calibration"> </a>

The interactive window for the wavelength calibration step (task **arc**) shows the 
reconstructed arc frames for each of
the three detectors at one of the six rotator position angles. 
Other rotator angles (either 0, 60, 120, 180, 240, or 300 degrees) can be chosen with the
`Select Angle` menu. The
output file with the reconstructed arc frames has 18 extensions (3 extensions per detector, times 6 angles).
Exposures at different angles are taken to account for the instrument flexures. When applying the wavelength
correction to a dataset, the KMOS pipeline automatically selects the calibration with the closest angle. 


The KMOS wavelength calibration uses Argon and Neon arc line. 
There is normally no need to fine tune the wavelength calibration result. 
Since the Argon lines are less numerous and
less bright than the Neon ones, the fit to the line positions is dominated by the Neon lines and
the average offset of the Argon lines is larger than the ones of the Neon lines. This can be checked with the
QC ARC AR POS MEAN and QC ARC NE POS MEAN header keywords in the product file extensions. Their values are
less than the uncertainties. The effect could be mitigated by increasing the recipe parameter `order` to 7.
The parameter determines the order of the fit polynomial.
With its default value of 0, the applied order is 6 for the H, K, and YJ grisms, 4 for the IZ grism, and
5 for the HK grism. 

 ---
Go to [top](#configuration)


## Science reduction: level correction <a name="level_correction"> </a>

Science data can contain extra counts due to the electronics and other sources. These counts differ from one
detector read-out channel to another and can vary intensity across the detector. 
The KMOS pipeline has two main strategies for removing this extra level (“level correction”).

The first strategy (overscan) evaluates the extra counts on pre- and over- scan regions; 
it evaluates the correction for each of the 32 read-out channels independently and for even and odd pixels.

The second strategy (intra slices), uses the non illuminated portion of the detector located in between the various
slices and IFUs to evaluate the extra light and remove it. This strategy is to be used only for very faint sources,
otherwise the cross-talk effect contaminates the intra-slices region and the pipeline over-correct the data.

These strategies can be selected by setting the `lcmethod` parameter in the recipe **kmos_sci_red** 
(task **object**).

The values for `lcmethod` are:
- OSCAN It applies the overscan method. This is the default value.
- SLICES_MEAN. It applies the intra-slices method. The input file is divided into a grid of 32×16 windows,
each of them 64 × 128 pixels wide. The mean of the non illuminated portions (i.e., intra-slices pixels) of
the detector within each window is subtracted from the data. Bad pixels are masked. Intra slice pixels and
bad pixels are identified with the calibrations BADPIXEL_DARK and LCAL produced by the workflow.
- SLICES_MEDIAN. Same as SLICES_MEAN but the median is computed instead of the average.
- NONE. No correction is done.

In general, the default strategy OSCAN is recommended. 
Intra-slice correction can improve a bit the overall background
subtraction (but not the emission sky lines) and it is recommended only for very faint sources. Bright
sources generate cross-talk between slices. The intra-slice area is then contaminated by this source of light
in the target exposures (which will be over-corrected) and not in the sky exposures. This will result in an over
subtraction of the sky continuum for the slices that are more affected by the cross-talk.

 ---
Go to [top](#configuration)


## Science reduction: optimizing sky removal with recipe parameters <a name="sky_removal"> </a>

The **kmos_sci_red** recipe triggered by the **object** task automatically assigns a sky IFU to an
object IFU. The adopted criteria is to use the same IFU as the object, which is closest in time. To override the
automatic assignment, please refer to the next section.

Once the Object / Sky pair is identified, the recipe proceeds to remove the sky from the corresponding object
IFU. To suppress sky subtraction, set `no_subtract` to true and `sky_tweak` to false. This setup will
create also reconstructed sky cubes.

There are several steps involved in the sky subtraction. First, the object cube is reconstructed and aligned to a
reference spectrum with OH emission lines. This includes a 2nd polynomial order fit to compensate non-optimal
wavelength calibration. The alignment is triggered if the dataset contains a OH_LINES reference file, which
is the default case and the recommended strategy. To remove this step, deselect the OH_LINES reference file
from the dataset.

Then the user has the option to re-scale the intensities of the sky emission lines measured on the sky cube
to match those observed in the science cube. This option exploits the sky tweaking algorithm described in
Davies et al. 2007, MNRAS, 375, 1099, that defines groups of lines with the same scaling factor. This op-
tion is triggered setting `sky_tweak` to true (default). In some (rare) cases, switching off the `skytweak`
method gives better results than the default configuration. Note that you cannot trigger this option and set
`no_subtract` to true.

The sky lines scaling factors computed via the sky tweaking algorithm can be not correct if there is still a residual
mismatch in wavelength between the object spectrum and the science spectrum. This scenario can be identified
by the presence of P-Cygni profiles in the residual sky lines in the reconstructed datacubes. In some cases,
it is possible to correct for this wavelength mismatch by applying an additional re-alignment of the skylines
measured in the sky and object cubes. This can be done by setting the parameter `stretch` to true.
The algorithm detects bright emission lines from 1D sky spectra extracted from the object and the sky datacubes,
identifies the same lines in both spectra, computes the difference in position, and computes a polynomial 
correction to minimize these differences. This correcting polynomial is then applied to the sky cube only in order
to align it better to the object cube.

Note that the alignment of the sky cube to the OH_LINES reference spectrum is still done before applying the
stretching algorithm, unless `skip_sky_oh_align` is set to true. Skipping the sky alignment reduces
the number of interpolations to reconstruct the sky datacube. However, in case of large offsets, it might still
be useful to have this initial alignment before applying the stretching algorithm. Note that 
`skip_sky_oh_align` = true has an effect only if the stretching algorithm is activated.

The outcome of the stretching algorithm needs to be evaluated with care. It is suggested to use high-order
polynomials (e.g. between 4 and 14) by setting the `stretch_degree` parameter accordingly (the default
degree is 8). The use of high-order polynomials helps in correcting for small wavelength mismatches in most of
the spectral range. It can, however, introduce spurious effects at the edges of the wavelength range.

 ---
Go to [top](#configuration)

## Science reduction: object/sky association for sky subtraction <a name="object_sky"> </a>

The **kmos_sci_red** recipe parameter `obj_sky_table` allows to specify the path to an ASCII file that
associates every object exposure with its corresponding sky, overriding the automatic association done by the
recipe itself. The suggested procedure to for this is:
1. Run the workflow on only one data set.
2. Locate the file obj_sky_table.txt produced by the **object** task (kmos_sci_red recipe). It is located in the same directory as the output products for the object task. This can be checked by clicking on the "Output files" tab in the "Quality reports" window.
3. Copy it into a safe place and rename it in a way that makes it easy to associate it with the current dataset.
4. Change it according to the needs (an example is provided below). Each time the file is edited, it should
be saved with a new name, otherwise a new reduction will not be triggered.
5. Enter the edited file name with its full path to the `obj_sky_table` field in the interactive window.
6. Reduce the data set again.

The ASCII file that associates every object exposure with its corresponding sky looks like the following (the
caption lines are not shown here, for sake of clarity).

    # [caption lines skipped]
    Object/sky associations of frames tagged as: SCIENCE
    index: filename:
    # 0: /scratch/data/edps/kmos/2013-06-30/KMOS.2013-06-30T23:48:06.049.fits
    # 1: /scratch/data/edps/kmos/2013-06-30/KMOS.2013-06-30T23:53:23.571.fits
    # 2: /scratch/data/edps/kmos/2013-06-30/KMOS.2013-06-30T23:59:09.586.fits
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    IFU          1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18  19  20 21 22 23 24
                -----------------------------------------------------------------------------
    frame #  0:  /scratch/data/edps/kmos/2013-06-30/KMOS.2013-06-30T23:48:06.049.fits
          type:  O  O  O  O  O  O  O  O  O  O  O  O  .  .  O  .  O  O   O   O  O  O  O  O
      sky in #:  1  1  1  1  1  1  1  1  1  1  1  1  .  .  1  .  1  1   1   1  1  1  1  1
    frame # 2:   /scratch/data/edps/kmos/2013-06-30/KMOS.2013-06-30T23:59:09.586.fits
          type:  O  O  O  O  O  O  O  O  O  O  O  O  .  .  O  .  O  O   O   O  O  O  O  O
      sky in #:  1  1  1  1  1  1  1  1  1  1  1  1  .  .  1  .  1  1  1/20 1  1  1  1  1
    -----------------------------------------------------------------------------------------

The IFUs pointing to Object and Sky are identified with the letters “O” and “S”, respectively. Inactive arms
are identified with a dot “.”. For each frame and IFU containing an object, the corresponding frame and IFU
containing the sky is displayed in the line below. If the sky location is described with a single number, e.g. N
(N is an integer), then the sky to be used is on the exposure with index N , on the same IFU as the object.
If the sky location is described in the format N/M (N and M integers, with 1 < M < 24), then the sky to be
used is located in the exposure with index N and IFU M.

In the example shown above, in the object frame KMOS.2013-06-30T23:48:06.049.fits (that has index 0) each
n-th IFU has the corresponding sky cube in the same n-th IFU of the frame with index 1 
(KMOS.2013-06-30T23:53:23.571.fits).
The same is true for the object frame KMOS.2013-06-30T23:59:09.586.fits (that has index 2), 
except for IFU 19. The corresponding sky has to be found in the frame with index 1, at ifu 20.

 ---
Go to [top](#configuration)

## Cubes combination <a name="cubes_combination"> </a>

The tasks **object_combination** and **object_combination_molecfit** work on data from a single execution
of an Observation Block. In order to create combined data cubes from several observations, the task
**cubes_combination** can be used.

The task **cubes_combination** requires as input products of type **SINGLE_CUBES** that have been created with
previous executions of the task **telluric_correction**. Each file contains the data cube for a single target. 
The task allows to combine the different data cubes for the same target. 

The suggested procedure is:
1. Copy the **SINGLE_CUBES** files that shall be combined into an (empty) directory.
2. Select this directory as input in the "Raw data" section of the GUI and create a dataset for them. This data set should have the target **cubes_combination**.
3. Start the reduction of this data set in the "Reduction Queue" section.

For each target in the input data set, a product of category **COMBINED_CUBE**, **COMBINED_IMAGE**, 
**IDP_COMBINED_CUBE**, and **EXP_MASK**, respectively, is then created.

 ---
Go to [top](#configuration)

## Telluric correction <a name="telluric_correction"> </a>

The KMOS workflow allows to select between three strategies in order to correct the observations for atmospheric 
transition. These are controlled via the workflow parameter `molecfit` which can have the values:
1. 'standard': Atmospheric features are modeled with the molecfit algorithm using the telluric standard as
                reference. The results are used to construct the full atmospheric transmission to correct
                science exposures. A static response curve is used to correct the relative instrumental 
                efficiency with wavelength. The zeropoint computed on the observed telluric standard is used for
                absolute spectrophotometric calibration.
2. 'science': Atmospheric features are modeled with the molecfit algorithm using the scientific exposure itself
                as reference. To be used only if the science exposure has a bright continuum that allows
                a proper fit to the atmospheric features. A static response curve is used to correct the
                relative instrumental efficiency with wavelength. The zeropoint computed
                on the observed telluric standard is used for absolute spectrophotometric calibration.
3. 'false': The observations of the telluric standard stars are compared with a model spectrum for that star.
                This generates a combined correction that includes response curve and telluric features, which is then
                used to correct scientific exposures.

For detailed information on Molecfit, we refer to its user manual which is available
[here](http://www.eso.org/sci/software/pipelines/skytools/molecfit).

The use of molecfit provides in general the best results, as it constructs a model of the atmospheric
transmission, and does not transfer to the science issues that can be included in the extraction of the 1D
standard star spectrum, such as low S/N, cosmic-rays, and recipe failure in the absorption line fitting. However,
it is rather slow, and the user might want to optimize the atmospheric model parameters to improve the execution
speed and the fit performance (LINK).

Another advantage of using molecfit is that it accounts for the dependency of the instrumental spectral
resolution from wavelength, IFU and grating, and rotator angle. This is advisable for example, if a bright target
was not observed with the same IFU and rotator angle as the telluric standard star.

The benefits of using molecfit are in general visible for high S/N targets (S/N >= 20). If the target has
low S/N then it could be tried to switch the usage of molecfit off (by setting the workflow parameter to 'false').
This could also be a strategy if the standard star and the target have been observed with the same IFU. 
In this way, the determination of the response curve is based on the data from that night, and does not rely on 
an average static calibration for the response.

The strategy of running molecfit directly on science has the advantage that the atmospheric model is obtained
under the same atmospheric conditions (water vapor and column densities of molecules) as the science spectra. 
This strategy is recommended if there are science data with high signal-to-noise and few intrinsic features. These
data can be used to determine the correction for all other science frames in the dataset.

## Using a telluric model from a standard star observation <a name="telluric_standard"> </a>

The tasks for determining an atmospheric model from a standard star observation 
are encapsulated in the sub workflow **telluric_on_standard**. It uses the tasks **model_on_standard**
(pipeline recipe **kmos_molecfit_model**) and **transmission_on_standard** (recipe **kmos_molecfit_calctrans**).

There are several recipe parameters for **model_on_standard** which can be used to improve the fit of the
model.

**Limiting the fit to certain IFUs.** `process_ifu` accepts a list of comma-separated integer numbers. 
The processing will then only be executed on those IFUs. Using only one IFU can be useful to increase the
processing speed when trying different parameters. With the default value of '-1', all IFUs that have data are
processed.

**Wavelength ranges.** The fit is performed on a sub-set of wavelength ranges and not to the entire spectrum;
this is found to be more efficient and less time-consuming. The advice is to select few wavelength ranges
that include the expected molecules that are observable in the spectrum. The recipe parameter to be used
is `wave_range`. For example, the entry ’0.815,0.830,0.972,0.986’ will perform the fit in the two ranges 
0.815 < λ[μm] < 0.830 and 0.972 < λ[μm] < 0.986. The quotation marks “ ’ ” are mandatory, spaces are not allowed.
The default value “-1” uses the ranges (values in in μm):
- IZ: ’0.815,0.830,0.894,0.899,0.914,0.919,0.929,0.940,0.972,0.986’
- YJ: ’1.106,1.116,1.075,1.083,1.131,1.137,1.139,1.149,1.155,1.166,1.177,1.189,1.201,1.209,1.263,1.276,1.294,1.303,1.312,1.336’
- H: ’1.482,1.491,1.500,1.512,1.559,1.566,1.598,1.605,1.575,1.583,1.622,1.629,1.646,1.671,1.699,1.711,1.721,1.727,1.746,1.758,1.764,1.767,1.773,1.780,1.789,1.794’
- K: ’1.975,1.987,1.993,2.010,2.041,2.060,2.269,2.291,2.308,2.335,2.360,2.379,2.416,2.440,2.445,2.475’
- HK: ’1.575,1.584,1.594,1.606,1.646,1.671,1.756,1.771,1.781,1.811,1.945,1.969,1.975,1.987,1.993,2.030,2.043,2.089,2.242,2.294,2.308,2.335,2.360,2.379’

It is good advice to limit the number of wavelength regions to 4 or 5. The default ranges are defined
to provide a good fit for all the possible cases at the cost of high execution time, but in general, they
are redundant. Regions have to be selected to include strong telluric features, avoiding at the same time
regions where transmission is close to 0. All molecules expected to contribute
in a specific instrumental wavelength range should be considered when defining the fitting regions.
It is also advisable to define narrow wavelength regions, so that the continuum can be approximated by a
1<sup>st</sup> or 2<sup>nd</sup> order polynomial.

**Molecules.** Only the molecules that appear in the wavelength region of the grism should
be fitted. The recipe parameters `relcol`, `fit_molec`, and `list_molec` should then be defined
accordingly. The default values depend on the instrument configuration and should be valid in general. Change
them only if you have evidence that a given molecule is not affecting the transmission.
The defaults of `list_molec` (enabled with parameter value "-1") are: 
- IZ: ’H2O’
- YJ: ’H2O,CO2,CH4,O2’
- H: ’H2O,CO2,CO,CH4’ 
- K: ’H2O,CO2,CH4’
- HK: ’H2O,CO2,CH4’

For a full list of supported molecules, please consult the molecfit user manual.

 ---
Go to [top](#configuration)


 ---
Go to [top](#configuration)

 ---
Go to KMOS EDPS tutorial [index](../kmos/index)