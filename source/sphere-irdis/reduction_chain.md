# The SPHERE-IRDIS data reduction flow

The overall data flow of the SPHERE-IRDIS pipeline is displayed [here](figures/reduction_cascade.jpg).

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

Recipes: `sph_ird_master_dark`, `sph_ird_ins_bg`, `sph_ird_sky_bg`

This subworkflow generates the dark-current frame, instrumental background and sky background calibration products. 

It consists of the tasks:
- **irdis_dark_imaging**
- **irdis_static_bad_pixel_map**
- **irdis_instrument_background** 
- **irdis_sky_background**

First, `sph_ird_master_dark` creates the master dark calibration frame by combining 
raw dark exposures using the selected collapse algorithm (typically clean mean). 
Bad pixels are identified after combination. 
The master dark is written as the main product, 
and a separate hot-pixel map is also generated.

Next,  `sph_ird_ins_bg` generates the instrument background calibration frame 
using only raw background exposures. The input frames are combined with 
the selected collapse algorithm to produce the final background product. 
Unlike the master dark recipe, no bad-pixel map is created. 

Finally, `sph_ird_sky_bg` generates the sky background calibration frame 
by combining raw background exposures. Unlike the master dark recipe, 
it does not produce a bad-pixel map. 

The resulting `MASTER_DARK`, `INS_BG`, and `SKY_BG` products are intended 
solely for subtraction from raw data and are not flat-fielded 
or corrected for other dark or background frames.
They contain 4 extensions: the image, badpixels, the weightmap 
(how many frames contribute to each pixel), and the rms map.

**Customization**

Recipe parameters:
- `ird.sky_bg.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).

## 2. Master Flat

Recipe: `sph_ird_master_detector_flat`

This task generates the IRDIS instrument flat field using narrow- 
or broadband lamp exposures and varying flux levels.
The resulting flat must be applied only to matching data.
For optimal dark subtraction, raw dark frames with matching DITs should be provided; 
each flat is corrected using the closest matching dark. 
If raw darks are unavailable, background products are used in the following priority order: 
`INS_BG_FIT` → `INS_BG` → `MASTER_DARK`. 
The recipe can run without darks, but this is discouraged. 

After dark correction, illuminated regions are identified using thresholding 
and detector windows are treated separately. For each pixel, a linear fit 
between its signal and the exposure mean level is performed; 
the slope defines the flat-field value (typically close to unity). 
The fit can be maximum-likelihood or robust (better against outliers). 
The main output is the flat-field image. 
Optional products include a non-linearity map and bad-pixel information. 
The master flat’s bad-pixel extension contains all bad pixels at this stage 
(including input static bad pixels), while the optional static bad-pixel output 
includes only those newly identified by this recipe.

**Customization**

Recipe parameters:
- `ird.instrument_flat.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `ird.instrument_flat.robust_fits` is FALSE by default. 
Changing to TRUE can provide better results against outliers (e.g., cosmic rays).

## 3. Distortion map

Recipe: `sph_ird_distortion_map`

The task **irdis_distortion_map** runs the pipeline recipe to derive 
the IRDIS geometric distortion map from calibration frames reduced 
as standard science data (field-stabilized, no dithering), 
optionally including dark subtraction and flat-fielding. 
After combining the frames, point sources are detected using a user-defined threshold. 
If no reference point pattern is provided, the recipe creates one; 
otherwise, it compares detected positions with the expected pattern to measure distortion. 
The optical axis is estimated from the most central point, 
the patterns are aligned, outliers beyond a user-defined maximum distortion are rejected, 
and 2D polynomial fits are computed to model the X and Y distortion across the detector.

The distortion map is saved in a FITS file
with a total of 16 extensions. The first 4
extensions contain values, badpixels,
rms and weightmap for the distortion in
the x direction and the next 4
extensions the same information for the
distortion in the y direction. The first 8
extension contain the information for
the left FOV the next 8 extension the
information for the right FOV.
Optional QC products include images of the input point patterns, 
corrected detector and FoV images, and residual distortion maps 
(typical residuals < 0.1 pixels for good solutions). 
The estimated optical axis position and full polynomial coefficients are recorded 
in header keywords for monitoring and verification.

