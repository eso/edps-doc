# Overview of all the data reduction configuration options <a name="configuration"></a>

## Selection of most appropriate calibrations

```{include} ../common/appropriate_calibrations.md
```

## Configuration of parameters: the configuration editor
```{include} ../common/configure_reduction.md
```
## Quality reports
```{include} ../common/quality_plots.md
```


## Troubleshooting

This section provides guidance for diagnosing and resolving common issues encountered during the SPHERE-ZIMPOL data-reduction cascade.

### Image Incorrectly Rotated / Signal Smeared out </a>

The task **zimpol_coronagraph_center_imaging** uses the instrument pipeline recipe `sph_zpl_star_center_img` 
to identify waffle spots and determine the position of the target behind the coronagraph. 
In some cases the detection threshold of 10σ is too high and the recipe cannot identify
the target’s position. In such a case `sph_zpl_science_imaging` will rotate the frames around an
incorrect position which will smear out the signal. If you see such behaviour you may try to reduce
`star_center_img.sigma` to 5.

 ---
Go to [top](#configuration)

 ---
Go to SPHERE EDPS tutorial [index](../sphere-zimpol/index)