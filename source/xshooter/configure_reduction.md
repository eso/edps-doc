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

For XSHOOTER, the following workflow parameters can be adjusted 
when the `Target Category` is set to *science*:

- `use_flat`: 
By default, this parameter is set to *science*, 
meaning the flats used for science frames are also applied to standard stars.
Set it to *standard* to use the flats taken closest in time 
to the standard-star observations instead.
- `telluric_correction_mode`: 
Atmospheric parameters can be derived either from 
a telluric standard or from the science frame itself.
Set this parameter to *standard* (default) to use a telluric star 
observed the same night with the same instrument setup.
Set it to *science* to derive the parameters directly from the science.
Use *none* to disable telluric correction.
- `response`:
This parameter selects the response curve used for flux calibration.
*night* (default) uses the response from the standard star observed that night; 
if unavailable, fall back to the master response.
*master* uses the master response from CalSelector, 
built by combining standards from multiple nights.
- `reduction-mode`:
Select between the physical-model mode (recommended) 
and the polynomial mode to map each wavelength onto the CCDs.
The physical model derives the solution from the actual optical path, 
while the polynomial method uses empirical multi-coefficient fits per order.
If the reduction fails or the physical model appears inconsistent, 
the polynomial mode can be used for troubleshooting or as a fallback.
- `max_diameter`:
TODO
- `max_separation`:
TODO
- `use_optical_dark`:
This parameter controls the use of a dark frame in the UVB/VIS data reduction.
Because the dark current is negligible at these wavelengths, 
it is set to *FALSE* by default.
Set it to *TRUE* if you wish to enable dark correction.

```{comment}
## Bad Pixels <a name="first_step"> </a>

The pipeline performs by default standard extraction between ± 2.0 arcsec 
(controlled by `localize-slit-hheight`) 
around the centre of the slit 
(controlled by `localize-slit-position`). 
Flagged pixels falling outside the extraction region 
do not affect the standard extraction algorithm. 
Flagged pixel falling inside the extraction region
are interpolated during the standard extraction algorithm
by constructing a local spatial profile. 
The local spatial profile uses a number of points 
(controlled by `stdextract-interp-hsize`)
at a certain distance from the wavelength for which interpolation is required.

 ---
Go to [top](#configuration)
```

## Troubleshooting <a name="troubleshooting"> </a>

This section provides guidance for diagnosing and resolving 
common issues encountered during the XSHOOTER data-reduction cascade.

### Not enough arc lines detected <a name="lines_not_found"> </a>

The recipe `xsh_2dmap` may fail with an error indicating that not enough arc lines were detected.
Typical expected values for `QC.NLINE.FOUND.CLEAN` are:
- UVB: ~2550 lines
- VIS: ~3950 lines
- NIR: ~1300 lines

Verify the quality and consistency of the input calibration products, in particular:
- `ARC_LINE_LIST_ARM`
- `THEO_TAB_MULT_ARM` (poly mode)
- `ORDER_TAB_EDGES_SLIT_ARM`
- `WAVE_TAB_GUESS_ARM`

In addition, adjust the line-detection parameters:

- increase `detectarclines-search-winhsize`
- decrease `detectarclines-min-sn`
to ensure more arc lines are detected.

 ---
Go to [top](#configuration)

### Sky subtraction residuals (especially NIR) <a name="high_nir_res"> </a>

Residual tilts between the sky model and the observed 2D frame
can introduce sky–subtraction artefacts, particularly in the NIR.
In practice, this manifests as alternating under- and over-subtracted regions
around OH emission lines.
See Figure {numref}`fig-res` as an example. 

Possible workarounds:

– #1 — Verify the accuracy of the `xsh_2dmap` products.
Run the reduction chain in physical-model mode, 
which provides a more robust 2D geometry than the polynomial mode.
Ensure that the residuals after model optimisation are small; 
if needed, re-run `xsh_2dmap` with additional iterations.

– #2 — Try setting `sky-method` = MEDIAN.
This can improve stability when the BSPLINE models fail 
due to slight geometric mismatches.

– #3 — Apply flexure corrections computed by `xsh_flexcomp`.
Flexure compensation can realign the sky model and 
reduce systematic sky–subtraction residuals.

```{figure} figures/NIR_residuals.jpg
:alt: residuals
:name: fig-res

Example of alternating under- and over-subtracted regions around OH emission lines,
caused by a slight tilt of the sky lines relative to the object trace.
The plot on the right shows the flux profile extracted along the green line
in the 2D image.
```

 ---
Go to [top](#configuration)

### Trace-localization failures <a name="trace_loc"> </a>

`xsh_scired_slit_XXX` may fail when `extraction-method` = LOCALIZATION 
and `localize-method` is set to either GAUSSIAN or MAXIMUM.

This issue typically occurs with low S/N science exposures, 
where the object trace cannot be reliably detected using either 
the Gaussian cross-order profile or the maximum-detection algorithm.

The user should try adjusting
`localize-slit-position` and `localize-slit-hheight`
to guide the trace-localization process,
or alternatively set `extraction-method` = MANUAL,
which avoids automatic trace detection altogether.

 ---
Go to [top](#configuration)

### Two object traces in the slit <a name="two_objects"> </a>

Reduce each object trace separately by providing appropriate values in
the `xsh_scired_slit_XXX` recipe for the parameters
`sky-position1`, `sky-hheight1`, `sky-position2`, and `sky-hheight2`.
These parameters define the specific regions of the slit used 
to estimate the sky during single-frame sky subtraction.

By default, all four parameters are set to zero, meaning that the sky is taken from all
pixels outside the object localization region (and outside the masked slit edges).
However, when multiple objects are present along the slit, or when the default choice is not
appropriate, the user should manually adjust these positions.

Both the central positions and the half-heights of the sky regions are expressed in arcseconds.

 ---
Go to [top](#configuration)

### Order-edge artefacts in extracted spectra <a name="order_edges"> </a>

Artefacts may affect the edges of the 2D and 1D orders, 
degrading the quality of the merged extracted 2D and 1D spectra.

In such case, use the appropriate reference format-check frames 
and verify that the values of 
`WLMIN` and `WLMAX` in `xsh_scired_slit_XXX` are correct.
They should correspond to the last wavelength imaged 
on the illuminated part of the order, divided by 1.007.

This can be checked by projecting the region files produced 
by the script `test_xsh_data_wave_tab_2d` onto the 
2D sky-subtracted science image.

Alternatively, in physical-model mode, the user may provide 
a reference sky-line table (`SKY_LINE_LIST_ARM`) 
and project the predicted sky-line positions onto 
the 2D sky-subtracted frame to assess the consistency of order edges.

 ---
Go to [top](#configuration)

### Small jumps between orders <a name="orders_jump"> </a>

Small discontinuities may appear between orders during merging, 
typically caused by slit-edge artefacts introduced by the flat-field.
To mitigate this, we recommend setting `extract-method` = LOCALIZATION 
in `xsh_scired_slit_XXX`.

For low S/N objects, use `localize-method` = MANUAL and 
provide appropriate values for `localize-slit-position` and `localize-slit-hheight`.
For high S/N objects, `localize-method` = AUTO is generally sufficient.

 ---
Go to [top](#configuration)

### Overestimated uncertainties in the extracted spectrum <a name="large_err"> </a>

This issue is typically caused by slit-edge artefacts introduced by the flat-field.
To mitigate it, set `extract-method` = LOCALIZATION in `xsh_scired_slit_XXX` 
and choose an appropriate localization strategy:

For low S/N objects, use `localize-method` = MANUAL 
and specify suitable values for
`localize-slit-position` and `localize-slit-hheight`.

For high S/N objects, localize-method = AUTO is usually sufficient.

 ---
Go to [top](#configuration)

### The extracted merged 1D spectrum looks poor  <a name="bad_quality"> </a>

The `xsh_respon_slit_xxx` and/or `xsh_scired_slit_xxx` recipes may have
failed to localize the trace correctly during extraction.

Try setting `extract-method` = LOCALIZATION and provide appropriate values 
for `localize-slit-position` and `localize-slit-hheight`, 
based on the appearance of the merged 2D spectral image
(e.g. `SCI_SLIT_FLUX_MERGE2D_NIR.fits`).

These parameters should be tuned so that:
- the object lies near the centre of the extraction aperture, and
- the extraction window fully includes the entire positive flux profile.

 ---
Go to [top](#configuration)

### Spectral regions of zero flux values <a name="zero_flux"> </a>

Large regions of zero-flux values in the final extracted 1D spectrum
may be caused by spurious Cosmic-Ray (CR) detections. 
See {numref}`fig-cr` as an example of affected spectrum.

CR-contaminated pixels are identified using the van Dokkum algorithm 
([2001, PASP, 113, 1420](https://scixplorer.org/abs/2001PASP..113.1420V/abstract)) 
applied to the input science frames.
The detection threshold is controlled by the parameter
`removecrhsingle-sigmalim`, whose default value is 5.0 for the UVB and VIS arms.
For the NIR arm, CR detection is disabled by default by setting
`removecrhsingle-niter` to 0.

In observations obtained under excellent seeing conditions (≈0.4″ or better),
the stellar PSF may appear sharp enough to be mistakenly flagged as CR-affected.
To reduce these false detections, increase the value of
`removecrhsingle-sigmalim`.
Figure {numref}`fig-cr2` illustrates the improvement obtained on the same observation.

```{figure} figures/CR_detections_bad.jpg
:alt: cr
:name: fig-cr

Here we show the VIS spectrum of the telluric standard star Hip089684,
as displayed in the `Graphical reports`.
The observation was obtained on May 1, 2023
(OB identifier: `XSHOO.2023-05-02T07:37:22.135`)
under excellent seeing conditions (0.4″).
With the default value `removecrhsingle-sigmalim`=5.0,
the algorithm produces spurious cosmic-ray detections,
which in turn lead to extended wavelength intervals with zero flux
in the extracted 1D spectrum.
```

```{figure} figures/CR_detections_good.jpg
:alt: cr
:name: fig-cr2

Same as {numref}`fig-cr`, but with `removecrhsingle-sigmalim`=7.0.
In this case, this avoids the flagging of good pixels as CR-affected.
```

### IFU cube not well aligned <a name="ifu_misaligned"> </a>



 ---
Go to [top](#configuration)

 ---
Go to XSHOOTER EDPS tutorial [index](../xshooter/index)