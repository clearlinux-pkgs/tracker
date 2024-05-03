#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v10
# autospec commit: 5905be9
#
Name     : tracker
Version  : 3.7.3
Release  : 61
URL      : https://download.gnome.org/sources/tracker/3.7/tracker-3.7.3.tar.xz
Source0  : https://download.gnome.org/sources/tracker/3.7/tracker-3.7.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: tracker-bin = %{version}-%{release}
Requires: tracker-data = %{version}-%{release}
Requires: tracker-lib = %{version}-%{release}
Requires: tracker-libexec = %{version}-%{release}
Requires: tracker-license = %{version}-%{release}
Requires: tracker-locales = %{version}-%{release}
Requires: tracker-services = %{version}-%{release}
BuildRequires : bash-completion-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gstreamer-dev
BuildRequires : json-glib-dev
BuildRequires : libexif-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libunistring-dev
BuildRequires : pkgconfig(avahi-client)
BuildRequires : pkgconfig(avahi-glib)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(libsoup-3.0)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : pygobject
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
REQUIREMENTS
============
To build the documentation, you must have the gtk-doc
package installed. To rebuild the template files,
you must have the current version of the Tracker
header files installed.

%package bin
Summary: bin components for the tracker package.
Group: Binaries
Requires: tracker-data = %{version}-%{release}
Requires: tracker-libexec = %{version}-%{release}
Requires: tracker-license = %{version}-%{release}
Requires: tracker-services = %{version}-%{release}

%description bin
bin components for the tracker package.


%package data
Summary: data components for the tracker package.
Group: Data

%description data
data components for the tracker package.


%package dev
Summary: dev components for the tracker package.
Group: Development
Requires: tracker-lib = %{version}-%{release}
Requires: tracker-bin = %{version}-%{release}
Requires: tracker-data = %{version}-%{release}
Provides: tracker-devel = %{version}-%{release}
Requires: tracker = %{version}-%{release}

%description dev
dev components for the tracker package.


%package lib
Summary: lib components for the tracker package.
Group: Libraries
Requires: tracker-data = %{version}-%{release}
Requires: tracker-libexec = %{version}-%{release}
Requires: tracker-license = %{version}-%{release}

%description lib
lib components for the tracker package.


%package libexec
Summary: libexec components for the tracker package.
Group: Default
Requires: tracker-license = %{version}-%{release}

%description libexec
libexec components for the tracker package.


%package license
Summary: license components for the tracker package.
Group: Default

%description license
license components for the tracker package.


%package locales
Summary: locales components for the tracker package.
Group: Default

%description locales
locales components for the tracker package.


%package services
Summary: services components for the tracker package.
Group: Systemd services
Requires: systemd

%description services
services components for the tracker package.


%prep
%setup -q -n tracker-3.7.3
cd %{_builddir}/tracker-3.7.3
pushd ..
cp -a tracker-3.7.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1714758455
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman=false \
-Ddocs=false \
-Dsoup=soup3  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dman=false \
-Ddocs=false \
-Dsoup=soup3  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/tracker
cp %{_builddir}/tracker-%{version}/COPYING.GPL %{buildroot}/usr/share/package-licenses/tracker/33fabce185708a9b17df7a9f37c7ed44eddc7e48 || :
cp %{_builddir}/tracker-%{version}/COPYING.LGPL %{buildroot}/usr/share/package-licenses/tracker/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/tracker-%{version}/src/libtracker-common/COPYING.LIB %{buildroot}/usr/share/package-licenses/tracker/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/tracker-%{version}/src/libtracker-sparql/core/COPYING.LIB %{buildroot}/usr/share/package-licenses/tracker/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/tracker-%{version}/subprojects/gvdb/COPYING %{buildroot}/usr/share/package-licenses/tracker/e2f8b4d1f76ec319b3e525132de7fa2460cac845 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang tracker3
## install_append content
#mv %{buildroot}/etc/xdg %{buildroot}/usr/share/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/tracker-3.0/trackertestutils/__init__.py
/usr/lib64/tracker-3.0/trackertestutils/__main__.py
/usr/lib64/tracker-3.0/trackertestutils/await_file/__init__.py
/usr/lib64/tracker-3.0/trackertestutils/await_file/__main__.py
/usr/lib64/tracker-3.0/trackertestutils/dbusdaemon.py
/usr/lib64/tracker-3.0/trackertestutils/dconf.py
/usr/lib64/tracker-3.0/trackertestutils/helpers.py
/usr/lib64/tracker-3.0/trackertestutils/mainloop.py
/usr/lib64/tracker-3.0/trackertestutils/psutil_mini.py
/usr/lib64/tracker-3.0/trackertestutils/sandbox.py
/usr/lib64/tracker-3.0/trackertestutils/storehelper.py
/usr/lib64/tracker-3.0/trackertestutils/tracker-await-file
/usr/lib64/tracker-3.0/trackertestutils/tracker-sandbox

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/tracker3
/V3/usr/bin/tracker3-endpoint
/V3/usr/bin/tracker3-export
/V3/usr/bin/tracker3-help
/V3/usr/bin/tracker3-import
/V3/usr/bin/tracker3-sparql
/V3/usr/bin/tracker3-sql
/usr/bin/tracker3
/usr/bin/tracker3-endpoint
/usr/bin/tracker3-export
/usr/bin/tracker3-help
/usr/bin/tracker3-import
/usr/bin/tracker3-sparql
/usr/bin/tracker3-sql

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Tracker-3.0.typelib
/usr/share/bash-completion/completions/tracker3
/usr/share/dbus-1/services/org.freedesktop.portal.Tracker.service
/usr/share/gir-1.0/*.gir
/usr/share/tracker3/commands/tracker-endpoint.desktop
/usr/share/tracker3/commands/tracker-export.desktop
/usr/share/tracker3/commands/tracker-help.desktop
/usr/share/tracker3/commands/tracker-import.desktop
/usr/share/tracker3/commands/tracker-sparql.desktop
/usr/share/tracker3/commands/tracker-sql.desktop
/usr/share/vala/vapi/tracker-sparql-3.0.deps
/usr/share/vala/vapi/tracker-sparql-3.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/tracker-3.0/libtracker-sparql/tracker-batch.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-connection.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-cursor.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-endpoint-dbus.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-endpoint-http.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-endpoint.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-enums.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-error.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-namespace-manager.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-notifier.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-ontologies.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-resource.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-sparql-enum-types.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-sparql.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-statement.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-utils.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-version-generated.h
/usr/include/tracker-3.0/libtracker-sparql/tracker-version.h
/usr/lib64/libtracker-sparql-3.0.so
/usr/lib64/pkgconfig/tracker-sparql-3.0.pc
/usr/lib64/pkgconfig/tracker-testutils-3.0.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libtracker-sparql-3.0.so.0.703.0
/V3/usr/lib64/tracker-3.0/libtracker-http-soup3.so
/V3/usr/lib64/tracker-3.0/libtracker-parser-libicu.so
/usr/lib64/libtracker-sparql-3.0.so.0
/usr/lib64/libtracker-sparql-3.0.so.0.703.0
/usr/lib64/tracker-3.0/libtracker-http-soup3.so
/usr/lib64/tracker-3.0/libtracker-parser-libicu.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/tracker-xdg-portal-3
/usr/libexec/tracker-xdg-portal-3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tracker/33fabce185708a9b17df7a9f37c7ed44eddc7e48
/usr/share/package-licenses/tracker/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/tracker/e2f8b4d1f76ec319b3e525132de7fa2460cac845

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/tracker-xdg-portal-3.service

%files locales -f tracker3.lang
%defattr(-,root,root,-)

