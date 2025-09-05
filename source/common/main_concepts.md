
EDPS is an environment designed to execute the recipes of an instrument pipeline according to a series of instructions. 
The main concepts in EDPS are:

- **Workflow** and **reduction cascades**. A workflow is a series of instructions designed to reduce data with an instrument pipeline 
  in potentially multiple ways, by carrying on a sequence of tasks. 
  Each workflow can define multiple reduction cascades, depending on the scientific needs.
  Foe example, the same workflow can be used to process data following different strategies that trigger different
  reduction steps (e.g. in one strategy flux calibration can be omitted) or different end-points (e.g., combine 
  different science exposures, or stop after the reduction of individual exposures without combining them). Each of these "strategies"
  defines a "reduction cascade"`".

- **Task**, **jobs**, and **recipes**. A task is an element in the workflow that performs a given step of the data reduction
  cascade. Tasks are often associated to a recipe of the underlying instrument pipeline. 
  A jobs is a work unit in a processing environment, that runs a recipe on a set of input data with a set of recipe paraemters.
  A single task can generate several jobs: for
  example, a "bias" task, can generate multiple jobs, each of the running the bias recipe on a different set of input files.

- **Dataset**. A dataset is a collection of files, that are needed to perform the data reduction as specified by the
  workflow. It consists, for example, of one or more science files plus the calibrations needed to process them. In
  EDPS, the dataset has a hierarchical structure, which highlights the connections between the various 
  files and tasks (e.g., task A is an input to task B).

- **Target** and **Target category**. The "target", or the "target task" is the end point of the reduction cascade. When specifying a target, EDPS will process
  all and only the files needed to execute it. For example, if my target is "science", and the science files
  need the bias files, EDPS will process only the biases that have been selected to process those science files.
  However, if my target is bias, then EDPS will process all and only the bias files, regardless they are not used by any science. 
  The "Target category` is a group of target that have similar purposes. For example, the target category `science`, includes
  all the tasks that deliver final scientific products, the target category `qc1calib` includes all and only the tasks that 
  perform a calibration (e.g., bias, standard stars).

<a name="association_levels"></a>
- **Association levels**. Processing a given type of data (e.g., science frame) requires certain calibraions (e.g., flat field) that match
similar properties (e.g., taken with the same filter). The rules on how to associate a given calibration to a given file requiring it are encoded
within the workflow. There could obviously be many calibrations that matches the association criteria (e.g., many flat fields taken with the same filter). In this case,  
EDPS associates the closest in time. However, having found a calibration does not mean that that calibration delivers a trustful reduction (e.g., the flat could be 5 years old).
Therefore, in EDPS there is the concept of "association level", or "quality level of the association", typically a quality level is associated to a validity time range that 
can differ for different types of calibrations and instruments. EDPS first looks for calibrations that satisfy the first quality level (e.g., 24 hours), associated to the instrument calibration plan (labeled, for convention, as level=0).
If a calibration in that validity range is not found, then calibrations within the second validity range are searched (e.g., 2 days), and so forth until the last validity time range (e.g. 3 months)
encoded for that calibration (labelled, for convention, to quality level=3). Calibrations outside the last validity period are not associated. 
It is possible to see the quality level of each association in the dataset description. One can therefore decide whether the level of association is enough, or to look for other calibrations in the archive.
The convention of the association levels is the following, the time range of the different levels obviously depend on the instrument and on the calibration itself:

  - level < 0. Calibrations more restrictive than the calibration plan are selected.
  - level = 0. Calibrations that follow the rules of the instrument calibration plans are selected.
  - level = 1. The selected calibrations are sufficient to ensure good quality science results.
  - level = 2. The selected calibrations "probably" produce results of still "acceptable" quality.
  - level = 3. Significant risk of bad quality results or recipe failure.