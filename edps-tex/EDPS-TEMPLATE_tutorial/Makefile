GUI_VERSION=0.91
TUTORIAL_REVISION=20260615

CURDIR :=$(shell pwd)
PIPEDOC_COMMON :=$(CURDIR)/pipeline_user_man
EDPSGUI_COMMON :=$(CURDIR)/common
EDPSGUI_TUT_DIR :=$(CURDIR)/instrument_tutorial
INSTRUMENT := template
.PHONY: all edpsgui clean view

all: edpsgui


edpsgui:
	cd $(EDPSGUI_TUT_DIR)  && $(MAKE) 
	cd $(CURDIR)

view:

	evince $(INSTRUMENT)-edpsgui-tutorial-$(GUI_VERSION)_$(TUTORIAL_REVISION).pdf &

clean:

	cd  $(EDPSGUI_TUT_DIR)  && $(MAKE) clean

	rm -f $(INSTRUMENT)-edpsgui-tutorial-$(GUI_VERSION)_$(TUTORIAL_REVISION).pdf


.NOTPARALLEL:
