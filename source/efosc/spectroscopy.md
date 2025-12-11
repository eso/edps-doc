<a name="top"></a>

# EFOS spectriscipic workflow

## Reducing spectroscopic data

Follow this procedure to quickly reduce EFOSC spectroscopic demo data. We assume that the `EDPS` Graphic User Interface and the EFOSC
pipeline and the demo data are installed in your system. For general instructions on how to install `EDPS` and the
pipeline, please
visit [https://www.eso.org/sci/software/pipe_aem_main.html](https://www.eso.org/sci/software/pipe_aem_main.html).

### 1. Setting the workflow

```{include} ../common/reducing_demo_1.md
```

c. Choose the desired workflow pipeline from the list in the `workflows` field. The workflows offered in this selector depend on
the installed pipelines. To reduce EFOSC spectroscopic data, select the workflow efosc_spectroscopy_wkf.

The graphic workflow representation will appear as in
{numref}`fig-wkf_spc`.

```{figure} figures/select_workflow_spc.jpg
:alt: wkf_spc
:name: fig-wkf_spc

**The EFOSC spectroscopic workflow selection procedure.**	
```

### 2. Selecting the input data

```{include} reducing_demo_2_spc.md
```

---
Go to [top](#top)

### 4. Final products

By default, EDPS saves all the recipe products for all the executions in the directory specified at the first execution (
default: `$HOME/EDPS_data`).
However, it is possible to save only the final products into a desired location. This can be achieved by exporting
archieved data reduction: press the `Export` button in the `Archieved Data` tab
(see [here](../edpsgui/gui.md#archived_data)).

To archieve a data reduction, press
the button `Archive` in the `Reduction Queue` tab (see [here](../edpsgui/gui.md#processing_queue))

Products are organized by `TARGET NAME` (the name of the object, as recorded in the header of the raw fits file) `DATASET` (named as the raw fits file), and `TIMESTAMP` (time of
start of reduction)

The final products saved in the specified directory are:

 - SPECTRUM_MOS_<arcfile>. Two dimensional spectrum, where in each raw there is the extracted and 
   reduced spectrum of a slit.

The variable arcfile is taken from the fits header, and it is the name of the raw science image.
 

---
Go to [top](#top)

---
Go to EFOSC EDPS tutorial [index](../efosc/index)