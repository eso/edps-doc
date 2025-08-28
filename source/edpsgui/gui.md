<a name="top"></a>

# The EDPS dashboard

Ectivate the `EDPS` python environment and press:

	. <path-to-environment>/bin/activate 
	edps-gui

The EDPS dashboard is then loaded on a browser window {numref}`fig-gui`. To start `EDPS`, press the
`Start EDPS` green button at the top of the window. To stop `EDPS`,
press the `Stop EDPS` red button and press `Ctrl-c` on the terminal
where the `edps-gui` command was launched.

At the top of the Dashboard, the `Workflow` selection menu allows to
load the desired workflow. The available workflows depend on the
pipelines installed in your system.

```{figure} figures/gui.jpg
:alt: gui
:name: fig-gui
:figclass: left-caption

The `EDPS` dashboard (Graphic User Interface). At this stage, `EDPS`
has not been started yet and no workflow has been selected.

```

There are 5 tabs in the main dashboard window, they are

- **`Workflow`**. It gives information on the workflow, the graphic
  layout, a description of the type of data and accesso the workflow
  code. It is described in detail in Section [The `Workflow` tab](#workflow).

- **`Raw Data`**. It allows to specify the input data, the preferences
  for association calibrations, and to create datasets to be reduced. It
  is described in Section [The `Raw Data` tab](#raw_data)


- **`Processing Queue`**. It starts the data reduction. It is described in
  Section [The `Processing Queue` tab](#processing_queue)

- **`Archived Data`**. It gives access to previously archived data
  reduction and final products. It is described in Section [The `Archived Data` tab](#archived_data)

- **`About EDPS`**. It provides some general information about
  `EDPS`.

At the bottom of the dashboard, the graphic representation of the
selected workflow is visible. {numref}`fig-gui` shows
the `EDPS` dashboard, with the FORS spectroscopic workflow loaded.

<a name="workflow"></a>

## The `Workflow` tab.

```{include} workflow_.md
```
---
Go to [top](#top)

Go to `edps-gui` documentation [index](../edpsgui/index)

<a name="raw_data"></a>
## The `Raw Data` tab.

```{include} raw_data_.md
```

---
Go to [top](#top)

Go to `edps-gui` manual [index](../edpsgui/index)

<a name="processing_queue"></a>
## The `Processing Queue` tab.

```{include} processing_queue_.md
```

---
Go to [top](#top)

Go to `edps-gui` manual [index](../edpsgui/index)


<a name="archived_data"></a>
## The `Archived Data` tab.

blabla

---
Go to [top](#top)

Go to `edps-gui` documentation [index](../edpsgui/index)

