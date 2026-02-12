# Overview of all the data reduction configuration options  <a name="configuration"></a>

## Selection of most appropriate calibrations

```{include} ../common/appropriate_calibrations.md
```


## Configuration of parameters
```{include} ../common/configure_reduction.md
```

## Wavelength calibration <a name="wavelength_calibration"> </a>

The interactive window for the wavelength calibration step (task **arc**) shows the 
reconstructed arc frames for each of
the three detectors at one of the six rotator position angles. 
Other rotator angles (either 0, 60, 120, 180, 240, or 300 degrees) can be chosen with the
`Select Angle` menu. The
output file with the reconstructed arc frames has 18 extensions (3 extensions per detector, times 6 angles).
Exposures at different angles are taken in order to account for instrument flexures. When applying the wavelength
correction to a dataset, the KMOS pipeline automatically selects the calibration with the closest angle. 

The KMOS wavelength calibration uses Argon and Neon arc lines. 
There is normally no need to fine tune the wavelength calibration result. 
Since the Argon lines are less numerous and
less bright than the Neon ones, the fit to the line positions is dominated by the Neon lines and
the average offset of the Argon lines is larger than the ones of the Neon lines. This can be checked with the
QC ARC AR POS MEAN and QC ARC NE POS MEAN header keywords in the product file extensions. Their values are
less than the uncertainties. The effect could be mitigated by increasing the recipe parameter `order` to 7.
The parameter determines the order of the fit polynomial.
With its default value of 0, the applied order is 6 for the H, K, and YJ grisms, 4 for the IZ grism, and
5 for the HK grism. 


[## Illumination correction <a name="illumination_correction"> </a>]:#

[Describe parameters here and what to do in case of bad results]:#


[## Second step <a name="second_step"> </a>]:#


[Describe parameters here and what to do in case of bad results]:#



 ---
Go to [top](#configuration)

 ---
Go to KMOS EDPS tutorial [index](../kmos/index)