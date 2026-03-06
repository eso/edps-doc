# The SPHERE ZIMPOL data reduction flow (imaging).

The overall data flow of the SPHERE pipeline for ZIMPOL data is displayed [here](figures/reduction_cascade-img.jpg) for the 
imaging mode (see next section for polarimetry).

The reduction cascade is organized in tasks, which represent well-defined steps in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The EDPS workflow is designed to execute the tasks that deliver
the final reduced data cube for each dataset. It can be either the product of a single exposure, or the combination of
multiple exposures. Only calibrations needed by the selected the scientific exposures are processed.

It is possible to set EDPS to perform the data reduction until a certain step of the reduction chain (e.g. to reduce
only standar stars, or only flat fields).
This is done by specifying the desired tasks in the field **Select reduction target** of the **Raw Data** tab.

The reduction steps of the **imaging** workflow are listed below. Before starting the reduction, 
the parameters of the recipes associated to each task can be configured by pressing the button ![](../edpsgui/figures/configure_dataset.jpg) close to each dataset configuration.
See [here](configure_reduction.md) for more information.

The reduction steps are:

## 1. Subworkflow Internal Calibrations Imaging

Recipes: `sph_zpl_intensity_flat_imaging`, `sph_zpl_master_dark_imaging`, `sph_zpl_master_bias_imaging`

This subworkflow generates the camera master flats, the master dark and bais. It consists of the following tasks:

- **zimpol_flat_imaging_cam2**: uses `sph_zpl_intensity_flat_imaging` to produce intensity flat-field calibration frames for camera 2.
- **zimpol_flat_imaging_cam1**: uses `sph_zpl_intensity_flat_imaging` to produce intensity flat-field calibration frames for camera 1.
- **zimpol_dark_imaging**: uses `sph_zpl_master_dark_imaging` to generate master dark calibration frames.
- **zimpol_bias_imaging**: uses `sph_zpl_master_bias_imaging` to produce the master bias calibration frame.

Each time, the calibration (flat, dark or bias) is generated separately for the odd (informative) and even (dark current) 
ZIMPOL sub-frames and stored in a DOUBLE IMAGE FITS format. 
If raw frames are provided, a pre-processing step on the raw cubes is performed with `sph_zpl_preproc_imaging` to generate pre-processed frames.
Outputs include the master calibration (flat, dark or bias), 
as well as a bad-pixel map, a number-of-combined frames map, and an RMS map.


In practice, bias and darks are rarely used in the current workflow:

- Bias frames are used only for Fast Polarimetry readout mode (`DET.READ.CURNAME` = FastPolarimetry).
- Dark frames are used only for long exposures, defined as `EXPTIME` > 30 s.

Recipe parameters:
- `zpl.intensity_flat.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median; default, 2 = Clean Mean).


## 2. Coronagraph Center

Recipe: `sph_zpl_star_center_img`

The task **zimpol_coronagraph_center_imaging** executes the pipeline recipe to 
determine the stellar center position behind the coronagraph and produce a table of frame centers.
If raw frames are provided, a pre-processing step on the raw cubes is performed with `sph_zpl_preproc_imaging` to generate pre-processed frames.

The combined images are analyzed with an aperture detection algorithm that identifies bright regions 
(e.g., waffle satellite spots or a single star) and computes their geometric center, which defines the frame center.
The resulting center coordinates are stored in the FITS header.

**Customization**

Recipe parameters:
- `zpl.star_center.coll_alg`: collapse algorithm 
(0 = Mean; default, 1 = Median, 2 = Clean Mean).
- `zpl.star_center.sigma`: the sigma threshold for source detection
  (default = 10.0).

## 3. Subworkflow Standard Imaging

Recipe: `sph_zpl_science_imaging` 

The tasks **zimpol_standard_astrometry_imaging** 
and **zimpol_standard_flux_imaging** both use `sph_zpl_science_imaging` 
to reduce calibration frames of astrometric and flux standards.
The calibration steps and customizable parameters are the same 
as for the science frames (see below).

## 4. Subworkflow Science Imaging

Recipe: `sph_zpl_science_imaging` 

The task **zimpol_science_flux_imaging** uses the pipeline recipe to reduce and combine science frames. 
Optional calibration inputs include master bias, master dark, and intensity flat-field frames for each camera.
If raw frames are provided, a pre-processing step on the raw cubes is performed with `sph_zpl_preproc_imaging` to generate pre-processed frames.

The pre-processed science frames are then calibrated by subtracting the master bias and master dark frames 
and dividing by the appropriate flat field, if available.

The calibrated frames are subsequently de-dithered and de-rotated, and saved as intermediate products. 
The center of rotation is taken from the star-center calibration frames (`SPH_ZPL_TAG_STAR_CENTER_IMG_CALIB_CAM*`/2) when available; 
otherwise, the geometric center of the frame (xc=512, yc=512) is used.

In the final step, all calibrated, de-dithered, and de-rotated frames are combined using a mean algorithm. 
The resulting products for each camera are written in DOUBLE IMAGE format (8 FITS extensions), containing:

- a combined science intensity image, bad-pixel map, number-of-combined frames map, and RMS map;
- a combined dark-current image, with corresponding bad-pixel map, ncomb map, and RMS map.

These outputs constitute the final reduced science products for both ZIMPOL cameras.

For point sources, the recipe can also estimate the Strehl ratio if a filter-table calibration frame is available. 
When successful, Strehl-related quality-control parameters are written into the product headers.

**Customization**

Recipe parameters:
- `zpl.science_imaging.coll_alg`: collapse algorithm 
(0 = Mean; default, 1 = Median, 2 = Clean Mean).

---
Go to SPHERE EDPS tutorial [index](../sphere-zimpol/index)