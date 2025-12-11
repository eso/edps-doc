## Customizing the data reduction  <a name="configuration"></a>

### Selection of most appropriate calibrations

```{include} ../common/appropriate_calibrations.md
```

### Configuration of parameters

The data reduction of each dataset can be configured according to the scientific needs. In order to configure a
reduction, go in the `Reduction Queue` tab, which lists the datasets that are listed for reduction,
and press the button ![](../edpsgui/figures/configure_dataset.jpg) (see {numref}`fig-reduction_configuration_0`).

```{figure} figures/reduction_configuration_0.jpg
:alt: reduction_configuration_0
:name: fig-reduction_configuration_0
:figclass: left-caption

How to open the dataset configuration menu to customize data reduction.
```

The configuration window appears (see {numref}`fig-reduction_configuration_1`)
It is possible to configure `recipe parameters` associated to each individual task. When parameters are modified, they can be saved as new configuration.
Each dataset can be reduced with multiple configurations.

```{figure} figures/reduction_configuration_1.jpg
:alt: reduction_configuration_1
:name: fig-reduction_configuration_1
:figclass: left-caption

The reduction configuration window, where the recipe parameters can be configured.

```


 ---
Go to [top](#configuration)



### Inspection of intermediate products

Go in the Reduction Queue Tab. There is the list of datasets with their reduction configurations. Select a COMPLETE reduction and expand it.
A list of executed jobs will appear. By pressing on the magnifying lense in the raw of the configuration name, one has access to the main products
quality plots (currently not available in EFOSC)
as well as the list of inputs/outputs and recipe logs. 
By pressing on the magnifying lense close to each job, one has acces to the product of that job only.

Fits products can be inspected via fv and ds9 if present in the system, or via python plots.


```{figure} figures/inspect_products_1.jpg
:alt: inspect_products_1
:name: fig-inspect_products_1
:figclass: left-caption

How to access the final and/or intermediate products and logs of a reduction.

```

```{figure} figures/inspect_products_2.jpg
:alt: inspect_products_2
:name: fig-inspect_products_2
:figclass: left-caption

Panel that allows to inspect the master bias intermediate product
```

 ---
Go to EFOSC EDPS tutorial [index](../efosc/index)