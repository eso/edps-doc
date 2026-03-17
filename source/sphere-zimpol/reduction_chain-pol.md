# The SPHERE ZIMPOL data reduction flow (polarimetry).

The overall data flow of the SPHERE pipeline for ZIMPOL data is displayed [here](figures/reduction_cascade-pol.jpg) for the 
polarimetry mode (see previous section for imaging).

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

The reduction steps of the **polarimetry** workflow are listed below. Before starting the reduction, 
the parameters of the recipes associated to each task can be configured by pressing the button ![](../edpsgui/figures/configure_dataset.jpg) close to each dataset configuration.
See [here](configure_reduction.md) for more information.

The reduction steps are:

## 1. Subworkflow Internal Calibrations Polarimetry

Recipes: `sph_zpl_master_bias`, `sph_zpl_master_dark`, `sph_zpl_intensity_flat`, `sph_zpl_modem_efficiency`

This subworkflow produces the internal calibration products required for ZIMPOL polarimetric data reduction. 
It generates the master bias, master dark, intensity flat fields, 
and the modulation–demodulation (modem) efficiency calibration for the two ZIMPOL cameras.

The processing proceeds in four steps:

- **zimpol_bias_polarimetry**: uses the pipeline recipe `sph_zpl_master_bias` to create the master bias.
This calibration is associated with downstream tasks only in FastPolarimetry readout mode.
- **zimpol_dark_polarimetry**: uses `sph_zpl_master_dark` to generate the master dark.
This calibration is used only for SlowPolarimetry exposures longer than 30 s, 
and may use the master bias when applicable.
- **zimpol_flat_polarimetry_cam1** and **zimpol_flat_polarimetry_cam2** use `sph_zpl_intensity_flat` to
produce the intensity flat fields (pixel-to-pixel sensitivity calibrations) for each ZIMPOL camera.
- **zimpol_modem_efficiency_cam1** and **zimpol_modem_efficiency_cam2** use `sph_zpl_modem_efficiency` to
produce the modem efficiency calibration.
Modem-efficiency calibration frames (FLAT,POL100) are processed to measure the efficiency of the detector modulation–demodulation cycle.
The modem efficiency is computed from the measured Stokes signals as the ratio P/I.
The resulting modem efficiency products for both cameras are required inputs 
for all subsequent ZIMPOL polarimetric reduction recipes.

