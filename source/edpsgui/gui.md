<a name="top"></a>

# The EDPS dashboard

To install the EDP dashboard (a.k.a. EDPS-GUI), please follow the instructions 
given  [here](../quick/installation.md#installation). To launch the dashboard, type:

	. <path-to-environment>/bin/activate 
	edps-gui

The `<path-to-environment>` is the full-path-name of the virtual environment defined during the installation [procedure](../quick/installation.md#installation-steps).

The EDPS dashboard is then loaded on a browser window {numref}`fig-gui`. To start EDPS, press the
Start EDPS green button at the top of the window. To stop EDPS,
press the Stop EDPS red button and press `Ctrl-c` on the terminal
where the `edps-gui` command was launched.

At the top of the Dashboard, close to the Start/Stop EDPS button there is the **Workflow** selection menu, which allows to load the desired workflow. The available workflows depend on the
pipelines installed in your system.

```{figure} figures/gui.jpg
:alt: gui
:name: fig-gui
:figclass: left-caption

The EDPS dashboard (Graphic User Interface). At this stage, EDPS
has not been started yet and no workflow has been selected.

```

The "Help" drop-down menu contains version information, reference, and the **Settings** menu, which allows to configure several EDPS behaviors, such as
links to data-storage directories, and the parallelization. 
It is described in detail in Section [**Settings**](#settings). Note that it is possible to change the settings 
only if EDPS has not been started yet.

There are 4 tabs in the main dashboard window, they are:

- **Workflow**. It gives information on the workflow, the graphic
  layout, a description of the type of data and access to the workflow
  code. It is described in detail in Section [The **Workflow** tab](#workflow).

- **Raw Data**. It allows to specify the input data, the preferences
  for association calibrations, and to create datasets to be reduced. It
  is described in Section [The **Raw Data** tab](#raw_data)


- **Reduction Queue**. It starts the data reduction. It is described in
  Section [The **Reduction Queue** tab](#reduction_queue)

- **Reduction Archive**. It gives access to previously archived data
  reduction and final products. It is described in Section [The **Reduction Archive** tab](#reduction_archive)


At the bottom of the dashboard, the graphic representation of the
selected workflow is visible.
% {numref}`fig-workflow-tab` shows the EDPS dashboard with the FORS spectroscopic workflow loaded.


<a name="settings"></a>
## Settings. 

```{include} settings_.md
```

---
Go to [top](#top)

Go to EDPS-GUI documentation [index](../edpsgui/index)

<a name="workflow"></a>

## The **Workflow** tab.
t.b.d.

%```{include} workflow_.md
%```
---
Go to [top](#top)

Go to the EDPS-GUI documentation [index](../edpsgui/index)

<a name="raw_data"></a>
## The **Raw Data** tab.

t.b.d.

%```{include} raw_data_.md
%```

---
Go to [top](#top)

Go to the EDPS-GUI documentation [index](../edpsgui/index)

<a name="reduction_queue"></a>
## The **Reduction Queue** tab.

t.b.d.

%```{include} reduction_queue_.md
%```

---
Go to [top](#top)

Go to the EDPS-GUI documentation [index](../edpsgui/index)


<a name="reduction_archive"></a>
## The **Reduction Archive** tab.

t.b.d.

---
Go to [top](#top)

Go to the EDPS-GUI documentation [index](../edpsgui/index)

