<a name="top"></a>

# Reducing demo data

Follow this procedure to quickly reduce FORS demo data. We assume that the `EDPS` Graphic User Interface and the FORS
pipeline and the demo data are installed in your system. For general instructions on how to install `EDPS` and the
pipeline, please
visit [https://www.eso.org/sci/software/pipe_aem_main.html](https://www.eso.org/sci/software/pipe_aem_main.html).

## 1. Setting the workflow

```{include} ../common/reducing_demo_1.md
```

c. Choose the desired workflow pipeline from the list in the `workflows` field. The workflows offered in this selector depend on
the installed pipelines.
The FORS pipeline comes with several workflow dedicated to the different instrument modes;
the general workflow `fors.fors_wkf` deals with data from all modes.

The graphic workflow representation will appear as in
{numref}`fig-wkf`.

```{figure} figures/select_workflow.jpg
:alt: wkf
:name: fig-wkf

**Insert caption here**	
```

## 2. Selecting the input data

```{include} ../common/reducing_demo_2.md
```

---
Go to [top](#top)

## 4. Final products

By default, EDPS saves all the recipe products for all the executions in the directory specified a the first execution (
default: `$HOME/EDPS_data`).
However, it is possible to save only the final products into a desired location. This can be achieved by exporting
archieved data reduction: press the `Export` button in the `Archieved Data` tab
(see [here](../edpsgui/gui.md#archived_data)).

To archieve a data reduction, press
the button `Archive` in the `Reduction Queue` tab (see [here](../edpsgui/gui.md#processing_queue))

Products are organized by `DATASET` (named as the first scientific exposure of the dataset), and `TIMESTAMP` (time of
start of reduction)

The final products saved in the specified directory are:

**Please desribe the main products of the reduction**

## 5. Quality plots

```{include} ../common/quality_plots.md
```


---
Go to [top](#top)

---
Go to FORS EDPS tutorial [index](../fors/index)