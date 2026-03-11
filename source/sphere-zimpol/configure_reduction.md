# Overview of all the data reduction configuration options <a name="configuration"></a>

## Selection of most appropriate calibrations

```{include} ../common/appropriate_calibrations.md
```

## Quality reports
```{include} ../common/quality_plots.md
```

## Configuration of parameters: the configuration editor
```{include} ../common/configure_reduction.md
```


## Troubleshooting

This section provides guidance for diagnosing and resolving common issues encountered during the SPHERE-ZIMPOL data-reduction cascade.

### Vertical pairs of bright and dark pixels

For long exposure times (DET.DIT1 > 50 s), charge traps may appear in the ZIMPOL detector. 
Those are defects in the CCD lattice that temporarily capture electrons during the charge transfer 
and release them with a time delay, producing vertical pairs of dark and bright pixels. See Figure {numref}`fig-charges` as an example.

Small errors in the charge transfer accumulate over time. The effect can appear at shorter exposure times in FastPolarimetry mode and may also be present in calibration frames such as `FLAT,LAMP` or `FLAT,POL100`.

```{figure} figures/charge_traps.jpg
:alt: charge traps
:name: fig-charges

Vertical pairs of bright and dark pixels marked in cyan caused by charge traps in the ZIMPOL detector.
```

### Image Incorrectly Rotated / Signal Smeared out </a>

The task **zimpol_coronagraph_center_imaging** uses the instrument pipeline recipe `sph_zpl_star_center_img` 
to identify waffle spots and determine the position of the target behind the coronagraph. 
In some cases the detection threshold of 10σ is too high and the recipe cannot identify
the target’s position. In such a case the science recipe (`sph_zpl_science_imaging`, `sph_zpl_science_p?`)
will rotate the frames around an incorrect position which will smear out the signal. 
If you see such behaviour you may try to reduce `star_center_img.sigma` to 5.

 ---
Go to [top](#configuration)

 ---
Go to SPHERE EDPS tutorial [index](../sphere-zimpol/index)