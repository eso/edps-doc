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

## Bad Pixels <a name="first_step"> </a>

```{comment}
The pipeline performs by default standard extraction between ± 2.0 arcsec 
(controlled by `localize-slit-hheight`) 
around the centre of the slit 
(controlled by `localize-slit-position`). 
Flagged pixels falling outside the extraction region 
do not affect the standard extraction algorithm. 
Flagged pixel falling inside the extraction region
are interpolated during the standard extraction algorithm
by constructing a local spatial profile. 
The local spatial profile uses a number of points 
(controlled by `stdextract-interp-hsize`)
at a certain distance from the wavelength for which interpolation is required.
```

 ---
Go to [top](#configuration)


## Zero flux values? Check the cosmic-ray rejection <a name="second_step"> </a>

Large regions of zero-flux values in the final extracted 1D spectrum
may be caused by spurious Cosmic-Ray (CR) detections. 
See {numref}`fig-cr` as an example of affected spectrum.

CR-contaminated pixels are identified using the van Dokkum algorithm 
([2001, PASP, 113, 1420](https://scixplorer.org/abs/2001PASP..113.1420V/abstract)) 
applied to the input science frames.
The detection threshold is controlled by the parameter
`removecrhsingle-sigmalim`, whose default value is 5.0 for the UVB and VIS arms.
For the NIR arm, CR detection is disabled by default by setting
`removecrhsingle-niter` to 0.

In observations obtained under excellent seeing conditions (≈0.4″ or better),
the stellar PSF may appear sharp enough to be mistakenly flagged as CR-affected.
To reduce these false detections, increase the value of
`removecrhsingle-sigmalim`.
Figure {numref}`fig-cr2` illustrates the improvement obtained on the same observation.

```{figure} figures/CR_detections_bad.jpg
:alt: cr
:name: fig-cr

Here we show the VIS spectrum of the telluric standard star Hip089684,
as displayed in the `Graphical reports`.
The observation was obtained on May 1, 2023
(OB identifier: `XSHOO.2023-05-02T07:37:22.135`)
under excellent seeing conditions (0.4″).
With the default value `removecrhsingle-sigmalim`=5.0,
the algorithm produces spurious cosmic-ray detections,
which in turn lead to extended wavelength intervals with zero flux
in the extracted 1D spectrum.
```

```{figure} figures/CR_detections_good.jpg
:alt: cr
:name: fig-cr2

Same as {numref}`fig-cr`, but with `removecrhsingle-sigmalim`=7.0.
In this case, this avoids the flagging of good pixels as CR-affected.
```

 ---
Go to [top](#configuration)


## Third step <a name="third_step"> </a>

Describe parameters here and what to do in case of bad results


 ---
Go to [top](#configuration)

 ---
Go to XSHOOTER EDPS tutorial [index](../xshooter/index)