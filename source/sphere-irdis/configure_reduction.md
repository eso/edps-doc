# Customizing the data reduction  <a name="configuration"></a>

## Selection of most appropriate calibrations

```{include} ../common/appropriate_calibrations.md
```

## Quality reports
```{include} ../common/quality_plots.md
```

## Configuration of parameters
```{include} ../common/configure_reduction.md
```

## Configuration and troubleshooting <a name="troubleshooting"> </a>

This section provides guidance on configuring the reduction, 
as well as diagnosing and resolving common issues encountered 
during the SPHERE-IRDIS data-reduction cascade.

### Dark regions in the background <a name="dark-reg"> </a>

{numref}`fig-bkg` shows an example of dark regions appearing in the products of the imaging workflow. These features are caused by astrophysical sources present in the SKY frames used for background subtraction.  

If SKY frames are not provided to the pipeline, dark frames are used instead for the background correction, which removes this pattern.

```{figure} figures/bad_background.jpg
:alt: wkf
:name: fig-bkg

Dark regions in the final image product for `SPHER.2015-12-19T02:24:25.758_tpl` (DPI).
```

### Fine tuning the instrument flat <a name="ins_flat"> </a>

The recipe `sph_ird_instrument_flat` is executed using modified bad-pixel rejection thresholds. 
Instead of the default values of 0.1 and 10 for `ird.instrument_flat.badpix_lowtolerance` 
and `ird.instrument_flat.badpix_uptolerance`, respectively, values of 0.75 and 1.25 are adopted. 

For K-band data, the [High Contrast Data Center](https://hc-dc.cnrs.fr/) 
recommends increasing `ird.instrument_flat.badpix_uptolerance` to 1.5.

### Distortion map are not used by default <a name="distortion_map"> </a>

The pipeline recipe `sph_ird_distortion_map` determines the geometric distortion 
of IRDIS data using internal calibration observations obtained with a pinhole mask. 
The recipe can also measure the relative offset between the LEFT and RIGHT detector 
images when the workflow parameter `force_distortion_correction` is enabled.

In practice, distortion solutions derived from internal calibration data 
have been found to be insufficiently robust for routine processing. 
Calibration sequences acquired close in time may produce 
noticeably different distortion solutions, 
including variations in the derived geometric mapping. 
When applied to science or astrometric observations, 
these solutions generally do not improve the calibration 
beyond what is achieved using a simple anamorphism correction alone, 
and in some cases may even degrade the data.

For this reason, processing of internal distortion calibrations 
is disabled by default in the standard IRDIS workflow. 
If required, the distortion map computation can be enabled manually by 
changing workflow parameter `force_distortion_correction` = `TRUE`.

A more robust approach is to correct only the dominant distortion component, 
which is a stable anamorphism of approximately 0.6%. 
This can be applied in a simple and reproducible manner by 
rescaling the detector coordinates, multiplying the X and Y axes 
by factors of 1.0059 and 1.0011, respectively.

### Waffle spots cannot be detected <a name="img_coro"> </a>

In task **irdis_coronagraph_center**, the recipe `sph_ird_star_center` 
may require parameter adjustments depending on the observing setup.

For K-band data, the detection of waffle spots can be challenging 
due to the high thermal background.  
Increasing `ird.star_center.sigma` to 100 may improve the detection. 
Alternatively, the background can be removed manually prior to running the recipe.

The default parameters are optimized for detecting waffle spots in coronagraphic observations.  
For data acquired without a coronagraph, the following parameters should be modified:

- `ird.star_center.use_waffle` = `FALSE`,
- `ird.star_center.sigma` = `500` (the stellar PSF is typically very bright in this configuration).

### Angular Differential Imaging and Spectral Differential Imaging <a name="highcontrast"> </a>

The recipe `sph_ird_science_dbi` runs with both ADI and SDI disabled by default.  
If SDI processing is enabled, the Data Centre (DC) recommends setting
`ird.science_dbi.minr` and `ird.science_dbi.maxr` to 20 and 70, respectively,
instead of the default values of 4 and 40.

These values are calibrated for a wavelength of λ = 1.6 µm and should be scaled
linearly with wavelength for other observing bands.

### Getting additional data products <a name="img_prod"> </a>

The recipe `sph_ird_science_dbi` is used to process both Classical Imaging (CI) 
nd Dual-Band Imaging (DBI) data. 
The workflow is configured to save stacked products for each detector arm 
(`ird.science_dbi.save_addprod` = `TRUE`) while intermediate products 
are not retained by default.

To generate and preserve all intermediate products that may be useful for further analysis,
set the recipe parameter `ird.science_dbi.save_interprod` = `TRUE`.



 ---
Go to [top](#configuration)

 ---
Go to SPHERE-IRDIS EDPS tutorial [index](../sphere-irdis/index)