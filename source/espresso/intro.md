<a name="top"></a>

# Introduction

## Scope


This document describes how to reduce ESPRESSO data with the 
**ESO Data Processing System** (EDPS) - a user-friendly Graphic 
User Interface (GUI). The EDPS is user-oriented, but it is also 
employed internally at ESO for quality control on a regular basis.
Please note that EDPS should not be called a pipeline. Instead, 
it is an environment for executing the ESO pipelines, including 
the ESPRESSO pipeline. Other environments are Reflex (also a GUI, 
but in the process of being phazed out) and the command-line-based 
esorex. The actual ESO pipelines are the instrument-specific 
collections of recipes that are designed to process data from a 
given instrument.
Specific details on the ESPRESSO data reduction stream and how 
to configure the reduction to meet specific scientific needs 
are also described.

The data processing with EDPS is done with **workflows** – 
dedicated instrument-specific Python scripts that remove the 
instrument signature from the raw science data. The ESPRESSO 
data reduction workflow is called 
<span style="font-variant: small-caps;">espresso_wkf</span>. 
Workflows are dedicated instrument-specific (and sometimes 
mode-specific) Python scripts. They facilitate automation, 
easy repeatability, and collaboration, which are important 
for data-heavy projects. This system is flexible – with 
appropriate configuration, the users can run batch processing 
on large data sets or, alternatively, the data can be processed 
flexibly, repeating one or a few data sets with different 
parameters, seeking the data reduction strategy that best 
suits their science goals.

EDPS is the **recommended environment** to reduce data from the 
instruments at the ESO telescopes, especially for users who 
want to learn and experiment with the forthcoming environment 
for ESO pipeline execution that will be used with the 
pipelines of the next generation of ESO instruments. It is 
well suited for processing large data sets in batch mode or 
for users who
who want to (re-)process calibration data independent of 
science data. EDPS takes better advantage of the internal 
parallelization in recipes than any other pipeline execution 
environment. It also accounts for changes in the instrument
hardware when organizing the data through the so-called 
"break points".

For a more extensive documentation on the EDPS-GUI itself, consult the dedicated manual [here](../edpsgui/index).

For a brief description of EDPS and its main concepts, see [here](../edpsgui/intro.md/#what_is_edps).

The ESPRESSO pipeline itself is described in detail in a 
[pipeline manual](https://ftp.eso.org/pub/dfs/pipelines/instruments/espresso/espdr-pipeline-manual-3.3.12.pdf).


---
Go to [top](#top)

---
Go to ESPRESSO EDPS tutorial [index](../espresso/index)
