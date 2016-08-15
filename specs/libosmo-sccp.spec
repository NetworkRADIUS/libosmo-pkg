#
# spec file for package libosmo-sccp
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


Name:           libosmo-sccp
Summary:        Osmocom library for the A-bis interface between BTS and BSC
License:        AGPL-3.0+ and GPL-2.0+
Group:          Development/Libraries/C and C++
Version:        %{_version}
Release:        %{_release}
Url:            http://openbsc.osmocom.org/

#Git-Clone:	git://git.osmocom.org/libosmo-sccp
#Snapshot:      0.7.0
Source:         %name-%version.tar.bz2
Patch0:         0001-libosmo-sccp-build-fixes.patch
Patch1:         0002-libosmo-sccp-fix-pc-files.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake >= 1.6
BuildRequires:  libtool
BuildRequires:  xz
BuildRequires:  pkgconfig(libosmocore) >= 0.3.0
BuildRequires:  pkgconfig(libosmogsm)
BuildRequires:  pkgconfig(talloc)

%description
Osmocom library for the A-bis interface between BTS and BSC.

%package -n libosmo-xua
Summary:        Osmocom Message Transfer Part 2 User Adaptation library
License:        AGPL-3.0+
Group:          System/Libraries

%description -n libosmo-xua
M2UA (RFC 3331) provides an SCTP (RFC 3873) adaptation layer for the
seamless backhaul of MTP Level 2 user messages and service interface
across an IP network.

%package -n libosmo-xua-devel
Summary:        Development files for the Osmocom M2UA library
License:        AGPL-3.0+
Group:          Development/Libraries/C and C++
Requires:       libosmo-xua = %version

%description -n libosmo-xua-devel
M2UA provides an SCTP adaptation layer for MTP level 2 user messages
and service interface across an IP network.

This subpackage contains the development files for the Osmocom M2UA
library.

%package -n libosmo-mtp
Summary:        Osmocom Message Transfer Part library
License:        GPL-2.0+
Group:          System/Libraries

%description -n libosmo-mtp
The Message Transfer Part (MTP) is part of the Signaling System 7
(SS7) used for communication in Public Switched Telephone Networks.
MTP is responsible for reliable, unduplicated and in-sequence
transport of SS7 messages between communication partners.

%package -n libosmo-mtp-devel
Summary:        Development files for the Osmocom MTP library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       libosmo-mtp = %version

%description -n libosmo-mtp-devel
MTP is part of SS7 used for communication in Public Switched
Telephone Networks.

This subpackage contains the development files for the Osmocom MTP
library.

%package -n libosmo-sccp-devel
Summary:        Development files for the Osmocom SCCP library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       libosmo-sccp = %version

%description -n libosmo-sccp-devel
SCCP is a network layer protocol that provides routing, flow control,
segmentation, connection-orientation, and error correction facilities
in SS7 telecommunications networks.

This subpackage contains the development files for the Osmocom SCCP
library.

%prep
%setup -q
%patch -P 0 -P 1 -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
b="%buildroot"
make %{?_smp_mflags} install DESTDIR="$b"
find "$b/%_libdir" -type f -name "*.la" -delete
find "$b/%_libdir" -name "*sigtran*" -delete

%check
make %{?_smp_mflags} check

%post   -n libosmo-xua -p /sbin/ldconfig
%postun -n libosmo-xua -p /sbin/ldconfig
%post   -n libosmo-mtp -p /sbin/ldconfig
%postun -n libosmo-mtp -p /sbin/ldconfig
%post   -n libosmo-sccp -p /sbin/ldconfig
%postun -n libosmo-sccp -p /sbin/ldconfig

%files -n libosmo-xua
%defattr(-,root,root)
%_libdir/libosmo-xua*.so

%files -n libosmo-xua-devel
%defattr(-,root,root)
%dir %_includedir/osmocom
%_includedir/osmocom/sigtran/
%_libdir/libosmo-xua*.so

%files -n libosmo-mtp
%defattr(-,root,root)
%_libdir/libosmo-mtp*.so

%files -n libosmo-mtp-devel
%defattr(-,root,root)
%dir %_includedir/osmocom
%_includedir/osmocom/mtp/
%_libdir/libosmo-mtp*.so
%_libdir/pkgconfig/libosmo-mtp.pc

%files -n libosmo-sccp
%defattr(-,root,root)
%_libdir/libosmo-sccp*.so

%files -n libosmo-sccp-devel
%defattr(-,root,root)
%dir %_includedir/osmocom
%_includedir/osmocom/sccp/
%_libdir/pkgconfig/libosmo-sccp.pc

%changelog
* Thu Sep 10 2015 jengelh@inai.de
- Update to new upstream release 0.7.0
  * sccp: Allow to specify the context of the incoming message
  * mtp: Correct the pointcode mask
  * mtp: Add implementation from cellmgr
  * m3ua: Add the definition of the protocol data header
  * xua: Generalize the m2ua_msg and call it xua_msg
  * XUA: Move m2ua headers to sigtran, create xua_types.h
  and m3ua_types.h
  * sccp: Create sccp_create_cr and use it in the connection creation
* Mon Jul 21 2014 jengelh@inai.de
- Initial package (version 0.0.6.3) for build.opensuse.org