**Customization**

Recipe parameters:
- `ird.distortion_map.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `ird.distortion_map.threshold`: threshold for source detection (default is 3.0).

## 4. Subworkflow Standard Imaging

In this subworkflow, flux and astrometric standard frames are processed using the tasks 
**irdis_standard_flux_imaging** and **irdis_standard_astrometry_imaging**.  

These tasks execute the recipes `sph_ird_science_imaging` (for classical imaging, CI) 
and `sph_ird_science_dbi` (for dual-band imaging, DBI), respectively.

### 4a. Standard Flux Imaging

Recipe: `sph_ird_science_imaging`

The task **irdis_standard_flux_imaging** uses the pipeline recipe to produce 
reduced flux standard frames for zero point calibration. 
Raw frames are dark-subtracted (mandatory), optionally flat-fielded, 
and a combined bad-pixel map is generated. 
Left and right subframes are extracted using the IRDIS instrument model.
Frames are combined using weighted mean, mean (with bad-pixel rejection), or median. 
The final product is a multi-extension FITS file 
(8 extensions: image, bad-pixel map, N map, RMS for left and right FoVs).

**Customization**

Recipe parameters:
- `ird.science_imaging.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).

### 4b. Standard Astrometry Imaging

Recipe: `sph_ird_science_dbi`

The task **irdis_standard_astrometry_imaging** uses the pipeline recipe 
to produce reduced astrometry standard frames. 
Raw frames are dark-subtracted (mandatory), optionally flat-fielded, 
and a combined bad-pixel map is generated. 
Left and right subframes are extracted using the IRDIS instrument model. 
Frames are combined using weighted mean, mean (with bad-pixel rejection), or median. 
The final product is a multi-extension FITS file 
(8 extensions: image, bad-pixel map, N map, RMS for left and right FoVs).
**Customization**

Recipe parameters:
- `ird.science_dbi.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).

## 5. Subworkflow On-Sky Science Calibrations

This subworkflow processes on-sky calibrations for imaging data.

### 5a. Polarimetry flux standard



### 5b. Imaging flux standard
### 5c. Polarimetry flux standard

Recipes: `sph_ird_science_dpi`, `sph_ird_science_dbi`, `sph_ird_star_center`

## 5. Subworkflow On-Sky Science Calibrations

Recipe: `sph_ird_science_dbi`, `sph_ird_star_center`

## 6. Subworkflow Wavelength Calibration

Recipe: `sph_ird_wave_calib`


### 2. Spectra positions

Recipe: `sph_IRDIS_spectra_positions`

The task **IRDIS_spectra_positions** runs the pipeline recipe to associate detector pixels with IRDIS lenslets and assigns an initial wavelength solution to each pixel. 
The first-order solution is later refined by the dedicated wavelength calibration recipe (`sph_IRDIS_wave_calib`).

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

- `IRDIS.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).


## 3. Wavelength calibration

Recipe: `sph_IRDIS_wave_calib`

The task **IRDIS_wavelength_calibration** runs the pipeline recipe to perform the wavelength calibration by refining the pixel-to-wavelength associations
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

- `IRDIS.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).









This subworkflow executes the tasks:

- **IRDIS_science_flux**
- **IRDIS_coronagraph_center**
- **IRDIS_science**

to reduce IRDIS science observations, 
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

- `IRDIS.master_dark.coll_alg`: collapse algorithm (0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `IRDIS.science_dr.use_adi`: enable use of ADI (0 = not applied, 1 = always applied, 2 = applied only if the total rotation is larger than `IRDIS.science_dr.min_adi_angle`).
- `IRDIS.science_dr.min_adi_angle`: minimum angle for automatic ADI switch (when previous parameter equals 2).
- `IRDIS.science_dr.spec_deconv`: enable use of spectral deconvolution (0 = not applied, 1 = always applied).

## 8. Subworkflow Standard Data Reduction

Recipe: `sph_IRDIS_science_dr`

This subworkflow executes the tasks:

- **IRDIS_standard_astrometry**
- **IRDIS_standard_flux**

At the moment, astrometry and flux standard observations are processed like science data.

---
Go to SPHERE EDPS tutorial [index](../sphere/index)