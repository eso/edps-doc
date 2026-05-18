TUT_VERSION=0.9_20260515

TOPDIR :=$(shell pwd)/..
PIPEDOC_COMMON :=$(TOPDIR)/common
EDPSGUI_TUT_DIR :=$(TOPDIR)/instrument_tutorial
TEXINPUTS :=.:$(TOPDIR):$(TOPDIR)/figures:$(EDPSGUI_TUT_DIR):$(EDPSGUI_TUT_DIR)/figures:$(PIPEDOC_COMMON):
INSTRUMENT := edpsgui

.PHONY: all clean mv 

all: $(EDPSGUI_TUT_DIR)/instrument_tutorial.pdf mv

$(EDPSGUI_TUT_DIR)/$(INSTRUMENT)_tutorial.pdf: $(EDPSGUI_TUT_DIR)/*.tex 

clean:

	rm -f *.dvi *.aux *.toc *.log *.out *.brf $(INSTRUMENT)_tutorial.idx
	rm -f $(INSTRUMENT)_tutorial.pdf $(INSTRUMENT)_tutorial.idx ../$(INSTRUMENT)-tutorial-$(TUT_VERSION).pdf


# Check that all clickable URIs in PDF-document are valid
#pdf_check: $(EDPSGUI_TUT_DIR)/edpsgui_tutorial.pdf
#	perl -nle '$$done{$$1}++ or system("wget -q -O /dev/null $$1") ? die $$1 : print $$1 while s/\bURI\/URI\(([fht]+tp[^\)]+)\)//i' $(EDPSGUI_TUT_DIR)/edpsgui_tutorial.pdf
#
mv:
	mv  instrument_tutorial.pdf ../$(INSTRUMENT)-tutorial-$(TUT_VERSION).pdf

#  iiinstrument-pipe-recipes.html
#install: $(EDPSGUI_TUT_DIR)/edpsgui_tutorial.pdf
#	chmod 644 $(EDPSGUI_TUT_DIR)/edpsgui_tutorial.pdf
#	cp -fp $(EDPSGUI_TUT_DIR)/edpsgui_tutorial.pdf /ftp/pub/dfs/pipelines/muse/edpsgui-tutorial-$(TUT_VERSION).pdf
#	chmod 444 $(EDPSGUI_TUT_DIR)/edpsgui_tutorial.pdf

#view:
#	evince $(EDPSGUI_TUT_DIR)/edpsgui_tutorial.pdf  &


# Create .pdf from .tex
%.pdf: %.tex
	TEXINPUTS=$(TEXINPUTS); export TEXINPUTS; pdflatex $*
	-bibtex  `basename $*` 
	if [ -s `basename  $*.bbl` ] ; then bibtex `basename $*` ; fi;
	TEXINPUTS=$(TEXINPUTS); export TEXINPUTS; pdflatex $*
	TEXINPUTS=$(TEXINPUTS); export TEXINPUTS; pdflatex $*
	-grep 'Label.s. may have changed' `basename $*.log` && echo s|TEXINPUTS=$(TEXINPUTS) pdflatex $*
	-grep 'Label.s. may have changed' `basename $*.log` && echo s|TEXINPUTS=$(TEXINPUTS) pdflatex $*
	-perl -e 'system("grep -w Warning `basename $*.log`") || die "Warnings are not allowed\n"'

