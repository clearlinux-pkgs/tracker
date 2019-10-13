#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tracker
Version  : 2.3.1
Release  : 25
URL      : https://download.gnome.org/sources/tracker/2.3/tracker-2.3.1.tar.xz
Source0  : https://download.gnome.org/sources/tracker/2.3/tracker-2.3.1.tar.xz
Summary  : Desktop-neutral user information store, search tool and indexer
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: tracker-bin = %{version}-%{release}
Requires: tracker-data = %{version}-%{release}
Requires: tracker-lib = %{version}-%{release}
Requires: tracker-libexec = %{version}-%{release}
Requires: tracker-license = %{version}-%{release}
Requires: tracker-locales = %{version}-%{release}
Requires: tracker-man = %{version}-%{release}
BuildRequires : bash-completion-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gobject-introspection-dev
BuildRequires : gstreamer-dev
BuildRequires : json-glib-dev
BuildRequires : libexif-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libsoup-dev
BuildRequires : libunistring-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : upower-dev
Patch1: 0001-don-t-autostart-by-default.patch

%description
RSS reader application
======================
Example of an application using the tracker SparQL interface to query
data and set other data.

%package bin
Summary: bin components for the tracker package.
Group: Binaries
Requires: tracker-data = %{version}-%{release}
Requires: tracker-libexec = %{version}-%{release}
Requires: tracker-license = %{version}-%{release}

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
Requires: tracker = %{version}-%{release}

%description dev
dev components for the tracker package.


%package extras
Summary: extras components for the tracker package.
Group: Default

%description extras
extras components for the tracker package.


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


%package man
Summary: man components for the tracker package.
Group: Default

%description man
man components for the tracker package.


%prep
%setup -q -n tracker-2.3.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570993250
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfts=false \
-Dfunctional_tests=false \
-Dsystemd_user_services=/usr/lib/systemd/user  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/tracker
cp COPYING.GPL %{buildroot}/usr/share/package-licenses/tracker/COPYING.GPL
cp COPYING.LGPL %{buildroot}/usr/share/package-licenses/tracker/COPYING.LGPL
cp src/libtracker-common/COPYING.LIB %{buildroot}/usr/share/package-licenses/tracker/src_libtracker-common_COPYING.LIB
cp src/libtracker-data/COPYING.LIB %{buildroot}/usr/share/package-licenses/tracker/src_libtracker-data_COPYING.LIB
cp src/libtracker-miner/COPYING.LIB %{buildroot}/usr/share/package-licenses/tracker/src_libtracker-miner_COPYING.LIB
cp utils/ontology/resources/LICENSE.txt %{buildroot}/usr/share/package-licenses/tracker/utils_ontology_resources_LICENSE.txt
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang tracker

%files
%defattr(-,root,root,-)
/usr/lib64/tracker-2.0/trackertestutils/__init__.py
/usr/lib64/tracker-2.0/trackertestutils/dconf.py
/usr/lib64/tracker-2.0/trackertestutils/helpers.py
/usr/lib64/tracker-2.0/trackertestutils/mainloop.py

%files bin
%defattr(-,root,root,-)
/usr/bin/tracker

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Tracker-2.0.typelib
/usr/lib64/girepository-1.0/TrackerControl-2.0.typelib
/usr/lib64/girepository-1.0/TrackerMiner-2.0.typelib
/usr/share/bash-completion/completions/tracker
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker.DB.gschema.xml
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker.FTS.gschema.xml
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker.Store.gschema.xml
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker.enums.xml
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker.gschema.xml
/usr/share/tracker/domain-ontologies/default.rule
/usr/share/tracker/ontologies/nepomuk/30-nie.description
/usr/share/tracker/ontologies/nepomuk/30-nie.ontology
/usr/share/tracker/ontologies/nepomuk/32-nco.description
/usr/share/tracker/ontologies/nepomuk/32-nco.ontology
/usr/share/tracker/ontologies/nepomuk/33-nfo.description
/usr/share/tracker/ontologies/nepomuk/33-nfo.ontology
/usr/share/tracker/ontologies/nepomuk/34-nmo.description
/usr/share/tracker/ontologies/nepomuk/34-nmo.ontology
/usr/share/tracker/ontologies/nepomuk/35-ncal.description
/usr/share/tracker/ontologies/nepomuk/35-ncal.ontology
/usr/share/tracker/ontologies/nepomuk/36-scal.description
/usr/share/tracker/ontologies/nepomuk/36-scal.ontology
/usr/share/tracker/ontologies/nepomuk/37-nid3.description
/usr/share/tracker/ontologies/nepomuk/37-nid3.ontology
/usr/share/tracker/ontologies/nepomuk/38-nmm.description
/usr/share/tracker/ontologies/nepomuk/38-nmm.ontology
/usr/share/tracker/ontologies/nepomuk/39-mto.description
/usr/share/tracker/ontologies/nepomuk/39-mto.ontology
/usr/share/tracker/ontologies/nepomuk/40-mlo.description
/usr/share/tracker/ontologies/nepomuk/40-mlo.ontology
/usr/share/tracker/ontologies/nepomuk/41-mfo.description
/usr/share/tracker/ontologies/nepomuk/41-mfo.ontology
/usr/share/tracker/ontologies/nepomuk/89-mtp.description
/usr/share/tracker/ontologies/nepomuk/89-mtp.ontology
/usr/share/tracker/ontologies/nepomuk/90-tracker.description
/usr/share/tracker/ontologies/nepomuk/90-tracker.ontology
/usr/share/tracker/ontologies/nepomuk/91-maemo.description
/usr/share/tracker/ontologies/nepomuk/91-maemo.ontology
/usr/share/tracker/ontologies/nepomuk/92-slo.description
/usr/share/tracker/ontologies/nepomuk/92-slo.ontology
/usr/share/tracker/ontologies/nepomuk/93-libosinfo.description
/usr/share/tracker/ontologies/nepomuk/93-libosinfo.ontology
/usr/share/tracker/stop-words/stopwords.da
/usr/share/tracker/stop-words/stopwords.de
/usr/share/tracker/stop-words/stopwords.en
/usr/share/tracker/stop-words/stopwords.es
/usr/share/tracker/stop-words/stopwords.fi
/usr/share/tracker/stop-words/stopwords.fr
/usr/share/tracker/stop-words/stopwords.hu
/usr/share/tracker/stop-words/stopwords.it
/usr/share/tracker/stop-words/stopwords.nb
/usr/share/tracker/stop-words/stopwords.nl
/usr/share/tracker/stop-words/stopwords.pt
/usr/share/tracker/stop-words/stopwords.ru
/usr/share/tracker/stop-words/stopwords.sv
/usr/share/tracker/tracker-backup.xml
/usr/share/tracker/tracker-miner.xml
/usr/share/tracker/tracker-resources.xml
/usr/share/tracker/tracker-statistics.xml
/usr/share/tracker/tracker-status.xml
/usr/share/vala/vapi/tracker-control-2.0.deps
/usr/share/vala/vapi/tracker-control-2.0.vapi
/usr/share/vala/vapi/tracker-miner-2.0.deps
/usr/share/vala/vapi/tracker-miner-2.0.vapi
/usr/share/vala/vapi/tracker-sparql-2.0.deps
/usr/share/vala/vapi/tracker-sparql-2.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/tracker-2.0/libtracker-control/tracker-control.h
/usr/include/tracker-2.0/libtracker-control/tracker-miner-manager.h
/usr/include/tracker-2.0/libtracker-miner/tracker-data-provider.h
/usr/include/tracker-2.0/libtracker-miner/tracker-decorator-fs.h
/usr/include/tracker-2.0/libtracker-miner/tracker-decorator.h
/usr/include/tracker-2.0/libtracker-miner/tracker-indexing-tree.h
/usr/include/tracker-2.0/libtracker-miner/tracker-miner-enum-types.h
/usr/include/tracker-2.0/libtracker-miner/tracker-miner-enums.h
/usr/include/tracker-2.0/libtracker-miner/tracker-miner-fs.h
/usr/include/tracker-2.0/libtracker-miner/tracker-miner-object.h
/usr/include/tracker-2.0/libtracker-miner/tracker-miner-online.h
/usr/include/tracker-2.0/libtracker-miner/tracker-miner-proxy.h
/usr/include/tracker-2.0/libtracker-miner/tracker-miner.h
/usr/include/tracker-2.0/libtracker-sparql/tracker-generated.h
/usr/include/tracker-2.0/libtracker-sparql/tracker-namespace-manager.h
/usr/include/tracker-2.0/libtracker-sparql/tracker-notifier.h
/usr/include/tracker-2.0/libtracker-sparql/tracker-ontologies.h
/usr/include/tracker-2.0/libtracker-sparql/tracker-resource.h
/usr/include/tracker-2.0/libtracker-sparql/tracker-sparql.h
/usr/include/tracker-2.0/libtracker-sparql/tracker-version.h
/usr/lib64/libtracker-control-2.0.so
/usr/lib64/libtracker-miner-2.0.so
/usr/lib64/libtracker-sparql-2.0.so
/usr/lib64/pkgconfig/tracker-control-2.0.pc
/usr/lib64/pkgconfig/tracker-miner-2.0.pc
/usr/lib64/pkgconfig/tracker-sparql-2.0.pc

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/user/tracker-store.service
/usr/share/dbus-1/services/org.freedesktop.Tracker1.service

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtracker-control-2.0.so.0
/usr/lib64/libtracker-control-2.0.so.0.301.0
/usr/lib64/libtracker-miner-2.0.so.0
/usr/lib64/libtracker-miner-2.0.so.0.301.0
/usr/lib64/libtracker-sparql-2.0.so.0
/usr/lib64/libtracker-sparql-2.0.so.0.301.0
/usr/lib64/tracker-2.0/libtracker-data.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/tracker-store

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tracker/COPYING.GPL
/usr/share/package-licenses/tracker/COPYING.LGPL
/usr/share/package-licenses/tracker/src_libtracker-common_COPYING.LIB
/usr/share/package-licenses/tracker/src_libtracker-data_COPYING.LIB
/usr/share/package-licenses/tracker/src_libtracker-miner_COPYING.LIB
/usr/share/package-licenses/tracker/utils_ontology_resources_LICENSE.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tracker-daemon.1
/usr/share/man/man1/tracker-index.1
/usr/share/man/man1/tracker-info.1
/usr/share/man/man1/tracker-reset.1
/usr/share/man/man1/tracker-search.1
/usr/share/man/man1/tracker-sparql.1
/usr/share/man/man1/tracker-sql.1
/usr/share/man/man1/tracker-status.1
/usr/share/man/man1/tracker-store.1
/usr/share/man/man1/tracker-tag.1

%files locales -f tracker.lang
%defattr(-,root,root,-)

