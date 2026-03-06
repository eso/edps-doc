<a name="top"></a>

# Reducing demo data

Follow this procedure to quickly reduce SPHERE-ZIMPOL demo data. 
We assume that the `EDPS` Graphic User Interface and the SPHERE
pipeline and the demo data are installed in your system. 
For general instructions on how to install `EDPS` and the
pipeline, please visit [https://www.eso.org/sci/software/pipe_aem_main.html](https://www.eso.org/sci/software/pipe_aem_main.html).

## 1. Setting the workflow

```{include} ../common/reducing_demo_1.md
```

d. Choose the desired workflow pipeline from the list in the `workflows` field. The workflows offered in this selector depend on
the installed pipelines.
The SPHERE pipeline comes with several workflow dedicated to the different instrument modes;
the general workflow `sphere.sphere_wkf` deals with data from all modes. Select `sphere.sphere_zimpol_wkf` 
to reduce ZIMPOL data.

The graphic workflow representation will appear as in
{numref}`fig-wkf-zimpol`.

```{figure} figures/select_workflow.jpg
:alt: wkf
:name: fig-wkf-zimpol

The EDPS Dashboard (Graphic User Interface) with the ZIMPOL workflow loaded.	
```

## 2. Selecting the input data

```{include} ../common/reducing_demo_2.md
```
c. (Optional). Select the reduction target, configure the workflow parameter and specify the association preferences. 
These steps are optional. For more information see [here](configure_dataset_.md).

```{include} ../common/reducing_demo_3.md
```
---
---
Go to [top](#top)

## 4. Final products

By default, EDPS saves all the recipe products for all the executions in the directory specified at the first execution (default: `$HOME/EDPS_data`).
However, it is possible to save only the final products into a desired location. This can be achieved by exporting
archived data reduction: press the `Export` button in the `Archived Data` tab
(see [here](../edpsgui/gui.md#archived_data)).

To archive a data reduction, press
the button `Archive` in the `Reduction Queue` tab (see [here](../edpsgui/gui.md#processing_queue)).

The exported products are organized by DATASET (named as the first scientific exposure of the dataset), and `TIMESTAMP` (time of
start of reduction).

In imaging mode, the final products saved in the specified directory are the reduced and combined images from the two ZIMPOL cameras, 
with name format `ZIMPOL_` followed by the observing mode (`IMAGE_`), camera number (`CAM1_` or `CAM2_`), 
and archive file name (corresponding to header keyword `ARCFILE`).
The file contains 8 extensions:
In addition to the combined science intensity image, additional extensions include a bad-pixel map, number-of-combined (ncomb) frames map, and RMS map; 
a combined dark-current image, with its own corresponding bad-pixel map, ncomb map, and RMS map.

In polarimetry mode, the final products saved in the specified directory are the reduced and combined Q and U Stoke parameter images 
from the two ZIMPOL cameras, with name format `ZIMPOL_` followed by the polarimetry mode (`POL1_` or `POL23_`), camera number (`CAM1_` or `CAM2_`)
and archive file name (corresponding to header keyword `ARCFILE`).
The file contains 8 extensions:
In addition to the combined science intensity image, additional extensions include a bad-pixel map, number-of-combined (ncomb) frames map, and RMS map; 
an image with the polarization component, with its own corresponding bad-pixel map, ncomb map, and RMS map.

Other useful products can be found in the EDPS_data directory, where all intermediate products are saved.

## 5. Quality plots

```{include} ../common/quality_plots.md
```


---
Go to [top](#top)

---
Go to SPHERE-ZIMPOL EDPS tutorial [index](../sphere-zimpol/index)