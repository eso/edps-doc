VERSION=2.10.6
TUT_VERSION=2.10.6_20260515

TOPDIR :=$(shell pwd)/..
PIPEDOC_COMMON :=$(TOPDIR)/common
INSTRUMENT_EDPSGUI_TUT_DIR :=$(TOPDIR)/instrument_tutorial
EDPSGUI_TUT_DIR :=$(TOPDIR)/edpsgui/edpsgui_tutorial
TEXINPUTS :=.:$(TOPDIR):$(TOPDIR)/figures:$(INSTRUMENT_EDPSGUI_TUT_DIR):$(INSTRUMENT_EDPSGUI_TUT_DIR)/figures:$(PIPEDOC_COMMON):
INSTRUMENT := quick-guide

.PHONY: all clean pdf_check mv install view


all: $(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf mv

$(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf: $(INSTRUMENT_EDPSGUI_TUT_DIR)/*.tex 

clean:

	rm -f *.dvi *.aux *.toc *.log *.out *.brf edpsgui_$(INSTRUMENT)_tutorial.idx
	rm -f edpsgui_$(INSTRUMENT)_tutorial.pdf edpsgui_$(INSTRUMENT)_tutorial.idx ../$(INSTRUMENT)-edpsgui-tutorial-$(TUT_VERSION).pdf


# Check that all clickable URIs in PDF-document are valid
pdf_check: $(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf
	perl -nle '$$done{$$1}++ or system("wget -q -O /dev/null $$1") ? die $$1 : print $$1 while s/\bURI\/URI\(([fht]+tp[^\)]+)\)//i' $(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf

mv:
	cp  edpsgui_$(INSTRUMENT)_tutorial.pdf ../$(INSTRUMENT)-tutorial-$(TUT_VERSION).pdf
	mv  edpsgui_$(INSTRUMENT)_tutorial.pdf ../$(INSTRUMENT)-edpsgui_tutorial.pdf

#  iiinstrument-pipe-recipes.html
install: $(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf
	chmod 644 $(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf
	cp -fp $(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf /ftp/pub/dfs/pipelines/$(INSTRUMENT)/$(INSTRUMENT)edpsgui_$(INSTRUMENT)_tutorial.pdf
	chmod 444 $(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf

view:
	evince $(INSTRUMENT_EDPSGUI_TUT_DIR)/edpsgui_$(INSTRUMENT)_tutorial.pdf  &


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

