PIPE_VERSION=2.10.6
REFLEX_VERSION=2.10.6
TUTORIAL_VERSION=2.10.6
TUTORIAL_REVISION=20260515
CURDIR :=$(shell pwd)
PIPEDOC_COMMON :=$(CURDIR)/pipeline_user_man
EDPSGUI_COMMON :=$(CURDIR)/common
MUSE_EDPSGUI_TUT_DIR :=$(CURDIR)/instrument_tutorial

.PHONY: all edpsgui clean view

all:	edpsgui


edpsgui:

	cd $(MUSE_EDPSGUI_TUT_DIR) && $(MAKE)

	cd $(CURDIR)

view:

	evince muse-edpsgui-tutorial-$(TUTORIAL_VERSION)_$(TUTORIAL_REVISION).pdf &

clean:

	cd  $(MUSE_EDPSGUI_TUT_DIR)  && $(MAKE) clean

	rm -f muse-edpsgui-tutorial-$(TUTORIAL_VERSION)_$(TUTORIAL_REVISION).pdf


.NOTPARALLEL:
