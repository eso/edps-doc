# The SPHERE-IFS data reduction flow

The overall data flow of the SPHERE-IFS pipeline is displayed [here](figures/reduction_cascade.jpg).

The reduction cascade is organized in tasks, which represent well defined steps in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
inputs, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The `EDPS` workflow is designed to execute the tasks that deliver
the final reduced data cube for each dataset. 
Currently, the pipeline does not stack science data.

<!-- It can be either the product of a single exposure, or the combination of multiple exposures. Only calibrations needed by the selected the scientific exposures are processed. -->

It is possible to set `EDPS` to perform the data reduction until a certain step of the reduction chain (e.g. to reduce
only standard stars, or only flat fields).
This is done by specifying the desired tasks in the field `Select reduction target` of the `Raw Data` tab.

The reduction steps are listed below. Before starting the reduction, 
the parameters of the recipes associated to each task can be configured by pressing the button ![](../edpsgui/figures/configure_dataset.jpg) close to each dataset configuration.
See [here](configure_reduction.md) for more information.

The reduction steps are:

## 1. Subworkflow: Dark background

Recipes: `sph_ifs_cal_background`, `sph_ifs_master_dark`

This subworkflow generates the instrumental background and dark-current calibration products. 

It consists of the tasks:
- **ifs_instrument_background** 
- **ifs_sky_background**
- **ifs_dark**
- **ifs_static_bad_pixel_map**

which run the pipeline recipes `sph_ifs_cal_background` and `sph_ifs_master_dark`.

The first recipe measures the instrumental background in counts per second per pixel.  
The output is a 4-extension FITS file containing the background image, bad-pixel map, RMS map, and weight map.

The second recipe derives the detector dark current (`IFS_MASTER_DARK`) and a bad pixel map (`IFS_STATIC_BADPIXELMAP`; also contained in the 2nd extension of the master dark).

The master dark is obtained by combining the input raw frames using the selected collapse algorithm. Bad pixels are identified through the following steps:

1. Initial thresholding using `min_acceptable` and `max_acceptable`.
2. Smoothing of the master dark with a Gaussian kernel and subtraction of the smoothed frame to remove large-scale variations.
3. Sigma clipping of the residuals using the `sigma_clip` parameter.

The final (unsmoothed) master dark is written with extensions for the bad-pixel map, RMS, and the number of contributing raw pixels per output pixel.

**Customization**

Recipe parameters:
- `ifs.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `ifs.master_dark.min_acceptable`, `ifs.master_dark.max_acceptable`: pixel-value limits for thresholding (default 0 and 1000; reasonably adjustable within [-100:0] and [800:1000], respectively).
- `ifs.master_dark.sigma_clip`: sigma-clipping threshold (default 3; increase to 5 if you believe too many pixels are flagged).

### 2. Spectra positions

Recipe: `sph_ifs_spectra_positions`

The task **ifs_spectra_positions** runs the pipeline recipe to associate detector pixels with IFS lenslets and assigns an initial wavelength solution to each pixel. 
The first-order solution is later refined by the dedicated wavelength calibration recipe (`sph_ifs_wave_calib`).

Spectral traces are detected via thresholding and used to determine their centroid positions. 
These measured positions are compared to those predicted by a scaled and shifted lenslet model, 
allowing refinement of the model’s scale and position. 
Optionally, a 2D distortion model is fitted and incorporated into the lenslet model to improve wavelength calibration.

The output is a pixel description table (PDT) written out as a FITS image 
with 6  extensions, corresponding to:
wavelength, spectra region id, lenslet id,
wavelength width, second derivate of
wavelength and illumination fraction.

**Customization**

Recipe parameters:

- `ifs.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).


## 3. Wavelength calibration

Recipe: `sph_ifs_wave_calib`

The task **ifs_wavelength_calibration** runs the pipeline recipe to perform the wavelength calibration by refining the pixel-to-wavelength associations
(starting from the model produced by the spectra-positions calibration),
using observed wavelength calibration frames and an existing lenslet model. 

1D spectra are then extracted for each spectral region, and the positions of known calibration lines 
are measured using a flux-weighted centroid within a configurable fitting window. 
These measured line positions are fitted with a polynomial that defines the wavelength solution for each spectrum, 
provided the solution is consistent with the expected dispersion; 
otherwise, the original model wavelengths are retained or the region is flagged as bad.

From the final wavelength solutions, the recipe computes per-spectrum quality-control metrics, 
including minimum, maximum, and central wavelengths, as well as the resolving power derived from the local wavelength gradient. 
The corrected PDT is written as the main product, together with updated QC keywords.

**Customization**

Recipe parameters:

- `ifs.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).

## 4. Subworkflow Detector Flat

Recipe: `sph_ifs_master_detector_flat`

This subworkflow executes the following series of tasks to generate detector flat-field calibrations using exposures 
obtained with narrow or broadband calibration lamps:

- **ifs_det_flat_narrow_band1**
- **ifs_det_flat_narrow_band3**
- **ifs_det_flat_narrow_band4**
- **ifs_det_flat_narrow_band2**
- **ifs_det_flat_broad_band**

It can produce several flat-field components, including a standard detector flat, 
a large-scale (smoothed) flat, and a preamplifier correction flat. 
In practice, the standard `IFS_MASTER_DFF_LONG` products are sufficient to correct pixel-to-pixel 
detector response variations.

Raw frames are dark-subtracted and corrected for preamplifier variations, 
after which the detector flat is derived by fitting, for each pixel, 
a linear relation between its signal and the mean illumination level of each exposure. 
The slope of this fit represents the relative pixel response.
The main output is the detector flat-field image, with optional products including a non-linearity map 
and a smoothed large-scale flat.

**Customization**

Recipe parameters:

- `ifs.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).
- The fit between signal and illumination level can be performed using either 
a maximum-likelihood (`ifs.master_detector_flat.robust_fit` = TRUE; default) 
or a robust linear method (change parameter to FALSE), 
the latter being more resistant to outliers such as cosmic rays. 

## 5. IFU Flat

Recipe: `sph_ifs_instrument_flat`

The task **ifs_ifu_flat** uses the pipeline recipe to generate flat-field calibrations.
It can operate in two modes, depending on the inputs and selected parameters. 

In detector flat (total flat) mode, raw calibration frames are combined to produce 
a flat field that includes the detector response. 
This product can be used by the `spectra-positions` and `wavelength-calibration` recipes (see above).

In IFU flat mode, the recipe uses the PDT and wavelength calibration 
to remove the detector response and isolate the IFU (lenslet) contribution. 
A wavelength-dependent “super-flat” is first constructed from master detector flats 
and used to flat-field the combined raw frames. 
Using the lenslet model from the wavelength calibration, spectra are extracted for all lenslets 
and collapsed along the wavelength direction to derive one flat-field value per lenslet. 
The main output is a table of IFU flat-field values used by subsequent recipes, along with a diagnostic interpolated image.

The outputs are:

- `IFS_INSTRUMENT_FLAT_FIELD` - The total instrument flat field, with 4 extensions: the flat values, the bad pixels, the rms error on the flat and a weightmap.
- `IFS_IFU_FLAT_FIELD` - The IFU flat field, with 4 extensions: the flat values, the bad pixels, the rms error on the flat, a weightmap, and a 1 table extension containing the lenslet flat values.
- `IFS_STATIC_BADPIXELMAP` - Optional output of all non-linear pixels.

**Customization**

Recipe parameters:

- `ifs.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).

## 6. Distortion map

Recipe: `sph_ifs_distortion_map`

The task **ifs_distortion_map** runs the pipeline recipe to measure geometric distortion in the SPHERE IFS lenslet grid. 
Raw calibration frames are reduced similarly to science data, 
with optional background or dark subtraction and flat-fielding. 
The resulting monochromatic images are collapsed along the wavelength axis 
and point sources are detected using a user-defined threshold.

If no reference point pattern is provided, the recipe derives one from the detected sources 
and saves it as a product; otherwise, the supplied pattern is used directly. 
Distortion is computed by comparing detected and expected source positions, 
rejecting vectors larger than a user-defined limit, and fitting the remaining offsets 
with a 2D polynomial model. 
An optional self-consistency check applies the derived distortion to the data 
and outputs a residual distortion map, which can be inspected to assess the quality 
and accuracy of the calibration.

The outputs are:

- `IFS_POINT_PATTERN` - The point pattern, in case that an input point pattern was provided. This product may be used as reference
input for future runs of this recipe.
- `IFS_DISTORTION_MAP` - The distortion map, with 8 extensions. The first 4 contain the  distortion in the x direction, the
badpixels, the rms on the distortion and a weightmap. The second set of 4 extensions contain the same information
but for the y direction.

## 7. Subworkflow Science Data Reduction 

Recipe: `sph_ifs_science_dr`

This subworkflow executes the tasks:

- **ifs_science_flux**
- **ifs_coronagraph_center**
- **ifs_science**

to reduce IFS science observations, 
with optional background or dark subtraction and pre-amplifier stripe correction. 

It also processes FLUX frames acquired during coronagraphic observations, 
where the telescope is offset to move the target away from the coronagraph, 
allowing to measure the stellar flux.

In addition, it processes CENTER frames to determine the stellar position behind the coronagraph. 
This is required to accurately define the center of rotation for pupil-stabilized observations.

Large-scale flat-field effects are removed using a wavelength-dependent “super flat” 
built from multi-colour lamp flats and the wavelength calibration, while small-scale, 
time-dependent pixel-to-pixel variations are corrected using a broadband master flat.

The recipe supports automatic frame combination using "spectral deconvolution"
(a method used to reduce speckle noise; see Mesa et al. 2015) 
and angular differential imaging (ADI), 
which can be enabled or disabled via flags. 
<!-- Pixel-to-pixel detector corrections and bad-pixel interpolation can also be applied, 
with the small-scale flat correction strongly recommended and the large-scale variant deprecated. -->

**Customization**

Recipe parameters:

- `ifs.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `ifs.science_dr.use_adi`: enable use of ADI (0 = not applied, 1 = always applied, 2 = applied only if the total rotation is larger than `ifs.science_dr.min_adi_angle`).
- `ifs.science_dr.min_adi_angle`: minimum angle for automatic ADI switch (when previous parameter equals 2).
- `ifs.science_dr.spec_deconv`: enable use of spectral deconvolution (0 = not applied, 1 = always applied).

## 8. Subworkflow Standard Data Reduction

Recipe: `sph_ifs_science_dr`

This subworkflow executes the tasks:

- **ifs_standard_astrometry**
- **ifs_standard_flux**

At the moment, astrometry and flux standard observations are processed like science data.

---
Go to SPHERE EDPS tutorial [index](../sphere/index)