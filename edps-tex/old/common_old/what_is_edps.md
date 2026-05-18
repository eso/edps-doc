The ESO Data Processing System (EDPS) is a framework to run ESO’s data processing pipelines and it is meant to
eventually replace the previous [EsoReflex environment](https://www.eso.org/sci/software/esoreflex/). The general
principles of EDPS have been described by Freudling, Zampieri, Coccato et
al. [2024, A&A, 681, A93](https://www.aanda.org/articles/aa/full_html/2024/01/aa47651-23/aa47651-23.html). Please refer
to that paper if you have used EDPS for research resulting in a scientific publication.

Each of ESO’s data processing pipeline consist of a series of standalone programs called “recipes”. Each recipe is
designed to process certain type(s) of input data. The processing of these input data typically requires a range of
auxiliary files such as calibration files. EDPS is designed to select appropriate input data for the different recipes
of a pipeline, and execute them in sequence. This is done by specifying for each pipeline the workflow for organizing
data and executing the recipes. This workflow can the used to process a set of data fully automatically.
