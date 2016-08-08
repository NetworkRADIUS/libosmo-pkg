DIR		:= $(dir $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
CPUS		:= CORES=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || sysctl -n hw.ncpu)
BUILDDIR	:= $(DIR:%/=%)/build

#
#  Libraries for the packages we need to build
#
libraries	= $(wildcard libosmo*)

PACKAGES	= $(addprefix $(BUILDDIR)/,$(notdir $(libraries)))
ARCHIVES        = $(addsuffix .tar.bz2,$(PACKAGES))

$(info $(PACKAGES))
$(info $(BUILDDIR))
#
#  Prevent .git dirs from being deleted  
#
.SECONDARY:

$(BUILDDIR)/%.tar.bz2: %/.git
	@echo ARCHIVE $(notdir $@)
	cd $(dir $<)
	git archive master | bzip2 > $@

$(BUILDDIR)/%: | $(BUILDDIR)/%.tar.bz2
	@echo ARCHIVE $@

#
#  Initialise submodules
#
%/.git: 
	@git submodule update --init $(dir $@)
	@cd $(dir $@) && git checkout $$(git config -f ../.gitmodules submodule.$(subst /,,$(dir $@)).branch)

.PHONY: all clean distclean udpdate test install
all: $(PACKAGES) 

update:
	@git submodule foreach -q --recursive 'branch="$$(git config -f $$toplevel/.gitmodules submodule.$$name.branch)"; git checkout $$branch && git pull'

sync:
	@$(MAKE) update
	@git add $(find ./* -maxdepth 0 -type d)
	@git commit --message 'sync'
