#
# spec file for package libosmocore
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libosmocore
Version:        %{_version}
Release:        %{_release}
Summary:        Open Source Mobile Communications Core Library
License:        GPL-2.0 and GPL-2.0+ and LGPL-3.0+ and AGPL-3.0+
Group:          Productivity/Telephony/Utilities
Url:            http://bb.osmocom.org/trac/wiki/libosmocore

#Git-Clone:	git://git.osmocom.org/libosmocore
Source:         %name-%version.tar.bz2
Patch1:         0001-libosmocore-pkgconfig.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake >= 1.6
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  xz
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(talloc)

%description
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

There is no clear scope of it. It simply houses all code shared
between OsmocomBB and OpenBSC to avoid code duplication.

%package tools
Summary:        GSM utilities from the osmocore project
License:        GPL-2.0 and GPL-2.0+ and LGPL-3.0+ and AGPL-3.0+
Group:          Productivity/Telephony/Utilities

%description tools
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

This package contains GSM utilities from libosmocore.

%package -n libosmocodec0
Summary:        Library for Osmocom codec-related utilities
License:        GPL-2.0+
Group:          System/Libraries

%description -n libosmocodec0
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

%package -n libosmocodec-devel
Summary:        Development files for the Osmocom codec library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       libosmocodec0 = %version

%description -n libosmocodec-devel
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmocodec.

%package -n libosmocore-devel
Summary:        Development files for the Osmocom core library
License:        GPL-2.0 and GPL-2.0+
Group:          Development/Libraries/C and C++
# crc16.h has GPL2-only clauses, the rest (*.h) is GPL-2.0+
Requires:       libosmocore = %version
Requires:       libtalloc-devel

%description -n libosmocore-devel
libosmocore is a library with various utility functions shared
between OpenBSC and OsmocomBB.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmocore.

%package -n libosmoctrl0
Summary:        Osmocom SNMP-like control interface library
License:        GPL-2.0+
Group:          System/Libraries

%description -n libosmoctrl0
libosmocore is a library with various utility functions shared
between OpenBSC and OsmocomBB.

libosmoctrl is an SNMP-like control interface. In contrast to the VTY
interface, the control interface is meant to be used by programs.

%package -n libosmoctrl-devel
Summary:        Osmocom control interface library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmoctrl0 = %version
Requires:       libosmovty-devel = %version

%description -n libosmoctrl-devel
libosmoctrl is an SNMP-like control interface. In contrast to the VTY
interface, the control interface is meant to be used by programs.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmoctrl.

%package -n libosmogb4
Summary:        Osmocom GPRS Gb Interface (NS/BSSGP) library
License:        AGPL-3.0+
Group:          System/Libraries

%description -n libosmogb4
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

%package -n libosmogb-devel
Summary:        Development files for the Osmocom GPRS Gb interface library
License:        AGPL-3.0+
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmogb4 = %version
Requires:       libosmogsm-devel = %version

%description -n libosmogb-devel
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmogb.

%package -n libosmogsm5
Summary:        Osmocom GSM core library
License:        GPL-2.0+ and AGPL-3.0+
Group:          System/Libraries

%description -n libosmogsm5
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

%package -n libosmogsm-devel
Summary:        Development files for the Osmocom GSM core library
License:        GPL-2.0+ and AGPL-3.0+
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmogsm5 = %version

%description -n libosmogsm-devel
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmogsm.

%package -n libosmosim0
Summary:        Osmocom SIM card related utility library
License:        GPL-2.0+
Group:          System/Libraries

%description -n libosmosim0
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

%package -n libosmosim-devel
Summary:        Development files for the Osmocom SIM card utility library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmosim0 = %version

%description -n libosmosim-devel
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmosim.

%package -n libosmovty3
Summary:        Osmocom VTY interface library
License:        GPL-2.0+
Group:          System/Libraries

%description -n libosmovty3
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

%package -n libosmovty-devel
Summary:        Development files for the Osmocom VTY interface library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmovty3 = %version

