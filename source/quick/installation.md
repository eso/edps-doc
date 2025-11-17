# Installation

## Prerequisites

1. Recent Firefox or Chrome browser, Python 3.11 or higher (but there are issues with Python 3.14).
2. At least one ESO pipeline with EDPS workflow should be in your system. To install the desired ESO pipelines, follow
   the instructions in the [ESO pipelines pages](http://eso.org/pipelines). NOTE: the `apptainer` installation method is
   currently not supported. After the installation, the `esorex` command must be in the path. To test whether the
   installation was successful, type

   	    esorex --recipes 
https://heasarc.gsfc.nasa.gov/docs/software/ftools/fv/fv.html.5.0
A list of available recipes should appear.

3. Install [graphviz](https://graphviz.org/), [fv](https://heasarc.gsfc.nasa.gov/docs/software/ftools/fv/fv.html.5.0), and 
[ds9](https://sites.google.com/cfa.harvard.edu/saoimageds9/download), which have to be included in the system path (definying aliases not enough). Graphviz can be easily installed via:

         sudo apt install graphviz (Debian, Ubuntu)
         sudo dnf install graphviz (Fedora)

   For fv and ds9, follow the instructions in corresponding webpages.
   You can test whether these three packages are installed and their path are correctly set by typing on a terminal:

         dot -V
         fv  -version
         ds9 -version


## Installation steps

To install `EDPS` follow these steps:

1. Create a new Python virtual environment and activate it:

         python3 -m venv edpsgui
         . edpsgui/bin/activate

   Make sure the python3 version is 3.11 or higher, but not 3.14. 

2. Install the required packages:

         pip install --extra-index-url https://ftp.eso.org/pub/dfs/pipelines/repositories/stable/src edps edpsgui edpsplot adari_core 

---
Go to EDPS quick-start guide [index](../quick/index)