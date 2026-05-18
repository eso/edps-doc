1. Copy the overleaf template project into EDPS-<wkfname>_tutorial, for example EDPS_FORS_IMAGING_tutorial
The main document is instrument_tutorial/instrument_tutorial.tex

2. In the Makefile and instrument_tutorial/Makefile

 Change INSTRUMENT value in Makefile (line 8) and instrument_tutorial/Makefile (line 7)
 Change TUTORIAL_VERSION and TUTORIAL_REVISION in  Makefile only
 Change TUT_VERSION in instrument_tutorial/Makefile only

The logic is to have the tutorial version matching the EDPS_GUI version and the revision matching the date of the last revision.

3. Change instrument_tutorial/instrument_tutorial.tex, and modify the fields:

author          : your name
pdftitle        : title of the tutorial (e.g. FORS IMAGING EDPS-GUI tutorial)
releasedate     : released date
issue           : issue number (I "think" it must match TUTORIAL_VERSION)
revision        : revision number(must match TUTORIAL_REVISION)

pipelinevers    : the version of the pipeline the tutorial refers to, e.g. 2.3.1
instname        : the name of the instrument, e.g. FORS2
pipename        : the name of the pipeline, e.g. fors
wkffilename     : the name of the python file the tutorial is for, e.g. fors_imaging_wkf.py
wkfname         : the name of the workflow the tutorial is for, e.g. fors.fors_imaging_wkf
edpsversion     : version of edps
edpsguiversion  : version of edps-gui 


Still in instrument_tutorial/instrument_tutorial.tex, edit the change records (line 79) accordingly

4.  add as many Sections (\input{XXX}) as required, but you should keep those
already listed if possible.
PLEASE, DO NOT CHANGE ANYTHING IN THE common/ DIRECTORY

Usually, the list of files requiring changes are:
 intro.tex: no changes needed
 reducing_demo_data.tex: add the list of final products at the end of the file
 reduction_chain.tex: describe the reduction chain, with tips on the wkf and recipe parameters to modify to improve the outcome.
 configure_reudction.tex: describe the instrument specific parameters, and multiple reduction strategies
 task_list.tex: list all the tasks
 faq.tex: eventually, add instrument specific faq.
 
5.
PLEASE, DO NOT CHANGE ANYTHING IN THE common/ DIRECTORY

The directory instrument_tutorial/figures contains the kind figures you
need to start with (and much more). By default, they are the muse-version. 
Please, prepare the same for your instrument and KEEP THE SAME NAMES. 
The suggestion is to 
a. apply the changes above
b. type make from the main directory, or click Recompile on Overleaf
c. check the pdf and see which figure(s) you need to adapt for your instrument.
d. additional figures can be added if your tutorial requires it.

If the command make does not work, or the compilation fails, contact L. Coccato.
