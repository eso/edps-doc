<a name="top"></a>

# Reducing demo data

Follow this procedure to quickly reduce MUSE demo data. We assume that the `EDPS` Graphic User Interface and the MUSE
pipeline and the demo data are installed in your system. For general instructions on how to install `EDPS` and the
pipeline, please
visit [https://www.eso.org/sci/software/pipe_aem_main.html](https://www.eso.org/sci/software/pipe_aem_main.html).

## 1. Setting the workflow

```{include} ../common/reducing_demo_1.md
```

d. Choose the FORS SPECTROSCOPIC pipeline from the list in the `workflows` field. The workflows offered in this selector depend on
the installed pipelines.
The graphic workflow representation will appear as in
{numref}`fig-wkf`.

```{figure} figures/select_workflow.jpg
:alt: wkf
:name: fig-wkf

Add caption	
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

By default, EDPS saves all the recipe products for all the executions in the directory specified a the first execution (
default: `$HOME/EDPS_data`).
However, it is possible to save only the final products into a desired location. This can be achieved by exporting
archieved data reduction: press the `Export` button in the `Archieved Data` tab
(see [here](the-reduction-archive-tab.md), or consult the [Frequently Asked Questions](faq.md) ).

To archive a data reduction, press the button `Archive` in the `Reduction Queue` tab.

Products are organized by `DATASET` (named as the first scientific exposure of the dataset), and `TIMESTAMP` (time of
start of reduction)

The final products saved in the specified directory are:

**DESCRIBE THE FINAL PRODUCTS (see parameters.yaml to check what are the categories that
are exported and their name convention)**

Additionally, if specified by the reduction target, also products
of sky exposures (treated as regular science exposures) are saved. They product names have the same convention as
regular science exposures.

## 5. Quality plots

```{include} ../common/quality_plots.md
```


---
Go to [top](#top)

---
Go to FORS SPEC EDPS tutorial [index](../fors_spec/index)