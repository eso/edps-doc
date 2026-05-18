1. Change the overleaf project name into EDPS-<wkfname>_tutorial for example EDPS_FORS_IMAGING_tutorial

2. In the Makefile and instrument_tutorial/Makefile

 Change INSTRUMENT value in Makefile and instrument_tutorial/Makefile
 Change TUTORIAL_VERSION and TUTORIAL_REVISION in  Makefile
 Change TUT_VERSION in instrument_tutorial/Makefile

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


Edit the change records accordingly

4.  add as many \input{XXX} as required, but you shuld keep those
already listed if possible.

5.

The directoryinstrument_tutorial/figures contains the kind figures you
need to start with (and much more). They are the muse-version. Please,
prepare the same for your instrument and KEEP THE SAME NAME.  The
suggestion is to - first apply the changes above - type make from the
main directory - check the pdf and see which figure you need to adapt
for your instrument.

Other figures can be added if your tutorial requires it.

If the command make does not work, call me.
