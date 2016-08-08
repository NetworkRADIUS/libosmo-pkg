DIR		:= $(dir $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
CPUS		:= CORES=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || sysctl -n hw.ncpu)
BASEDIR		:= $(DIR:%/=%)
RPMBUILDDIR	:= $(BASEDIR)/rpmbuild
SPECSDIR	:= $(RPMBUILDDIR)/SPECS
SOURCESDIR	:= $(RPMBUILDDIR)/SOURCES

#
#  Libraries for the packages we need to build
#
LIBRARIES	= $(shell git config --file .gitmodules --get-regexp path | awk '{ print $$2 }')
SUBMODULES	= $(addprefix $(BASEDIR)/,$(addsuffix /.git,$(LIBRARIES)))

#
#  Have to ensure all submodules are checked out first
#
ifeq ($(filter $(SUBMODULES),$(MAKECMDGOALS)),)
OUT=$(shell $(MAKE) -C "$(BASEDIR)" $(SUBMODULES))
endif

VERSIONS	= $(foreach mod,$(LIBRARIES),$(shell cd "$(mod)" && (git describe --abbrev=0)-$(shell cd "$(mod)" && git rev-list --all --count))

$(info $(VERSIONS))
#
#  Prevent .git dirs from being deleted  
#
.SECONDARY:

.PHONY: all clean distclean directories udpdate test install
all: $(PACKAGES) 

directories: $(RPMBUILDDIR) $(SOURCESDIR) $(SPECSDIR)

#
#  Setup our build directory
#
$(RPMBUILDDIR) $(SOURCESDIR) $(SPECSDIR):
	HOME="$(BASEDIR)" rpmdev-setuptree

$(SPECDIR)/%.tar.bz2: %/.git $(SOURCESDIR)
	echo ARCHIVE $(notdir $@)
	mkdir -p "$(dir $@)"
	cd $(dir $<)
	git archive master | bzip2 > $@

$(RPMBUILDDIR)/%: $(RPMBUILDDIR)/%.tar.bz2
	echo Hello

#
#  Initialise submodules
#
%/.git: 
	@git submodule update --init $(@D) > /dev/null 
	@cd $(@D) && git checkout $$(git config -f ../.gitmodules submodule.$(subst /,,$(dir $@)).branch)

clean:
	rm -rf "$(RPMBUILDDIR)"

update:
	git submodule foreach -q --recursive 'branch="$$(git config -f $$toplevel/.gitmodules submodule.$$name.branch)"; git checkout $$branch && git pull'

sync:
	$(MAKE) update
	git add $(find ./* -maxdepth 0 -type d)
	git commit --message 'sync'
