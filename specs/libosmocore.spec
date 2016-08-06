%global git_commit 916423ef9585c7042730fdb17f55afc376565d32
%global git_date 20151109

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

# git clone git://git.osmocom.org/libosmocore.git
# cd %%{name}
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{git_commit} | \
# bzip2 > ../%%{name}-%%{version}-%%{git_suffix}.tar.bz2

Name:             libosmocore
URL:              http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
Version:          0.9.0
Release:          3.%{git_suffix}%{?dist}
License:          GPLv2+ and GPLv3+ and AGPLv3+
BuildRequires:    autoconf, automake, libtool, pcsc-lite-devel, doxygen
BuildRequires:    findutils, sed
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Group:            Applications/Engineering
Summary:          Utility functions for OsmocomBB, OpenBSC and related projects
Source0:          %{name}-%{version}-%{git_suffix}.tar.bz2

%description
A collection of common code used in various sub-projects inside the Osmocom
family of projects (OsmocomBB, OpenBSC, ...).

%package devel
Summary:          Development files for libosmocore
Group:            Applications/Engineering
Requires:         %{name}%{?_isa} = %{version}-%{release}
# for /usr/include/osmocom directory
Requires:         libosmo-dsp-devel

%description devel
Development files for libosmocore.

%package doc
Summary:        Documentation files for libosmocore
Group:          Applications/Engineering
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files for libosmocore.

%prep
%setup -q
%patch0 -p1 -b .ppc-smscb-fix

%build
autoreconf -fi
%configure

# Fix unused direct shlib dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
# Remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} \;

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc %{_docdir}/%{name}
# fallback for cases where there is no _licensdir
%exclude %{_docdir}/%{name}/codec
%exclude %{_docdir}/%{name}/core
%exclude %{_docdir}/%{name}/gsm
%exclude %{_docdir}/%{name}/vty
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/osmocom/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/%{name}/codec
%doc %{_docdir}/%{name}/core
%doc %{_docdir}/%{name}/gsm
%doc %{_docdir}/%{name}/vty

%changelog
* Wed Dec  9 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.0-3.20151109git916423ef
- Fixed library to pass smscb test on ppc
  Resolves: rhbz#1289940

* Wed Dec  2 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.0-2.20151109git916423ef
- Updated according to review

* Mon Nov  9 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.9.0-1.20151109git916423ef
- Initial version
