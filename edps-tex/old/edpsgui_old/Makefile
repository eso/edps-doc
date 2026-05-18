TUTORIAL_VERSION=0.9
TUTORIAL_REVISION=20260515

CURDIR :=$(shell pwd)
PIPEDOC_COMMON :=$(CURDIR)/pipeline_user_man
EDPSGUI_COMMON :=$(CURDIR)/common
EDPSGUI_TUT_DIR :=$(CURDIR)/edpsgui_tutorial

.PHONY: all edpsgui clean view

all: edpsgui


edpsgui:
	cd $(EDPSGUI_TUT_DIR)  && $(MAKE) 
	cd $(CURDIR)

view:

	evince espdr-edpsgui-tutorial-$(TUTORIAL_VERSION)_$(TUTORIAL_REVISION).pdf &

clean:

	cd  $(EDPSGUI_TUT_DIR)  && $(MAKE) clean

	rm -f muse-edpsgui-tutorial-$(TUTORIAL_VERSION)_$(TUTORIAL_REVISION).pdf


.NOTPARALLEL:
