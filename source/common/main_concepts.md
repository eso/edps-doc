
EDPS is an environment designed to execute the recipes of an instrument pipeline according to a series of instructions. 
The main concepts in EDPS are:

- `Workflow` and `reduction cascades`. A workflow is a series of instructions designed to reduce data with an instrument pipeline 
  in potentially multiple ways, by carrying on a sequence of `tasks`. 
  Each workflow can define multiple reduction cascades, depending on the scientific needs.
  Foe example, the same workflow can be used to process data following different strategies that trigger different
  reduction steps (e.g. in one strategy flux calibration can be omitted) or different end-points (e.g., combine 
  different science exposures, or stop after the reduction of individual exposures without combining them). Each of these "strategies"
  defines a `reduction cascade`.

- `Task`, `jobs`, and `recipes`. A `task` is an element in the workflow that performs a given step of the data reduction
  cascade. Tasks are often associated to a recipe of the underlying instrument pipeline. 
  A `jobs` is a work unit in a processing environment, that runs a recipe on a set of input data with a set of recipe paraemters.
  A single task can generate several jobs: for
  example, a "bias" task, can generate multiple jobs, each of the running the bias recipe on a different set of input files.

- `Dataset`. A dataset is a collection of files, that are needed to perform the data reduction as specified by the
  workflow. It consists, for example, of one or more science files plus the calibrations needed to process them. In
  EDPS, the dataset has a hierarchical structure, which highlights the connections between the various 
  files and tasks (e.g., task A is an input to task B).

- `Target` and `Target category`. The `target`, or the `target task` is the end point of the reduction cascade. When specifying a target, EDPS will process
  all and only the files needed to execute it. For example, if my target is "science", and the science files
  need the bias files, EDPS will process only the biases that have been selected to process those science files.
  However, if my target is bias, then EDPS will process all and only the bias files, regardless they are not used by any science. 
  The `Target category` is a group of target that have similar purposes. For example, the target category science, includes
  all the tasks that deliver final scientific products, the target category qc1calib includes all and only the tasks that 
  perform a calibration (e.g., bias, standard stars).
