By default, EDPS associates raw calibrations to the reduction process. It is also possible to use pre-processed
calibrations (a.k.a. master calibrations) if available, in order to speed up the reduction. 
To do that:

- Stop EDPS by pressing the green Stop EDPS button in the dashboard.
- Edit the $HOME/.edps/application.properties file, by setting the parameter `association_preference`
  to `master_per_quality_level`.
- Restart EDPS to make the changes effective.

Possible values of `association_preference` are:

- **raw_per_quality_level**: At equal quality of reduction, association of raw calibrations is preferred. This is the
  default.
- **master_per_quality_level**: At equal quality of reduction, association of master calibrations is preferred.
- **raw**. Association of raw calibration is preferred, despite the quality of results.
- **master**. Association of master calibration is preferred, despite the quality of results.

When master calibrations are used, the reduction step needed to process raw calibrations are not executed. The reduction
then moves directly to the process of scientific exposures.

For example, if reduction speed for a quick check is preferred over a high quality reduction, one can select "master".
In this case, old master calibrations are associated even if there are raw calibrations closer in time (and therefore
more likely to ensure better quality products). 

The quality level that the selected calibrations deliver is indicated close to each dataset in the
`Raw input` tab, under the colum `CalibLevel`. CalibLevel=0 indicates that
calibrations that follow the rules of the instrument calibration plans have
been selected. The higher the number, the poorer the quality of the products.

More information on the application properties file can be
found [here](../edpsgui/reduction_configuration.md#configuration_file).

More explanations on the concept of "association levels" can be
found [here](../edpsgui/reduction_configuration.md#association_level).

