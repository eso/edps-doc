# The XSHOOTER data reduction flow

The overall data flow of the XSHOOTER pipeline is displayed [here](figures/reduction_cascade.jpg).

The reduction cascade is organized in tasks, 
which represent well-defined steps in the process. 
Tasks are grouped inside sub-workflows. 
Each task runs a recipe; 
the detailed description of the algorithms, input, outputs and recipe parameters 
used in each recipe are available in the pipeline manual. 
Here, we present only the description of the most important features.

The `EDPS` workflow is designed to execute the tasks that deliver
the final reduced spectrum (per order and merged) for each dataset, 
optionally flux- and telluric-calibrated.
Only calibrations needed by the selected scientific exposures are processed.

It is possible to set `EDPS` to perform the data reduction until a certain step of the reduction chain 
(e.g. to reduce  only standard stars, or only flat fields).
This is controlled by the `Select the reduction target` option in the `Raw Data` tab.

The reduction steps are listed below. Before starting the reduction, 
the parameters of the recipes associated to each task can be configured by pressing the button ![](../edpsgui/figures/configure_dataset.jpg) close to each dataset configuration.
See [here](configure_reduction.md) for more information.

## Generate Master Bias
This step is carried in the task **bias**, which runs the recipe  **xsh_mbias**.

Produces a master bias for UVB/VIS arms.
NIR frames do not use bias frames.

Customization:
- Choose stacking method (average, median).
- Adjust sigma-clipping parameters.

## Generate Master Dark
his step is carried in the task **dark**, which runs the recipe  **xsh_mdark**.


Produces a master dark.
Optional for UVB/VIS (dark current negligible).
For NIR it is only needed for stare observations; 
generally not used in nodding/offset where ON–OFF subtraction removes the dark. 

Customization:
- You can omit darks entirely for UVB/VIS and for NIR nod/offset.
- Change `stack-method` and `klow` / `khigh` thresholds to adjust stacking behaviour, e.g. for better cosmic-ray rejection.

## Instrument Model Prediction

Recipe: `xsh_predict`

Uses the instrument physical model and information about 
ambient conditions during the observations 
(e.g. atmospheric  pressure, temperature, instrument setting)
to predict line positions and a first dispersion solution.

Customization:
- Select between physical-model (recommended) and polynomial mode.
The physical model is recommended and should be used by default.
If the reduction fails or the optical model appears inconsistent, the polynomial mode can be enabled for troubleshooting or as an alternative.

## Order Tracing (Determining Order Geometry)

Recipe: `xsh_orderpos`

Uses pinhole order-definition frames (ORDERDEF_*) 
to trace the location and curvature of each echelle order on the detector. 
Produces order tables that later help rectification and wavelength calibration.

Customization:
- Tuning of detection thresholds can help when continuum levels are low or orders are partially vignetted.

## Generate Master Flat

Recipe: `xsh_mflat`

Produces a master flat,
refined version of the table from `xsh_orderpos`
and a bad pixel map for each arm. 
The flat defines the detector response and 
updates the true geometry of the orders from slit illumination.

Customization:
- Adjust bad-pixel handling (via `decode-bp`) if master flats saturate or raise quality control errors.

## 2D Mapping

Recipe: `xsh_2dmap`

Determines the two-dimensional wavelength solution needed to resample the orders.
Creates `WAVE_TAB_2D_ARM`, 
which provides a full mapping from detector coordinates to wavelength+slit coordinates, 
and `SPECTRAL_FORMAT_TAB_ARM`,
which defines, for each order, the wavelength range, pixel boundaries, predicted order edge traces,
and spatial-to-spectral coordinate conversion.

Customization:
- Select between physical-model (recommended) and polynomial mode.
- Adjust line-detection thresholds for weak arcs via `detectarclines-fit-win-hsize` and `detectarclines-search-win-hsize`. 
These parameters have to be small enough not to include a doublet but large
enough to be able to detect and fit the line.

## Wavelength Calibration

Recipe: `xsh_wavecal`

Computes arc lines tilt and resolving power.

Customization:
- Select between physical-model (recommended) and polynomial mode.

## Flexure Compensation

Recipe: `xsh_flexcomp`

Refines the wavelength solution to account for flexure, 
especially when arcs are not taken at the same rotator angle as science.

Customization:
- Select between physical-model (recommended) and polynomial mode.

## Instrument Response and Efficiency

Recipes: `xsh_respon_slit_stare`, `xsh_respon_slit_offset` and `xsh_respon_slit_nod`

Use standard stars to derive the per-order and merged instrument response 
(mapping detector counts to physical flux),
the blaze correction and the telescope + instrument + detector efficiency.
Used for flux calibration of science exposures.

## Science Reduction

Recipes: `xsh_scired_slit_stare`, `xsh_scired_slit_offset` and `xsh_scired_slit_nod`

Perform the data reduction: 
- Prepare the science frame (bias/dark/inter-order background correction, flat-fielding).
- Rectify orders using the model and wavelength solution.
- Perform sky subtraction (mode-dependent).
- Localize the object and extract `ORDER1D` and `MERGE1D` products.

When several exposures are fed together, 
the recipes stack them (mean/median) before extraction, 
and you get one combined 2D and 1D spectrum per run, not one per exposure.
To obtain one spectrum per exposure (or per AB pair in nodding), 
you must run `xsh_scired_slit_*` separately on each exposure or nod pair.

Customization:
- Select between physical-model (recommended) and polynomial mode.
- Use Active Flexure Correction (AFC) tables (`ORDER_TAB_AFC_`, `DISP_TAB_AFC_`) instead of the non-AFC ones, when available.
- Change `stack-method` and `klow` / `khigh` thresholds to adjust stacking behaviour.
- Sky modelling: In the NIR, `BSPLINE2` provides the best residuals,
`BSPLINE1` is faster and acceptable for UVB/VIS, 
and `MEDIAN` is the fatest but may leave residuals.
- Sky region selection:
use parameters `sky-position1`, `sky-hheight1`, `sky-position2`, and `sky-hheight2` to manually select sky zones.
Required when object not centered, multiple objects on slit, or strong NIR gradient.
- Spectroscopic extraction:
Standard extraction 
(`localize-method`=MANUAL)
recommended for faint sources.
Automatic detection
(`localize-method`=AUTO)
is usually fine for bright sources.

---
Go to XSHOOTER EDPS tutorial [index](../xshooter/index)