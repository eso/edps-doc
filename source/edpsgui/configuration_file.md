# How to configure EDPS: the `application.properties` file.

Several options in `EDPS` can be specified in a configuration file, named `application.properties`.
This file is located in the `.edps/` directory in your `HOME` directory. 
Note: to make effective the changes done in application.properties, one must restart the EDPS dashboard.


## Association preference: RAW vs MASTER calibrations.

If the input directory contain both MASTER (e.g., pre-reduced calibrations) and RAW calibrations, it
could happen that both of them fulfil the matching criteria and quality level for a
certain task. In this case, one can specify to which type of calibration to give priority by setting the
variable association_preference in the `application.properties` configuration file.

Possible values of association_preference are:
 - **raw**. First, EDPS checks if there are raw calibrations ensuring the first quality level (see [here](
   ../common/main_concepts.md#association_levels)) of the
products. If found, they are associated. If not found, raw calibrations ensuring the second quality
level of the products are searched. If not found, the next level is searched until the last quality
level  is reached.
If no raw calibrations are found for none of the quality levels, then EDPS searches for master
calibrations, starting from those ensuring the first quality level. If none are found, the second
level is searched, and so forth. If no calibrations are found, the association is not done.
- **master**. Same as raw, but first master calibrations are looked for all the products quality levels
permitted by the workflow parameter quality_threshold. Then, if master
calibrations are not found, the system looks for raw calibrations.
- **raw_per_quality_level** (default). First, the system will check if there are raw calibra-
tions ensuring the first quality level of the products. If not found, MASTER calibrations en-
suring this level are searched for. If not found, RAW calibrations ensuring the second quality
level are searched for, if not found MASTER calibrations matching the second quality level are
searched for. The sequence goes on until the last level permitted by the workflow parameter
quality_threshold.
- **master_per_quality_level**. Same as raw_per_quality_level, but with inverted roles
for MASTER and RAW calibrations.
If a combination of RAW and MASTER calibrations are present, the value of association_preference
might have an impact on the performances and the quality of the results. Typically. association_
preference = raw_per_quality_level delivers the best quality products, at the price of speed.
On the other hand, association_preference = master ensures faster performances, at cost
of quality (e.g., a very old master calibration could be used instead a more recent raw calibration). If
only RAW or MASTER calibrations are present in the input directories, then the value of association_
preference has no impact.


## Parallelization
One of the advantages of EDPS is that it can exploit powerful hardware. The following variables in
the application.properties file determine the pararellization of EDPS reduction.
- `processes` (default: 1). It specifies the maximum number of jobs to run in parallel (e.g. esorex
parallel executions) .
- `cores` (default: 1). It specifies the maximum numbers of computers cores to use, considering
all the parallel jobs.
- `default_omp_threads` (default: 1). The number of cores to use for each job. This can be
overridden by specifying a recipe parameter OMP_NUM_THREAD for a given task when configuring the reduction. 

## Order of executions.
The variable ordering in the application.properties file specifies the priority to give to the
reduction jobs. The most important values are:
- `dfs`. depth-first, gives preference to reaching final reduction target quicker. In other words, it
finish the reduction of a dataset before moving to the next dataset. This choice is less efficient
in time but it gives priority to the reduction of individual datasets.
- `type`. It gives preference to following the reduction cascade level by level making sure to pro-
cess same type of data together (eg. first all biases).
- `dynamic`. Immediately runs whichever job is ready (has all needed inputs), no stalling but the
order is unpredictable. This is the most time efficient execution order.