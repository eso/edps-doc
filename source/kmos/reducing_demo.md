<a name="top"></a>

# Reducing demo data

Follow this procedure to quickly reduce KMOS demo data. We assume that the `EDPS` Graphic User Interface and the KMOS
pipeline and the demo data are installed in your system. For general instructions on how to install `EDPS` and the
pipeline, please
visit [https://www.eso.org/sci/software/pipe_aem_main.html](https://www.eso.org/sci/software/pipe_aem_main.html).

## 1. Setting the workflow

```{include} ../common/reducing_demo_1.md
```

c. Choose the desired workflow pipeline from the list in the `workflows` field. The workflows offered in this selector depend on
the installed pipelines.


The graphic workflow representation will appear as in
{numref}`kmos-fig-wkf`.

```{figure} figures/select_workflow.jpg
:alt: kmos-wkf
:name: kmos-fig-wkf

The EDPS Dashboard (Graphic User Interface) with the KMOS workflow loaded
```

## 2. Selecting the input data

```{include} ../common/reducing_demo_2.md
```

c. (Optional). Select the reduction target, configure the workflow parameter and specify the association preferences. 
Thise steps are optional. For more information see [here](configure_dataset_.md).

```{include} ../common/reducing_demo_3.md
```
---
Go to [top](#top)

## 4. Final products

By default, EDPS saves all the recipe products for all the executions in the directory specified at the first execution (
default: `$HOME/EDPS_data`).
However, it is possible to save only the final products into a desired location. This can be achieved by exporting
archived data reduction: press the `Export` button in the `Archived Data` tab
(see [here](../edpsgui/gui.md#archived_data)).

To archive a data reduction, press
the button `Archive` in the `Reduction Queue` tab (see [here](../edpsgui/gui.md#processing_queue))

Products are organized by `DATASET` (named as the first scientific exposure of the dataset), and `TIMESTAMP` (time of
start of reduction)

The final products saved in the specified directory are:
- One combined data cube for each object in the dataset, coming in two different formats as
  `COMBINED_CUBE` and `IDP_COMBINED_CUBE`. Both products have the same data content. 
  The latter file has the needed metadata information for ingestion into the ESO archive.
- A field-of-view image `COMBINED_IMAGE` and an exposure mask image `EXP_MASK` for each object.

## 5. Quality plots

```{include} ../common/quality_plots.md
```


---
Go to [top](#top)

---
Go to KMOS EDPS tutorial [index](../kmos/index)