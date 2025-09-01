<a name="top"></a>

# Reducing demo data

Follow this procedure to quickly reduce MUSE demo data. We assume that the `EDPS` Graphic User Interface and the MUSE
pipeline and the demo data are installed in your system. For general instructions on how to install `EDPS` and the
pipeline, please
visit [https://www.eso.org/sci/software/pipe_aem_main.html](https://www.eso.org/sci/software/pipe_aem_main.html).

## 1. Setting the workflow
```{include} ../common/reducing_demo_1.md
```
c. Choose the `MUSE` pipeline from the list in the `workflows` field. The workflows offered in this selector depend on the installed pipelines.
The graphic workflow representation will appear as in
   {numref}`fig-wkf` under the 'Workflow' tab.

```{figure} figures/select_muse_workflow.jpg
:alt: wkf
:name: fig-wkf

The EDPS Dashboard (Graphic User Interface) with the MUSE workflow loaded.	
```
## 2. Selecting the input data

```{include} ../common/reducing_demo_2.md
```

%3. Select the `Raw Data` tab to load the data to be reduced. By default, the workflow already points to the demo
%   datasets. Press `Create Datasets` to create the datasets. Select the datasets to reduce and send them to the
%  processing queue by clicking on the button `Send to Processing Queue` (see {numref}`fig-datasets` below). The content
%   of each dataset can be inspected by pressing the ![](figures/inspect.jpg) icon at the end of each dataset row (
%   see [example](figures/muse_dataset_example.jpg)).
%
%```{figure} figures/muse_datasets.jpg
%:alt: datasets
%:name: fig-datasets
%
%The Creation of MUSE datasets.	
%```  
%
%4. Select the `Processing Queue` tab (see {numref}`fig-queue`). The reduction of each dataset can be configured by
%   pressing the icon  ![](figures/configure_dataset.jpg) at the end of each dataset row. To start the reduction, press
%   the  ![](figures/start_reduction_all.jpg) button. The possible configuration options for MUSE data reduction are
%   described in Section [Configuration](configure_reduction).
%
%```{figure} figures/muse_queue.jpg
%:alt: datasets
%:name: fig-queue
%
%The Creation of MUSE datasets.	
%```

---
Go to [top](#top)


---
Go to MUSE EDPS tutorial [index](../muse/index)