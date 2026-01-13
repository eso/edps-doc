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

 ---
Go to KMOS EDPS tutorial [index](../kmos/index)