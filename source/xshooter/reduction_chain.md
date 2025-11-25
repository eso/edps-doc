# The XSHOOTER data reduction flow

The overall data flow of the XSHOOTER pipeline is displayed [here](figures/reduction_cascade.jpg).

The reduction cascade is organized in tasks, 
which represent well-defined steps in the process. 
Tasks can be grouped  inside sub-workflows. 
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
This is controlled by the `Select reduction target` option in the `Raw Data` tab.

The reduction steps are:

## Generate Master Bias

Recipe: `xsh_mbias`

Produces a master bias for UVB/VIS arms.
NIR frames do not use bias frames.

## Generate Master Dark

Recipe: `xsh_mdark`

Produces the Master Dark.
Optional for UVB/VIS (dark current negligible).
For NIR it is only needed for stare observations; 
generally not used in nodding/offset where ON–OFF subtraction removes the dark. 

Customization:
- You can omit darks entirely for UVB/VIS and for NIR nod/offset.
- Change `stack-method`, `klow`, `khigh` to adjust stacking behaviour (e.g. for better cosmic-ray rejection).

## Instrument Model Prediction

Recipe: `xsh_predict`

Uses the instrument physical model and information about 
ambient conditions during the observations 
(e.g. atmospheric  pressure, temperature, instrument setting)
to predict line positions and a first dispersion solution.

## Order Tracing (Determining Order Geometry)

Recipe: `xsh_orderpos`

Uses pinhole order-definition frames (ORDERDEF_*) 
to trace the location and curvature of each echelle order on the detector. 
Produces order tables that later help rectification and wavelength calibration.

Customization:
- Tuning of detection thresholds can help when continuum levels are low or orders are partially vignetted.

## Generate Master Flat

Recipe: `xsh_mflat`

Produces the Master Flat,
refined version of the table from `xsh_orderpos`
and a bad pixel map for each arm. 
The flat defines the detector response and 
updates the true geometry of the orders from slit illumination.

Customization:
- Adjust bad-pixel handling (via `decode-bp`) if master flats saturate or raise QC errors.

---
Go to XSHOOTER EDPS tutorial [index](../xshooter/index)