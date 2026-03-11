
```{include} ../common/configure_dataset_.md
```

- As can be seen above, for SPHERE instruments (IFS, IRDIS, and ZIMPOL) the only available workflow parameter is `force_distortion_correction`.
However the processing of internal distortion calibrations is disabled in the workflow and these calibrations are currently used only for internal instrument monitoring.
Setting `force_distortion_correction = TRUE` does not enable distortion correction and will only cause EDPS to flag the dataset as incomplete if the required distortion calibration frames are not provided as inputs
(see [Section Configuration](../sphere-irdis/configure_reduction.md)).

---
Go to [top](#top)

---
Go to SPHERE-IRDIS EDPS tutorial [index](../sphere-irdis/index)