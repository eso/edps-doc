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

The task `irdis_flat_fiel` generates the IRDIS instrument flat field using narrow- 
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

The distortion map is saved in a FITS file with a total of 16 extensions. 
The first 4 extensions contain values, badpixels, rms and weightmap for 
the distortion in the x direction and the next 4 extensions the same information 
for the distortion in the y direction. 
The first 8 extension contain the information for the left FOV the next 8 extension 
the information for the right FOV.
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

Recipes: `sph_ird_science_dpi`, `sph_ird_science_dbi`, `sph_ird_star_center`

This subworkflow processes on-sky calibrations for imaging data (IRDIS-IMG).

### 5a. Imaging Flux Standard

The task **irdis_science_flux_imaging** uses `sph_ird_science_dbi` 
to reduce flux frames acquired for coronagraphic observations, 
where the telescope is offset to observe the star outside the coronagraph. 

These reductions are not used in the science processing
(no flux calibration is applied to the science data).

### 5b. Polarimetry Flux Standard

The task **irdis_science_flux_polarimetry** uses `sph_ird_science_dpi` 
to reduce flux frames acquired for coronagraphic observations, 
where the telescope is offset to observe the star outside the coronagraph. 

These reductions are not used in the science processing
(no flux calibration is applied to the science data).

### 5c. Coronagraph Center

The task **irdis_coronagraph_center** executes the pipeline recipe `sph_ird_star_center` to 
determine the stellar center position behind the coronagraph and produce a table of frame centers.

The illuminated left and right detector regions are analysed separately using 
a source-detection algorithm with a user-defined sigma threshold.
For each waffle image, the output table records the exposure start time, 
the derived center position, and the IRDIS DMS position converted from microns to pixels.

**Customization**

Recipe parameters:
- `ird.star_center.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `ird.star_center.sigma`: the sigma threshold for source detection
  (default = 10.0).

## 6. Subworkflow Wavelength Calibration

Recipe: `sph_ird_wave_calib`

In spectroscopy mode (IRDIS-LSS) the task **irdis_wavecal_spectroscopy** 
performs the wavelength calibration with the pipeline recipe `sph_ird_wave_calib`. 
Raw frames are combined, dark-subtracted, and flat-fielded, with bad pixels flagged. 
The combined image is sliced along the wavelength direction, 
and calibration lines are detected within a window of ±`ird.wave_calib.line_tolerance` 
around their expected positions.

Measured line positions are matched to known wavelengths and fitted with a polynomial, 
which defines the wavelength solution and interpolates values between calibration lines. 
The updated solution is written to the pixel description table (PDT) as the final product.

The output is a FITS file containing six image extensions, 
each corresponding to a column of the PDT: 
wavelength, spectrum ID, slit ID, wavelength width (or uncertainty), 
second derivative, and illumination fraction. 
Additional extensions include the combined image, a bad-pixel map, and an RMS map.

**Customization**

Recipe parameters:
- `ird.wave_calib.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).

### 7. Science Imaging

Recipe: `sph_ird_science_dbi`

The task **irdis_science_imaging** uses the recipe to produce 
reduced science frames for IRDIS observations 
in dual-band imaging (DBI) mode, 
supporting dithering as well as optional angular differential imaging (ADI), 
 and spectral differential imaging (SDI) processing. 
Raw frames are dark-subtracted (mandatory), optionally flat-fielded, 
and combined with static bad pixels from dark and flat frames. 
Left and right subframes are extracted using the IRDIS instrument model.

The output is an 8-extension FITS file containing image, bad-pixel map, 
N map, and RMS for both left and right FoVs. 
A dark/background frame is required, with priority: 
`SKY_BG_FIT` → `SKY_BG` → `INS_BG_FIT` → `INS_BG` → `MASTER_DARK`; 
matching DIT/readout (and ideally filter) is the user’s responsibility. 
Optional QC includes Strehl ratio estimation when calibration tables are available.

**Customization**

Recipe parameters:
- `ird.science_dbi.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `ifs.science_dbi.use_adi`: enable use of ADI (0 = not applied; Default , 1 = applied).
- `ifs.science_dbi.use_sdi`: enable use of SDI (0 = not applied; Default , 1 = applied).


### 8. Science Polarimetry

Recipe: `sph_ird_science_dpi`

The task **irdis_science_polarimetry** uses the recipe to produce 
reduced science frames for IRDIS observations in DPI mode. 
The processing is essentially identical to the DBI science recipe, 
but the final products are saved as polarization (P) and intensity (I) images 
instead of left and right FoVs (see the IRDIS DBI recipe for processing details).

The main output is a FITS file with eight extensions: 
the first four contain the polarization (P) image, bad-pixel map, RMS map, and weight map, 
while the last four contain the same products for the intensity (I) image. 
When ADI is enabled, only four extensions are written, containing the P image products.

Recipe parameters:
- `ird.science_dpi.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `ifs.science_dpi.use_adi`: enable use of ADI (0 = not applied; Default , 1 = applied).
- `ifs.science_dpi.use_sdi`: enable use of SDI (0 = not applied; Default , 1 = applied).

### 9. Science Spectroscopy

Recipe: `sph_ird_science_spectroscopy`

The task **irdis_science_spectroscopy** uses the recipe to produce 
reduced science frames for spectroscopy mode. 
The processing consists of dark subtraction and flat-fielding 
followed by frame combination using a user-selected method. 
If an atmospheric calibration is provided, it is subtracted from the combined result.

The output is a FITS file containing the reduced 2D spectrum 
for the left FoV as a full-detector image. 
The file includes four extensions: the science image, bad-pixel map, 
N-combination map (number of contributing frames per pixel), and an RMS map.

Recipe parameters:
- `ird.science_spectroscopy.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).

---
Go to SPHERE-IRDIS EDPS tutorial [index](../sphere/index)