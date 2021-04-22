#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tracker
Version  : 3.1.1
Release  : 34
URL      : https://download.gnome.org/sources/tracker/3.1/tracker-3.1.1.tar.xz
Source0  : https://download.gnome.org/sources/tracker/3.1/tracker-3.1.1.tar.xz
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
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gstreamer-dev
BuildRequires : json-glib-dev
BuildRequires : libexif-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libsoup-dev
BuildRequires : libunistring-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : systemd-dev

%description
The turtle files are created in this directory. For importing them into
tracker use:

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


%package doc
Summary: doc components for the tracker package.
Group: Documentation

%description doc
doc components for the tracker package.


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

%description services
services components for the tracker package.


%prep
%setup -q -n tracker-3.1.1
cd %{_builddir}/tracker-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619118792
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfts=false \
-Dfunctional_tests=false \
-Dman=false \
-Ddoc=false  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/tracker
cp %{_builddir}/tracker-3.1.1/COPYING.GPL %{buildroot}/usr/share/package-licenses/tracker/33fabce185708a9b17df7a9f37c7ed44eddc7e48
cp %{_builddir}/tracker-3.1.1/COPYING.LGPL %{buildroot}/usr/share/package-licenses/tracker/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/tracker-3.1.1/src/libtracker-common/COPYING.LIB %{buildroot}/usr/share/package-licenses/tracker/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/tracker-3.1.1/src/libtracker-data/COPYING.LIB %{buildroot}/usr/share/package-licenses/tracker/9a1929f4700d2407c70b507b3b2aaf6226a9543c
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang tracker3
## install_append content
#mv %{buildroot}/etc/xdg %{buildroot}/usr/share/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/tracker-3.0/trackertestutils/__init__.py
/usr/lib64/tracker-3.0/trackertestutils/__main__.py
/usr/lib64/tracker-3.0/trackertestutils/dbusdaemon.py
/usr/lib64/tracker-3.0/trackertestutils/dconf.py
/usr/lib64/tracker-3.0/trackertestutils/helpers.py
/usr/lib64/tracker-3.0/trackertestutils/mainloop.py
/usr/lib64/tracker-3.0/trackertestutils/psutil_mini.py
/usr/lib64/tracker-3.0/trackertestutils/sandbox.py
/usr/lib64/tracker-3.0/trackertestutils/storehelper.py
/usr/lib64/tracker-3.0/trackertestutils/tracker-sandbox

