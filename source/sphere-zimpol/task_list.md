# List of workflow tasks

This is the list of all the tasks and associated recipes in the SPHERE-ZIMPOL workflow. 
Only some of them are needed for scientific reduction, they are indicated by the flag "yes" (triggered by default) or "optional" (triggered only if requested
by a workflow parameter). Other tasks are not used for scientific reduction (they are indicated by the flag "no"), they are mainly used
for instrument monitoring and they can be executed only by specifying them as target. Note that, when a task is specified as target, all the 
tasks that generate the calibrations needed for it are automatically executed.

| TASK                                              | 	RECIPE               | Used in  <br/>  science reduction | 	Notes                                                                                             |
|---------------------------------------------------|-----------------------|-----------------------------------|----------------------------------------------------------------------------------------------------|
| zimpol_bias_imaging | sph_zpl_master_bias_imaging | no | Creates the imaging master bias for both cameras; mainly used for detector monitoring and standard-star reductions. |
| zimpol_dark_imaging | sph_zpl_master_dark_imaging | yes | Produces the imaging master dark calibration for both cameras. |
| zimpol_flat_imaging_cam1 | sph_zpl_intensity_flat_imaging | optional | Generates the imaging intensity flat-field calibration for camera 1. |
| zimpol_flat_imaging_cam2 | sph_zpl_intensity_flat_imaging | optional | Generates the imaging intensity flat-field calibration for camera 2. |
| zimpol_standard_astrometry_imaging | sph_zpl_science_imaging | optional | Reduces astrometric standard-field observations for calibration monitoring. |
| zimpol_standard_flux_imaging | sph_zpl_science_imaging | no | Reduces photometric standard-star observations for zeropoint monitoring. |
| zimpol_coronagraph_center_imaging | sph_zpl_star_center_img | yes | Determines the stellar position behind the coronagraph for centering and rotation-center definition. |
| zimpol_science_flux_imaging | sph_zpl_science_imaging | optional | Reduces off-axis flux frames associated with imaging science observations. |
| zimpol_science_imaging | sph_zpl_science_imaging | yes | Main ZIMPOL imaging science reduction task. |
| zimpol_bias_polarimetry | sph_zpl_master_bias | no | Creates the polarimetric master bias for both cameras. Used mainly for FastPolarimetry monitoring. |
| zimpol_dark_polarimetry | sph_zpl_master_dark | optional | Produces the polarimetric master dark for both cameras. |
| zimpol_flat_polarimetry_qc | sph_zpl_intensity_flat | no | Produces polarimetric intensity-flat products for QC and monitoring only. |
| zimpol_flat_polarimetry_cam1 | sph_zpl_intensity_flat | optional | Generates the polarimetric intensity flat for camera 1. |
| zimpol_flat_polarimetry_cam2 | sph_zpl_intensity_flat | optional | Generates the polarimetric intensity flat for camera 2. |
| zimpol_modem_efficiency_qc | sph_zpl_modem_efficiency | no | Computes modulation/demodulation efficiency products for QC and monitoring only. |
| zimpol_modem_efficiency_cam1 | sph_zpl_modem_efficiency | optional | Generates the modulation/demodulation efficiency calibration for camera 1. |
| zimpol_modem_efficiency_cam2 | sph_zpl_modem_efficiency | optional | Generates the modulation/demodulation efficiency calibration for camera 2. |
| zimpol_standard_polarimetry_unpolarized | sph_zpl_science_p1 | no | Reduces unpolarized standard stars to monitor instrumental polarization. |
| zimpol_standard_polarimetry_polarized | sph_zpl_science_p1 | no | Reduces highly polarized standard stars to monitor polarization angle and polarization-level offsets. |
| zimpol_coronagraph_center_polarimetry | sph_zpl_star_center_pol | yes | Determines the stellar position behind the coronagraph for polarimetric observations. |
| zimpol_science_flux_p1 | sph_zpl_science_p1 | optional | Reduces off-axis flux frames for polarimetric science observations taken in mode P1. |
| zimpol_science_p1 | sph_zpl_science_p1 | yes | Main polarimetric science reduction for observations taken in mode P1. |
| zimpol_science_flux_p2 | sph_zpl_science_p23 | optional | Reduces off-axis flux frames for polarimetric science observations taken in mode P2. |
| zimpol_science_p2 | sph_zpl_science_p23 | yes | Main polarimetric science reduction for observations taken in mode P2. |

**Notes**

- In polarimetry, the **bias** is associated only in **FastPolarimetry**, while the **dark** is associated only for **SlowPolarimetry exposures with EXPTIME > 30 s**.
- Modulation–demodulation efficiency calibrations are matched differently depending on whether they are used for **calibration**, **flux/center**, or **science** observations.
