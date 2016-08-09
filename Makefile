DIR		:= $(dir $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
ARCH		:= $(shell uname -m)
BASEDIR		:= $(DIR:%/=%)
RPMBUILDDIR	:= $(BASEDIR)/rpmbuild
SPECSSRCDIR	:= $(BASEDIR)/specs
SPECSDIR	:= $(RPMBUILDDIR)/SPECS
SOURCESDIR	:= $(RPMBUILDDIR)/SOURCES
RPMDIR		:= $(RPMBUILDDIR)/RPMS/$(ARCH)
RELEASE		:= $(shell cd $(BASEDIR) && git rev-list --all --count)

#
#  Libraries for the packages we need to build
#
LIBRARIES	:= $(foreach lib,$(shell git config --file .gitmodules --get-regexp path | awk '{ print $$2 }'),$(strip $(lib)))
SUBMODULES	:= $(addprefix $(BASEDIR)/,$(addsuffix /.git,$(LIBRARIES)))

#
#  Git version determination script
#
GIT_VERSION	:= \
version=$$(git describe --abbrev=0 --tags 2> /dev/null || echo "0.0.0");\
count=$$(git rev-list --all --count);\
if git describe --tags 2>&1 > /dev/null; then \
        diff=$$(expr $${count} - $$(git rev-list $$version --count)); \
else \
        diff=$$count; \
fi;\
echo $${version}_$${diff}_g$$(git rev-parse --short HEAD 2> /dev/null)

#
#  Initialise the submodules
#
OUT := $(foreach x,$(LIBRARIES),$(shell test -e "$(BASEDIR)/$(x)/.git" || git submodule update --init -- "$(BASEDIR)/$(x)"))
$(info $(OUT))

#
#  Figure out the 'version' from the latest tag and commit count
#
VERSIONS	= $(foreach lib,$(LIBRARIES),$(lib)-$(shell cd "$(lib)" && $(GIT_VERSION)))
PACKAGES	= $(addprefix $(RPMDIR)/,$(addsuffix -$(RELEASE).$(ARCH).rpm,$(VERSIONS)))

#
#  The order packages should be built
#
BUILDORDER	= libosmocore libosmo-abis libosmo-netif libosmo-sccp

#
#  Prevent .git dirs from being deleted  
#
.SECONDARY:

.PHONY: all clean distclean directories dependencies udpdate test install

all: $(foreach lib,$(BUILDORDER),$(filter $(RPMDIR)/$(lib)%,$(PACKAGES)))

directories: $(RPMBUILDDIR) $(SOURCESDIR) $(SPECSDIR) $(RPMDIR)

dependencies:
	@sudo yum install -y pcsc-lite-devel ortp-devel libtool

clean:
	@rm -rf "$(RPMBUILDDIR)"

distclean: clean
	@yum remove -y 'libosmo*'

update:
	@git submodule foreach -q --recursive 'branch="$$(git config -f $$toplevel/.gitmodules submodule.$$name.branch)"; git checkout $$branch && git pull'

sync:
	$(MAKE) update
	git add $(find ./* -maxdepth 0 -type d)
	git commit --message 'sync'

#
#  Setup buildir
#
$(RPMBUILDDIR) $(SOURCESDIR) $(SPECSDIR) $(RPMDIR):
	@HOME="$(BASEDIR)" rpmdev-setuptree

$(SPECSDIR)/%.spec: $(SPECSSRCDIR)/%.spec | $(SPECSDIR)
	@cp "$<" "$@"

$(SOURCESDIR)/%.patch: $(SPECSSRCDIR)/%.patch | $(SOURCESDIR)
	@cp "$<" "$@"

#
#  Yay! Metamaking! This is really the only way you can do this
#  without losing your sanity...
#
define package
$(SOURCESDIR)/$(1)-$(2).tar.bz2: $(BASEDIR)/$(1) | $(SOURCESDIR)
	@echo ARCHIVE \"$$@\"
	@cd $(BASEDIR)/$(1) && git archive --prefix "$(1)-$(2)/" HEAD | bzip2 > $$@

$(RPMDIR)/$(1)-$(2)-$(RELEASE).$(ARCH).rpm: $(SOURCESDIR)/$(1)-$(2).tar.bz2 \
					    $(SPECSDIR)/$(1).spec \
					    $(addprefix $(SOURCESDIR)/,$(foreach x,$(wildcard $(SPECSSRCDIR)/*$(1)*.patch),$(notdir $(x))))
	@echo RPMBUILD $(1)
	@HOME="$(BASEDIR)" rpmbuild -bb --define="_version $(2)" --define="_release $(RELEASE)" $(SPECSDIR)/$(x).spec
	@yum --nogpgcheck -y localinstall $(RPMDIR)/*.rpm
endef
$(foreach x,$(LIBRARIES),$(eval $(call package,$(x),$(shell cd "$(BASEDIR)/$(x)" && $(GIT_VERSION)))))

