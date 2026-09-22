#
# Builds the EDPS command-line tutorial from latex sources
#

version = $(shell grep '\\dmdDocVersion' $(TEX_MASTER).tex | \
            head -n 1 | sed -e 's/.*{\(.*\)}/\1/' )

CHMOD = chmod
LATEX = pdflatex

CLEANFILES = *.aux *.idx *.log *.toc *.out *.bbl *.blg *.brf

TEX_MASTER = main

TEX_SOURCES = \
	$(TEX_MASTER).tex \
	intro.tex \
	installation.tex \
	quick_reduction.tex \
	customized_reduction.tex \
	useful_options.tex \
	configuration.tex \
	troubleshooting.tex \
	feedback.tex \
	conda.tex \
	layout.tex

TEX_FIGURES = $(wildcard figures/*.pdf figures/*.png figures/*.jpg figures/*.jpeg)
TEX_OUTPUT = $(addsuffix .pdf, $(TEX_MASTER))
TEX_LOG = $(addsuffix .log, $(TEX_MASTER))
TEX_MAX_ITERATIONS = 5
TEX_OPTIONS := -file-line-error -halt-on-error -interaction nonstopmode

TEXINPUTS := .:./texmf//:

all: $(TEX_OUTPUT)

$(TEX_OUTPUT): $(TEX_SOURCES) $(TEX_FIGURES)
	@echo "$(LATEX) $<"; \
	(rerun=1; i=0; \
	 until test $$i -eq $(TEX_MAX_ITERATIONS) -o $$rerun -ne 1; do \
	     if test -n "$(VERBOSE)"; then \
	         (TEXINPUTS=$(TEXINPUTS) $(LATEX) $(TEX_OPTIONS) $<) || \
			 exit 1; \
	     else \
		     (TEXINPUTS=$(TEXINPUTS) $(LATEX) $(TEX_OPTIONS) $< >/dev/null) || \
			 exit 1; \
		 fi; \
	     i=$$((i+1)); \
		 (egrep 'Label\(s\) may have changed' $(TEX_LOG) >/dev/null || \
		 egrep 'rerunfilecheck Warning' $(TEX_LOG) >/dev/null) || rerun=0; \
	 done) || exit 1; \
	$(CHMOD) 644 $(TEX_OUTPUT)

clean:
	@echo $(RM) $(TEX_OUTPUT) $(CLEANFILES); \
	$(RM) $(TEX_OUTPUT) $(CLEANFILES)

.PHONY: all clean
