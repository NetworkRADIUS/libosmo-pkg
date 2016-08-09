#
# spec file for package libosmo-abis
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libosmo-abis
Version:        %{_version}
Release:        %{_release}
Summary:        Osmocom library for A-bis interface between BTS and BSC
License:        AGPL-3.0+ and GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://openbsc.osmocom.org/trac/wiki/libosmo-abis

#Git-Clone:	git://git.osmocom.org/libosmo-abis
#Snapshot:	0.3.1
Source:         %name-%version.tar.bz2
Patch1:         0001-libosmo-abis-talloc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake >= 1.6
#BuildRequires:  dahdi-linux-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(libosmocore) >= 0.3.0
BuildRequires:  pkgconfig(libosmogsm) >= 0.3.10
BuildRequires:  pkgconfig(libosmovty) >= 0.3.0
BuildRequires:  pkgconfig(ortp) >= 0.13.1

%description
In GSM, A-bis is a BSS-internal interface link between the BTS and
BSC. This interface allows control of the radio equipment and radio
frequency allocation in the BTS.

%package -n libosmo-abis-devel
Summary:        Development files for the Osmocom A-bis core library
License:        AGPL-3.0+
Group:          Development/Libraries/C and C++
Requires:       libosmo-abis = %version
Requires:       libosmocore-devel >= 0.3.0
Requires:       libosmogsm-devel >= 0.3.10

%description -n libosmo-abis-devel
In GSM, A-bis is a BSS-internal interface link between the BTS and
BSC. This interface allows control of the radio equipment and radio
frequency allocation in the BTS.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmoabis.

%package -n libosmo-trau

Summary:        Osmocom TRAU (E1/RTP) library
License:        GPL-2.0+
Group:          System/Libraries

%description -n libosmo-trau
The Transcoder Rate Adaptor Unit enables the use of lower rates (32,
16 or 8 kbps) over the A-bis interface instead of the 64 kbps ISDN
rate for which the Mobile Switching Center (MSC) is designed.

%package -n libosmo-trau-devel
Summary:        Development files for the Osmocom TRAU (E1/RTP) library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       libosmo-trau = %version

%description -n libosmo-trau-devel
The Transcoder Rate Adaptor Unit enables the use of lower bitrates
over the A-bis interface instead of the 64 kbps design rate of the
MSC.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmotrau.

%prep
%setup -q
%patch -P 1 -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
b="%buildroot"
make %{?_smp_mflags} install DESTDIR="$b"
find "$b/%_libdir" -type f -name "*.la" -delete

%check
make %{?_smp_mflags} check

%post   -n libosmo-abis -p /sbin/ldconfig
%postun -n libosmo-abis -p /sbin/ldconfig
%post   -n libosmo-trau -p /sbin/ldconfig
%postun -n libosmo-trau -p /sbin/ldconfig

%files -n libosmo-abis
%defattr(-,root,root)
%_libdir/libosmoabis.so.5*

%files -n libosmo-abis-devel
%defattr(-,root,root)
%doc COPYING
%dir %_includedir/osmocom
%_includedir/osmocom/abis/
%_libdir/libosmoabis.so
%_libdir/pkgconfig/libosmoabis.pc

%files -n libosmo-trau
%defattr(-,root,root)
%_libdir/libosmotrau.so.1*

%files -n libosmo-trau-devel
%defattr(-,root,root)
%doc COPYING
%dir %_includedir/osmocom
%_includedir/osmocom/trau
%_libdir/libosmotrau.so
%_libdir/pkgconfig/libosmotrau.pc

%changelog
* Thu Apr  2 2015 jengelh@inai.de
- Add 0001-build-resolve-compiler-warnings.patch
* Sun Mar  1 2015 jengelh@inai.de
- Update to new upstream release 0.3.1
  * No changelog was provided, again
* Thu Oct  2 2014 jengelh@inai.de
- Update to new upstream release 0.3.0
  * No changelog was provided
* Mon Jul 21 2014 jengelh@inai.de
- Update to new upstream release 0.2.0
  * No changelog was provided
- Remove 0001-lapd-Do-not-override-t203_sec-initialization.patch,
  0002-misdn-Set-ret-to-0-when-using-the-LAPD-from-userspac.patch
  (no longer needed)
* Sun Jun  2 2013 jengelh@inai.de
- Add 0001-lapd-Do-not-override-t203_sec-initialization.patch,
  0002-misdn-Set-ret-to-0-when-using-the-LAPD-from-userspac.patch
* Fri Feb 22 2013 jengelh@inai.de
- Initial package (version 0.1.5) for build.opensuse.org
