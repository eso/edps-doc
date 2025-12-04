<a name="top"></a>

# Reducing demo data

Follow this procedure to quickly reduce XSHOOTER demo data. We assume that the `EDPS` Graphic User Interface, the XSHOOTER
pipeline and the demo data are installed in your system. For general instructions on how to install `EDPS` and the
pipeline, please
visit [https://www.eso.org/sci/software/pipe_aem_main.html](https://www.eso.org/sci/software/pipe_aem_main.html).

## 1. Setting the workflow

```{include} ../common/reducing_demo_1.md
```

c. Choose the `XSHOOTER` pipeline from the list in the `workflows` field. The workflows offered in this selector depend on
the installed pipelines.

The graphic workflow representation will appear as in
{numref}`fig-wkf`.

```{figure} figures/select_workflow_xsh2.jpg
:alt: wkf
:name: fig-wkf

The EDPS Dashboard (Graphic User Interface) with the XSHOOTER workflow loaded.	
```

## 2. Selecting the input data

```{include} ../common/reducing_demo_2.md
```

---
Go to [top](#top)

## 4. Final products

By default, EDPS saves all the recipe products for all the executions in the directory specified at the first execution (default: `$HOME/EDPS_data`).
However, it is possible to save only the final products into a desired location. This can be achieved by exporting
archived data reduction: press the `Export` button in the `Archived Data` tab
(see [here](../edpsgui/gui.md#archived_data)).

To archive a data reduction, press
the button `Archive` in the `Reduction Queue` tab (see [here](../edpsgui/gui.md#processing_queue))

The exported products are organized by TARGET_NAME (as read from the header), DATASET (named as the first scientific exposure of the dataset), and `TIMESTAMP` (time of
start of reduction)

The final products saved in the specified directory are:

- The 1D spectrum, telluric corrected, obtained from the combination of individual exposures. Its name format
is: SPECTRUM_COMBINED_<target_name>, where target name is read from the header.
- The individual 1D spectra prior to combination (either telluric corrected or not). They are in a subdirectory 
of the combined spectrum they refer to
their name formats are SPECTRUM_\<arm\>\_\<arcfile\> or SPECTRUM_TELLCORR_\<arm\>\_\<arcfile\> if telluric corrected. 
The values of arm (UVB, VIS, NIR) and arcfile (the file name of the raw science exposure) are read from the file header.
- The datacubes obtained from individual exposures for IFU observations. Its name format is: 
- DATACUBE_\<arm\>\_\<arcfile\>.

This applies to all slit modes (stare, offset, and nod) and ifu mode.

Other useful products cam be found in the EDPS_data directory, where all intermediate products are saved.

## 5. Quality plots

Almost all processing tasks can display the input raw frames and the products in the so called "quality plots", which
can be inspected from the `Reduction Queue` window.
Those associated for the main product can be inspected by pressing the magnifying glass symbol at the right side of each dataset.
To inspect those associated to each individual job (if created), 

 - Expand the desired dataset by pressing the black arrow on its left. The list of jobs will appear with the associated status (COMPLETED, RUNNING, PENDING)
 - Press the  magnifying glass symbol at the right side of the job you want to inspect. Only plots for completed jobs can be inspected.


   ````{figure} figures/quality_plots.jpg
   :alt: reports
   :name: show_reports
   ```` 

---
Go to [top](#top)

---
Go to XSHOOTER EDPS tutorial [index](../xshooter/index)