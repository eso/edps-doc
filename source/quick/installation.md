# Installation

## Prerequisites

1. Recent Firefox or Chrome browser, Python 3.11 or higher.
2. At least one ESO pipeline with EDPS workflow should be in your system. To install the desired ESO pipelines, follow
   the instructions in the [ESO pipelines pages](http://eso.org/pipelines). NOTE: the `apptainer` installation method is
   currently not supported. After the installation, the `esorex` command must be in the path. To test whether the
   installation was successful, type

   	esorex --recipes 

A list of available recipes should appear.

## Installation steps

To install `EDPS` follow these steps:

1. Create a new Python virtual environment and activate it:

   	python3 -m venv edpsgui 
   	. edpsgui/bin/activate 

2. Install the required packages:

   	pip install --extra-index-url https://ftp.eso.org/pub/dfs/pipelines/repositories/stable/src edps edpsgui edpsplot adari_core 

---
Go to EDPS quick-start guide [index](../quick/index)