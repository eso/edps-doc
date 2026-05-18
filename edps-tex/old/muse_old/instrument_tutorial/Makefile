VERSION=2.10.6
TUT_VERSION=2.10.6_20260515

TOPDIR :=$(shell pwd)/..
PIPEDOC_COMMON :=$(TOPDIR)/common
REFLEX_TUT_DIR :=$(TOPDIR)/edpsgui_tutorial
MUSE_EDPSGUI_TUT_DIR :=$(TOPDIR)/instrument_tutorial
EDPSGUI_TUT_DIR :=$(TOPDIR)/edpsgui/edpsgui_tutorial
TEXINPUTS :=.:$(TOPDIR):$(TOPDIR)/figures:$(MUSE_EDPSGUI_TUT_DIR):$(MUSE_EDPSGUI_TUT_DIR)/figures:$(PIPEDOC_COMMON):

all: $(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf mv

$(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf: $(MUSE_EDPSGUI_TUT_DIR)/*.tex 

clean:

	rm -f *.dvi *.aux *.toc *.log *.out *.brf edpsgui_muse_tutorial.idx
	rm -f edpsgui_muse_tutorial.pdf edpsgui_muse_tutorial.idx ../muse-edpsgui-tutorial-$(TUT_VERSION).pdf


# Check that all clickable URIs in PDF-document are valid
pdf_check: $(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf
	perl -nle '$$done{$$1}++ or system("wget -q -O /dev/null $$1") ? die $$1 : print $$1 while s/\bURI\/URI\(([fht]+tp[^\)]+)\)//i' $(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf

mv:
	mv  edpsgui_muse_tutorial.pdf muse-edpsgui-tutorial-$(TUT_VERSION).pdf
	mv  muse-edpsgui-tutorial-$(TUT_VERSION).pdf ..

#  iiinstrument-pipe-recipes.html
install: $(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf
	chmod 644 $(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf
	cp -fp $(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf /ftp/pub/dfs/pipelines/muse/muse-edpsgui-tutorial-$(TUT_VERSION).pdf
	chmod 444 $(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf

view:
	evince $(MUSE_EDPSGUI_TUT_DIR)/edpsgui_muse_tutorial.pdf  &


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