%files bin
%defattr(-,root,root,-)
/usr/bin/tracker3

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Tracker-3.0.typelib
/usr/share/bash-completion/completions/tracker3
/usr/share/dbus-1/services/org.freedesktop.portal.Tracker.service
/usr/share/gir-1.0/*.gir
/usr/share/tracker3/ontologies/nepomuk/30-nie.description
/usr/share/tracker3/ontologies/nepomuk/30-nie.ontology
/usr/share/tracker3/ontologies/nepomuk/31-nao.description
/usr/share/tracker3/ontologies/nepomuk/31-nao.ontology
/usr/share/tracker3/ontologies/nepomuk/32-nco.description
/usr/share/tracker3/ontologies/nepomuk/32-nco.ontology
/usr/share/tracker3/ontologies/nepomuk/33-nfo.description
/usr/share/tracker3/ontologies/nepomuk/33-nfo.ontology
/usr/share/tracker3/ontologies/nepomuk/38-nmm.description
/usr/share/tracker3/ontologies/nepomuk/38-nmm.ontology
/usr/share/tracker3/ontologies/nepomuk/41-mfo.description
/usr/share/tracker3/ontologies/nepomuk/41-mfo.ontology
/usr/share/tracker3/ontologies/nepomuk/90-tracker.description
/usr/share/tracker3/ontologies/nepomuk/90-tracker.ontology
/usr/share/tracker3/ontologies/nepomuk/92-slo.description
/usr/share/tracker3/ontologies/nepomuk/92-slo.ontology
/usr/share/tracker3/ontologies/nepomuk/93-libosinfo.description
/usr/share/tracker3/ontologies/nepomuk/93-libosinfo.ontology
/usr/share/tracker3/stop-words/stopwords.cs
/usr/share/tracker3/stop-words/stopwords.da
/usr/share/tracker3/stop-words/stopwords.de
/usr/share/tracker3/stop-words/stopwords.en
/usr/share/tracker3/stop-words/stopwords.es
/usr/share/tracker3/stop-words/stopwords.fi
/usr/share/tracker3/stop-words/stopwords.fr
/usr/share/tracker3/stop-words/stopwords.hu
/usr/share/tracker3/stop-words/stopwords.it
/usr/share/tracker3/stop-words/stopwords.nb
/usr/share/tracker3/stop-words/stopwords.nl
/usr/share/tracker3/stop-words/stopwords.pt
/usr/share/tracker3/stop-words/stopwords.ru
/usr/share/tracker3/stop-words/stopwords.sv
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

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libtracker-sparql-3/TrackerBatch.html
/usr/share/gtk-doc/html/libtracker-sparql-3/TrackerEndpoint.html
/usr/share/gtk-doc/html/libtracker-sparql-3/TrackerNamespaceManager.html
/usr/share/gtk-doc/html/libtracker-sparql-3/TrackerNotifier.html
/usr/share/gtk-doc/html/libtracker-sparql-3/TrackerResource.html
/usr/share/gtk-doc/html/libtracker-sparql-3/TrackerSparqlConnection.html
/usr/share/gtk-doc/html/libtracker-sparql-3/TrackerSparqlCursor.html
/usr/share/gtk-doc/html/libtracker-sparql-3/TrackerSparqlStatement.html
/usr/share/gtk-doc/html/libtracker-sparql-3/accompanying-metadata.html
/usr/share/gtk-doc/html/libtracker-sparql-3/annotation-glossary.html
/usr/share/gtk-doc/html/libtracker-sparql-3/api-index-3-0.html
/usr/share/gtk-doc/html/libtracker-sparql-3/api-index-3-1.html
/usr/share/gtk-doc/html/libtracker-sparql-3/api-index-deprecated.html
/usr/share/gtk-doc/html/libtracker-sparql-3/api-index-full.html
/usr/share/gtk-doc/html/libtracker-sparql-3/base-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql-3/blank-nodes.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch27s02.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch27s03.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s02.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s03.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s04.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s05.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s06.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s07.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s08.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s09.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s10.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s11.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s12.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ch28s13.html
/usr/share/gtk-doc/html/libtracker-sparql-3/creating-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql-3/date-time-functions.html
/usr/share/gtk-doc/html/libtracker-sparql-3/dc.html
/usr/share/gtk-doc/html/libtracker-sparql-3/defining-cardinality.html
/usr/share/gtk-doc/html/libtracker-sparql-3/defining-classes.html
/usr/share/gtk-doc/html/libtracker-sparql-3/defining-fts-indexes.html
/usr/share/gtk-doc/html/libtracker-sparql-3/defining-indexes.html
/usr/share/gtk-doc/html/libtracker-sparql-3/defining-properties.html
/usr/share/gtk-doc/html/libtracker-sparql-3/defining-uniqueness.html
/usr/share/gtk-doc/html/libtracker-sparql-3/fts-functions.html
/usr/share/gtk-doc/html/libtracker-sparql-3/full-text-search.html
/usr/share/gtk-doc/html/libtracker-sparql-3/geo-functions.html
/usr/share/gtk-doc/html/libtracker-sparql-3/graphs.html
/usr/share/gtk-doc/html/libtracker-sparql-3/home.png
/usr/share/gtk-doc/html/libtracker-sparql-3/id-functions.html
/usr/share/gtk-doc/html/libtracker-sparql-3/ids-and-iris.html
/usr/share/gtk-doc/html/libtracker-sparql-3/index.html
/usr/share/gtk-doc/html/libtracker-sparql-3/left-insensitive.png
/usr/share/gtk-doc/html/libtracker-sparql-3/left.png
/usr/share/gtk-doc/html/libtracker-sparql-3/libtracker-sparql-3.devhelp2
/usr/share/gtk-doc/html/libtracker-sparql-3/libtracker-sparql-TrackerSparqlError.html
/usr/share/gtk-doc/html/libtracker-sparql-3/libtracker-sparql-Utilities.html
/usr/share/gtk-doc/html/libtracker-sparql-3/libtracker-sparql-Version-Information.html
/usr/share/gtk-doc/html/libtracker-sparql-3/libtracker-sparql-reference.html
/usr/share/gtk-doc/html/libtracker-sparql-3/nrl.html
/usr/share/gtk-doc/html/libtracker-sparql-3/parameters.html
/usr/share/gtk-doc/html/libtracker-sparql-3/predefined-elements.html
/usr/share/gtk-doc/html/libtracker-sparql-3/property-functions.html
/usr/share/gtk-doc/html/libtracker-sparql-3/rdf.html
/usr/share/gtk-doc/html/libtracker-sparql-3/right-insensitive.png
/usr/share/gtk-doc/html/libtracker-sparql-3/right.png
/usr/share/gtk-doc/html/libtracker-sparql-3/sparql-and-tracker.html
/usr/share/gtk-doc/html/libtracker-sparql-3/sparql-functions.html
/usr/share/gtk-doc/html/libtracker-sparql-3/string-functions.html
/usr/share/gtk-doc/html/libtracker-sparql-3/style.css
/usr/share/gtk-doc/html/libtracker-sparql-3/syntax.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-examples-readonly.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-examples-writeonly-with-blank-nodes.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-examples-writeonly.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-examples.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-limits.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-migrating-1-to-2.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-migrating-2-to-3.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-ontologies.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-overview-connection-methods.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-overview-flatpak.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-overview.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-perf-avoid-contains.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-perf-graphs.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-perf-negated-property-path.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-perf-unrestricted-predicates.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-perf-use-statements.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-performance.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-tutorial-rdf-triples.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-tutorial-sparql.html
/usr/share/gtk-doc/html/libtracker-sparql-3/tracker-tutorial.html
/usr/share/gtk-doc/html/libtracker-sparql-3/triple-graph-1.png
/usr/share/gtk-doc/html/libtracker-sparql-3/triple-graph-2.png
/usr/share/gtk-doc/html/libtracker-sparql-3/triple-graph-3.png
/usr/share/gtk-doc/html/libtracker-sparql-3/up-insensitive.png
/usr/share/gtk-doc/html/libtracker-sparql-3/up.png
/usr/share/gtk-doc/html/libtracker-sparql-3/updating-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql-3/uri-functions.html
/usr/share/gtk-doc/html/libtracker-sparql-3/xsd.html
/usr/share/gtk-doc/html/ontology-3/home.png
/usr/share/gtk-doc/html/ontology-3/icon-deprecated.svg
/usr/share/gtk-doc/html/ontology-3/icon-fulltextindexed.svg
/usr/share/gtk-doc/html/ontology-3/icon-multivalue.svg
/usr/share/gtk-doc/html/ontology-3/icon-notify.svg
/usr/share/gtk-doc/html/ontology-3/icon-superproperty.svg
/usr/share/gtk-doc/html/ontology-3/index.html
/usr/share/gtk-doc/html/ontology-3/left-insensitive.png
/usr/share/gtk-doc/html/ontology-3/left.png
/usr/share/gtk-doc/html/ontology-3/mfo.html
/usr/share/gtk-doc/html/ontology-3/nao.html
/usr/share/gtk-doc/html/ontology-3/nco.html
/usr/share/gtk-doc/html/ontology-3/nfo.html
/usr/share/gtk-doc/html/ontology-3/nie.html
/usr/share/gtk-doc/html/ontology-3/nmm.html
/usr/share/gtk-doc/html/ontology-3/ontology-3.devhelp2
/usr/share/gtk-doc/html/ontology-3/ontology.html
/usr/share/gtk-doc/html/ontology-3/osinfo.html
/usr/share/gtk-doc/html/ontology-3/overview.html
/usr/share/gtk-doc/html/ontology-3/right-insensitive.png
/usr/share/gtk-doc/html/ontology-3/right.png
/usr/share/gtk-doc/html/ontology-3/slo.html
/usr/share/gtk-doc/html/ontology-3/style.css
/usr/share/gtk-doc/html/ontology-3/tracker.html
/usr/share/gtk-doc/html/ontology-3/up-insensitive.png
/usr/share/gtk-doc/html/ontology-3/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtracker-sparql-3.0.so.0
/usr/lib64/libtracker-sparql-3.0.so.0.101.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/tracker-xdg-portal-3
/usr/libexec/tracker3/endpoint
/usr/libexec/tracker3/export
/usr/libexec/tracker3/help
/usr/libexec/tracker3/import
/usr/libexec/tracker3/sparql
/usr/libexec/tracker3/sql

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tracker/33fabce185708a9b17df7a9f37c7ed44eddc7e48
/usr/share/package-licenses/tracker/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/tracker-xdg-portal-3.service

%files locales -f tracker3.lang
%defattr(-,root,root,-)