Recipe parameters:
- `zpl.flat_polarimetry_cam?.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).
- `zpl.modem_efficiency_cam?.coll_alg`: collapse algorithm 
(0 = Mean, 1 = Median, 2 = Clean Mean; default).

## 2. Coronagraph Center

Recipe: `sph_zpl_star_center_pol`

The task **zimpol_coronagraph_center_polarimetry** executes the pipeline recipe 
to determine the stellar center position behind the coronagraph in polarimetric mode 
and produce calibrated star-center frames. 

The input frames may be either raw polarimetric star-center frames (`ZPL_STAR_CENTER_POL_RAW`) 
or pre-processed frames (`ZPL_STAR_CENTER_POL_PREPROC_CAM1` and/or `ZPL_STAR_CENTER_POL_PREPROC_CAM2`). 
Optional calibration inputs include master bias, master dark, intensity flat-field, polarization flat-field, and modulation/demodulation efficiency (modem) calibrations.

If raw frames are provided, the recipe first performs a pre-processing step using `sph_zpl_preproc` 
to generate pre-processed frames for both ZIMPOL cameras.
The calibrated frames are then de-dithered (if required) and saved as intermediate products.
All calibrated frames are then combined using a collapse mean algorithm, 
producing a DOUBLE IMAGE product (8 FITS extensions) containing:

- a combined intensity image (I) with its bad-pixel map, number-of-combined frames map, and RMS map;
- a combined polarimetric image (P) with its bad-pixel map, number-of-combined frames map, and RMS map.

The combined star-center image is analyzed using an aperture detection algorithm 
that identifies bright regions (e.g., waffle satellite spots or a single star) 
and computes their geometric center, which defines the frame center. 

The detected center coordinates are stored in the FITS headers for each camera:

- `DRS ZPL STAR CENTER IFRAME XCOORD`
- `DRS ZPL STAR CENTER IFRAME YCOORD`
- `DRS ZPL STAR CENTER PFRAME XCOORD`
- `DRS ZPL STAR CENTER PFRAME YCOORD`

The star-center products are used in subsequent science polarimetric reductions 
to define the rotation center during frame combination.

**Customization**

Recipe parameters:
- `zpl.star_center.coll_alg`: collapse algorithm (0 = Mean; default, 1 = Median, 2 = Clean Mean).
- `zpl.star_center.sigma`: the sigma threshold for source detection (default = 10.0).
- `zpl.star_center.save_interprod`: enable to produce a field center table containing the calculated center positions
(default = FALSE). 

## 3. Subworkflow Standard Polarimetry

Recipe: `sph_zpl_science_p1`

This subworkflow processes polarimetric standard-star observations used for calibration monitoring. 
It reduces observations of unpolarized and highly polarized standard stars in order to assess 
the instrument’s polarimetric performance.

Two tasks are executed:

- **zimpol_standard_polarimetry_unpolarized**: Processes observations of unpolarized standard stars 
to measure the level of instrumental polarization introduced by the instrument.
- **zimpol_standard_polarimetry_polarized**: Processes observations of highly polarized standard stars 
to determine possible offsets in polarization degree and polarization angle.

Both tasks run the polarimetric science recipe (`sph_zpl_science_p1`) and use the relevant calibration products, 
including bias, dark, intensity flat, and modulation–demodulation efficiency (modem) calibrations, 
as well as the polarimetric correction and filter tables. For polarized standards, 
an additional reference table of polarized stars is used.

The resulting products are used for quality control and instrument monitoring (qc1calib, calchecker) 
and are not required for the reduction of science observations.

**Customization**

Recipe parameters:
- `zpl.science_p1.coll_alg`: collapse algorithm (0 = Mean; default, 1 = Median, 2 = Clean Mean)
- `zpl.science_p1.save_interprod` enable to produce
a field center table containing the calculated center positions (default = FALSE). 

## 4. Subworkflow Science Polarimetry P1

Recipe: `sph_zpl_science_p1`

The subworkflow contains two tasks:

- **zimpol_science_flux_p1**, which reduces flux frames obtained with the star moved off the coronagraph;
- **zimpol_science_p1**, which reduces the science polarimetric observations themselves.

Both tasks use the pipeline recipe `sph_zpl_science_p1` and process polarimetric frames obtained in ZIMPOL P1 mode.

Optional calibration inputs include master bias, master dark, intensity flat-field, polarization flat-field, and modulation–demodulation efficiency (modem) calibration frames for each camera. If raw frames are provided, a pre-processing step on the raw cubes is performed with `sph_zpl_preproc` to generate pre-processed frames.

The pre-processed science frames are organized into measurement groups corresponding to the Stokes parameters (Q measurements: Qplus and Qminus and U measurements: Uplus and Uminus).

The frames in each group are calibrated by subtracting the master bias and master dark frames and dividing by the appropriate intensity flat field, if available. The demodulation step then computes the intensity (I) and polarization component (P) frames. The polarization flat-field and modem efficiency corrections are subsequently applied.

The calibrated frames are then de-dithered and de-rotated, and saved as intermediate products.  
The center of rotation is taken from the star-center calibration frames (`SPH_ZPL_TAG_STAR_CENTER_POL_CALIB_CAM*`) when available; otherwise, the geometric center of the frame (`xc = yc = 512`) is used.

In the next step, the calibrated frames of each measurement group are combined using the collapse mean algorithm, producing DOUBLE IMAGE products (8 FITS extensions) for each group containing:

- a combined intensity image (I) with its bad-pixel map, number-of-combined (ncomb) frames map, and RMS map;
- a combined polarimetric image (P) with its bad-pixel map, ncomb map, and RMS map.

Finally, the Qplus and Qminus frames (and similarly Uplus and Uminus) are combined polarimetrically:

- **Q:**  
  `I = [I(+Q) + I(-Q)] / 2`  
  `P = [P(+Q) - P(-Q)] / 2`

- **U:**  
  `I = [I(+U) + I(-U)] / 2`  
  `P = [P(+U) - P(-U)] / 2`

The reduced products from `zimpol_science_flux_p1` are used to measure the flux of the target in non-coronagraphic frames and are not themselves the final science products.  
The task `zimpol_science_p1` produces the final reduced Q and/or U DOUBLE IMAGE products for both cameras.

**Customization**

Recipe parameters:
- `zpl.science_p1.coll_alg`: collapse algorithm (0 = Mean; default, 1 = Median, 2 = Clean Mean)
- `zpl.science_p1.save_interprod` enable to produce
a field center table containing the calculated center positions (default = FALSE). 

## 5. Subworkflow Science Polarimetry P23

Recipe: `sph_zpl_science_p23`

The subworkflow contains two tasks:

- **zimpol_science_flux_p2**, which reduces flux frames obtained with the star moved off the coronagraph;
- **zimpol_science_p2**, which reduces the science polarimetric observations themselves.

Both tasks use the pipeline recipe `sph_zpl_science_p23` and process polarimetric frames obtained in ZIMPOL P23 modes.

Optional calibration inputs include master bias, master dark, intensity flat-field, polarization flat-field, and modulation–demodulation efficiency (modem) calibration frames for each camera. If raw frames are provided, a pre-processing step on the raw cubes is performed with `sph_zpl_preproc` to generate pre-processed frames.

The pre-processed science frames are organized into measurement groups corresponding to the Stokes parameters (Q measurements: Qplus and Qminus and U measurements: Uplus and Uminus).
The frames in each group are calibrated by subtracting the master bias and master dark frames and dividing by the appropriate intensity flat field, if available. The demodulation step then computes the intensity (I) and polarization component (P) frames. The polarization flat-field and modem efficiency corrections are subsequently applied.
The calibrated frames are then de-dithered and saved as intermediate products.  

In the next step, the calibrated frames of each measurement group are combined using the collapse mean algorithm, producing DOUBLE IMAGE products (8 FITS extensions) for each group containing:

- a combined intensity image (I) with its bad-pixel map, number-of-combined (ncomb) frames map, and RMS map;
- a combined polarimetric image (P) with its bad-pixel map, ncomb map, and RMS map.

Finally, the Qplus and Qminus frames (and similarly Uplus and Uminus) are combined polarimetrically:

- **Q:**  
  `I = [I(+Q) + I(-Q)] / 2`  
  `P = [P(+Q) - P(-Q)] / 2`

- **U:**  
  `I = [I(+U) + I(-U)] / 2`  
  `P = [P(+U) - P(-U)] / 2`

The reduced products from `zimpol_science_flux_p2` are used to measure the flux of the target in non-coronagraphic frames and are not themselves the final science products.  
The task `zimpol_science_p2` produces the final reduced Q and/or U DOUBLE IMAGE products for both cameras.

**Customization**

Recipe parameters:
- `zpl.science_p23.coll_alg`: collapse algorithm (0 = Mean; default, 1 = Median, 2 = Clean Mean)
- `zpl.science_p23.save_interprod` enable to produce
a field center table containing the calculated center positions (default = FALSE). 

---
Go to [top](#top)

---
Go to SPHERE EDPS tutorial [index](../sphere-zimpol/index)