%description -n libosmovty-devel
libosmocore is a library with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that we develop in the sphere of Free Software / Open Source mobile
communications.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmovty.

%prep
%setup -q
%patch -P 1 -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
%configure --enable-shared --disable-static \
	--includedir="%_includedir/%name"
make %{?_smp_mflags}

%install
b="%buildroot"
make %{?_smp_mflags} install DESTDIR="$b"
find "$b/%_libdir" -type f -name "*.la" -delete

%check
# susceptible to timing issues
make %{?_smp_mflags} check || :

%post   -n libosmocodec0 -p /sbin/ldconfig
%postun -n libosmocodec0 -p /sbin/ldconfig
%post   -n libosmocore -p /sbin/ldconfig
%postun -n libosmocore -p /sbin/ldconfig
%post   -n libosmoctrl0 -p /sbin/ldconfig
%postun -n libosmoctrl0 -p /sbin/ldconfig
%post   -n libosmogb4 -p /sbin/ldconfig
%postun -n libosmogb4 -p /sbin/ldconfig
%post   -n libosmogsm5 -p /sbin/ldconfig
%postun -n libosmogsm5 -p /sbin/ldconfig
%post   -n libosmosim0 -p /sbin/ldconfig
%postun -n libosmosim0 -p /sbin/ldconfig
%post   -n libosmovty3 -p /sbin/ldconfig
%postun -n libosmovty3 -p /sbin/ldconfig

%files tools
%defattr(-,root,root)
%_bindir/osmo-*

%files -n libosmocodec0
%defattr(-,root,root)
%_libdir/libosmocodec.so.0*

%files -n libosmocodec-devel
%defattr(-,root,root)
%dir %_includedir/%name
%dir %_includedir/%name/osmocom
%_includedir/%name/osmocom/codec/
%_libdir/libosmocodec.so
%_libdir/pkgconfig/libosmocodec.pc

%files -n libosmocore
%defattr(-,root,root)
%_libdir/libosmocore.so.7*

%files -n libosmocore-devel
%defattr(-,root,root)
%dir %_includedir/%name
%dir %_includedir/%name/osmocom
%_includedir/%name/osmocom/core/
%_libdir/libosmocore.so
%_libdir/pkgconfig/libosmocore.pc

%files -n libosmoctrl0
%defattr(-,root,root)
%_libdir/libosmoctrl.so.0*

%files -n libosmoctrl-devel
%defattr(-,root,root)
%dir %_includedir/%name
%dir %_includedir/%name/osmocom
%_includedir/%name/osmocom/ctrl/
%_libdir/libosmoctrl.so
%_libdir/pkgconfig/libosmoctrl.pc

%files -n libosmogb4
%defattr(-,root,root)
%_libdir/libosmogb.so.4*

%files -n libosmogb-devel
%defattr(-,root,root)
%dir %_includedir/%name
%dir %_includedir/%name/osmocom
%_includedir/%name/osmocom/gprs/
%_libdir/libosmogb.so
%_libdir/pkgconfig/libosmogb.pc

%files -n libosmogsm5
%defattr(-,root,root)
%_libdir/libosmogsm.so.5*

%files -n libosmogsm-devel
%defattr(-,root,root)
%dir %_includedir/%name
%dir %_includedir/%name/osmocom
%_includedir/%name/osmocom/gsm/
%_includedir/%name/osmocom/crypt/
%_libdir/libosmogsm.so
%_libdir/pkgconfig/libosmogsm.pc

%files -n libosmosim0
%defattr(-,root,root)
%_libdir/libosmosim.so.0*

%files -n libosmosim-devel
%defattr(-,root,root)
%dir %_includedir/%name
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/sim/
%_libdir/libosmosim.so
%_libdir/pkgconfig/libosmosim.pc

%files -n libosmovty3
%defattr(-,root,root)
%_libdir/libosmovty.so.3*

%files -n libosmovty-devel
%defattr(-,root,root)
%dir %_includedir/%name
%dir %_includedir/%name/osmocom
%_includedir/%name/osmocom/vty/
%_libdir/libosmovty.so
%_libdir/pkgconfig/libosmovty.pc

%changelog
* Fri Mar 11 2016 jengelh@inai.de
- reenable bigendian builds as GSM IE code was fixed upstream
  during 2015
- Update to new upstream snapshot 0.9.0.91
  * log: Add conditional logging based on log_check_level
  * Add byte printing macros
  * vty: add bind command for telnet vty line
* Fri Jan 22 2016 jengelh@inai.de
- Update to new upstream snapshot 0.9.0.58
  * Add bitvector functions and APN conversion functions
- Add test.diff to resolve compiler warning
* Wed Dec 23 2015 jengelh@inai.de
- Update to new upstream release 0.9.0
  * ipaccess: add OAP proto_ext (in design).
  * stats: Report stat item values
  * stats: Implement timer based reporting
  * stats/vty: Add stats configuration
  * stat/vty: Add vty_out_statistics_full to show all statistics
  * stats: Add vty_out_stat_item_group
  * LaPDm: Refuse SUSPEND/RESUME/RECONNECT in BTS mode
  * ns: Force a defined state when sending NS RESET
- Drop osmo-symbols.diff (solved better upstream),
  osmo-talloc.diff, osmo-talloc2.diff, osmo-talloc3.diff (solved
  upstream)
* Thu Sep 10 2015 jengelh@inai.de
- Update to new upstream release 0.8.3
  * Add G-RNTI derived TLLI types defined in 23.003
  * vty: Change API to have node installation be done by int
  * ipa: Properly parse LV stream of a ID_GET request
  * Add APN utility function to libosmogsm
  * gsm: Add A5/3-4 cipher support
  * bssgp: Handle BSSGP STATUS messages
- Add osmo-symbols.diff
* Sun Mar  1 2015 jengelh@inai.de
- Update to new upstream release 0.8.0
  * new Osmocom SIM card library
- Remove 0001-utils-resolve-compiler-warnings-on-implicit-declarat.patch,
  libosmocore_0_7_0_avoid_smscb_test_failure.patch,
  osmo-kasumi.diff, osmo-version.diff (no longer needed x4),
  rework osmo-talloc2.diff and add osmo-talloc3.diff after upstream
  conversion. Add osmo-pkgconfig.diff.
* Wed Feb 18 2015 normand@linux.vnet.ibm.com
- remove the previous patch about  ppc/ppc64 architectures
  as upstream suggesting that known to be not supported
  so explicitely add ExcludeArch in spec file.
* Wed Feb 18 2015 normand@linux.vnet.ibm.com
- avoid smscb test failure on ppc/ppc64 architectures
  with libosmocore_0_7_0_avoid_smscb_test_failure.patch
* Thu Oct  2 2014 jengelh@inai.de
- Update to new upstream release 0.7.0
  * No changelog was provided
  * osmocore gained GPRS NS interface support, and now provides a
  control interface library (libosmoctrl)
- Add osmo-kasumi.diff to fix link failure during `make check`
* Mon Jul 21 2014 jengelh@inai.de
- Update to new upstream release 0.6.6
  * No changelog was provided
- Remove 0001-osmo-arfcn-Return-something-from-the-method.patch,
  0002-utils-avoid-breaking-strict-aliasing.patch (no longer needed)
* Sun Jun  2 2013 jengelh@inai.de
- Update to new upstream release 0.6.0
  * No changelog was provided
- Add 0001-osmo-arfcn-Return-something-from-the-method.patch
  from upstream to provide fix for rpmlint errors
- Add 0001-utils-resolve-compiler-warnings-on-implicit-declarat.patch,
  0002-utils-avoid-breaking-strict-aliasing.patch to fix rpmlint
  warnings
* Sun Feb 17 2013 jengelh@inai.de
- Initial package (version 0.5.3) for build.opensuse.org
* Mon Oct 10 2011 jengelh@medozas.de
- Initial prototype (version 0.3.10)
