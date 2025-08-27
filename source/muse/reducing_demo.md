<a name="top"></a>
# Reducing demo data

Follow this procedure to quickly reduce MUSE demo data. We assume that the EDPS Graphic User Interface and the MUSE pipeline and the demo data are installed in your system. For installation instructions and more general information, visit the [EDPS tutorial](https://www.eso.org/~lcoccato/EDPS/reducing_your_data.html).

1. Start the `EDPS` dashboard by typing:

		edps-gui			
	Press the Start button on the browser window that appears. 
	
2. Select the muse workflow from the dedicated `Workflow` field. The graphic workflow representation will appear as in {numref}`fig-wkf` under the 'Workflow' tab.


```{figure} figures/muse_load_wkf.jpg
:alt: wkf
:name: fig-wkf

The EDPS Dashboard (Graphic User Interface) with the MUSE workflow loaded.	
```

3. Select the `Raw Data` tab to load the data to be reduced. By default, the workflow already points to the demo datasets. Press `Create Datasets` to create the datasets. Select the datasets to reduce and send them to the processing queue by clicking on the button `Send to Processing Queue` (see {numref}`fig-datasets` below). The content of each dataset can be inspected by pressing the ![](figures/inspect.jpg) icon at the end of each dataset row (see [example](figures/muse_dataset_example.jpg)).


```{figure} figures/muse_datasets.jpg
:alt: datasets
:name: fig-datasets

The Creation of MUSE datasets.	
```  

4. Select the `Processing Queue` tab (see {numref}`fig-queue`). The reduction of each dataset can be configured by pressing the icon  ![](figures/configure_dataset.jpg) at the end of each dataset row. To start the reduction, press the  ![](figures/start_reduction_all.jpg) button. The possible configuration options for MUSE data reduction are described in Section [Configuration](configure_reduction).


```{figure} figures/muse_queue.jpg
:alt: datasets
:name: fig-queue

The Creation of MUSE datasets.	
```

---
Go to [top](#top)


---
Go to MUSE EDPS tutorial [index](../muse/index)