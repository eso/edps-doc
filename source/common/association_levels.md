Processing a given type of data (e.g., science frame) requires certain calibrations (e.g., flat field) that match
similar properties (e.g., taken with the same filter). The rules on how to associate a given calibration to a given file
requiring it are encoded
within the workflow. There could obviously be many calibrations that matches the association criteria (e.g., many flat
fields taken with the same filter). In this case,  
EDPS associates the closest in time. However, having found a calibration does not mean that that calibration delivers a
trustful reduction (e.g., the flat could be 5 years old).
Therefore, in EDPS there is the concept of "association level", or "quality level of the association", typically a
quality level is associated to a validity time range that
can differ for different types of calibrations and instruments. EDPS first looks for calibrations that satisfy the first
quality level (e.g., 24 hours), associated to the instrument calibration plan (labeled, for convention, as level=0).
If a calibration in that validity range is not found, then calibrations within the second validity range are searched (
e.g., 2 days), and so forth until the last validity time range (e.g. 3 months)
encoded for that calibration (labelled, for convention, to quality level=3). Calibrations outside the last validity
period are not associated.
It is possible to see the quality level of each association in the dataset description. One can therefore decide whether
the level of association is enough, or to look for other calibrations in the archive.
The convention of the association levels is the following, the time range of the different levels obviously depend on
the instrument and on the calibration itself:

- level < 0. Calibrations more restrictive than the calibration plan are selected.
- level = 0. Calibrations that follow the rules of the instrument calibration plans are selected.
- level = 1. The selected calibrations are sufficient to ensure good quality science results.
- level = 2. The selected calibrations "probably" produce results of still "acceptable" quality.
- level = 3. Significant risk of bad quality results or recipe failure.