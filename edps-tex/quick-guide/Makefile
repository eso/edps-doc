PIPE_VERSION=2.10.6
REFLEX_VERSION=2.10.6
TUTORIAL_VERSION=0.9
TUTORIAL_REVISION=20260515
CURDIR :=$(shell pwd)
PIPEDOC_COMMON :=$(CURDIR)/pipeline_user_man
EDPSGUI_COMMON :=$(CURDIR)/common
INSTRUMENT_EPSGUI_TUT_DIR :=$(CURDIR)/instrument_tutorial
INSTRUMENT := quick-guide

.PHONY: all edpsgui clean view

all:	edpsgui


edpsgui:

	cd $(INSTRUMENT_EPSGUI_TUT_DIR) && $(MAKE)

	cd $(CURDIR)

view:

	evince $(INSTRUMENT)-edpsgui-tutorial-$(TUTORIAL_VERSION)_$(TUTORIAL_REVISION).pdf &

clean:

	cd  $(INSTRUMENT_EPSGUI_TUT_DIR)  && $(MAKE) clean

	rm -f $(INSTRUMENT)-edpsgui-tutorial-$(TUTORIAL_VERSION)_$(TUTORIAL_REVISION).pdf


.NOTPARALLEL:
