#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tracker
Version  : 2.0.3
Release  : 5
URL      : https://download.gnome.org/sources/tracker/2.0/tracker-2.0.3.tar.xz
Source0  : https://download.gnome.org/sources/tracker/2.0/tracker-2.0.3.tar.xz
Summary  : A library to monitor/control tracker miners
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: tracker-bin
Requires: tracker-config
Requires: tracker-data
Requires: tracker-lib
Requires: tracker-doc
Requires: tracker-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : json-glib-dev
BuildRequires : libexif-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libsoup-dev
BuildRequires : libunistring-dev
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : python3
Patch1: 0001-don-t-autostart-by-default.patch
Patch2: build.patch

%description
1 Introduction
Tracker is a search engine and that allows the user to find their
data as fast as possible. Users can search for their files and
search for content in their files too.

%package bin
Summary: bin components for the tracker package.
Group: Binaries
Requires: tracker-data
Requires: tracker-config

%description bin
bin components for the tracker package.


%package config
Summary: config components for the tracker package.
Group: Default

%description config
config components for the tracker package.


%package data
Summary: data components for the tracker package.
Group: Data

%description data
data components for the tracker package.


%package dev
Summary: dev components for the tracker package.
Group: Development
Requires: tracker-lib
Requires: tracker-bin
Requires: tracker-data
Provides: tracker-devel

%description dev
dev components for the tracker package.


%package doc
Summary: doc components for the tracker package.
Group: Documentation

%description doc
doc components for the tracker package.


%package extras
Summary: extras components for the tracker package.
Group: Default

%description extras
extras components for the tracker package.


%package lib
Summary: lib components for the tracker package.
Group: Libraries
Requires: tracker-data

%description lib
lib components for the tracker package.


%package locales
Summary: locales components for the tracker package.
Group: Default

%description locales
locales components for the tracker package.


%prep
%setup -q -n tracker-2.0.3
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518033438
%configure --disable-static --enable-minimal --enable-tracker-fts=no --enable-icu-charset-detection=no --disable-functional-tests
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1518033438
rm -rf %{buildroot}
%make_install
%find_lang tracker
## make_install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/.
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tracker
/usr/libexec/tracker-store

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/user/tracker-store.service

%files data
%defattr(-,root,root,-)
%exclude /usr/share/dbus-1/services/org.freedesktop.Tracker1.service
%exclude /usr/share/xdg/autostart/tracker-store.desktop
/usr/lib64/girepository-1.0/Tracker-2.0.typelib
/usr/lib64/girepository-1.0/TrackerControl-2.0.typelib
/usr/lib64/girepository-1.0/TrackerMiner-2.0.typelib
/usr/share/bash-completion/completions/tracker
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.freedesktop.Tracker.DB.gschema.xml
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/libtracker-control/TrackerMinerManager.html
/usr/share/gtk-doc/html/libtracker-control/annotation-glossary.html
/usr/share/gtk-doc/html/libtracker-control/ch01.html
/usr/share/gtk-doc/html/libtracker-control/home.png
/usr/share/gtk-doc/html/libtracker-control/index.html
/usr/share/gtk-doc/html/libtracker-control/left-insensitive.png
/usr/share/gtk-doc/html/libtracker-control/left.png
/usr/share/gtk-doc/html/libtracker-control/libtracker-control.devhelp2
/usr/share/gtk-doc/html/libtracker-control/libtracker-miner-reference.html
/usr/share/gtk-doc/html/libtracker-control/right-insensitive.png
/usr/share/gtk-doc/html/libtracker-control/right.png
/usr/share/gtk-doc/html/libtracker-control/style.css
/usr/share/gtk-doc/html/libtracker-control/tracker-migrating-1-to-2.html
/usr/share/gtk-doc/html/libtracker-control/up-insensitive.png
/usr/share/gtk-doc/html/libtracker-control/up.png
/usr/share/gtk-doc/html/libtracker-miner/TrackerDataProvider.html
/usr/share/gtk-doc/html/libtracker-miner/TrackerDecorator.html
/usr/share/gtk-doc/html/libtracker-miner/TrackerDecoratorFS.html
/usr/share/gtk-doc/html/libtracker-miner/TrackerIndexingTree.html
/usr/share/gtk-doc/html/libtracker-miner/TrackerMiner.html
/usr/share/gtk-doc/html/libtracker-miner/TrackerMinerFS.html
/usr/share/gtk-doc/html/libtracker-miner/TrackerMinerOnline.html
/usr/share/gtk-doc/html/libtracker-miner/TrackerMinerProxy.html
/usr/share/gtk-doc/html/libtracker-miner/annotation-glossary.html
/usr/share/gtk-doc/html/libtracker-miner/ch02.html
/usr/share/gtk-doc/html/libtracker-miner/ch03.html
/usr/share/gtk-doc/html/libtracker-miner/ch04.html
/usr/share/gtk-doc/html/libtracker-miner/ch05s02.html
/usr/share/gtk-doc/html/libtracker-miner/ch05s03.html
/usr/share/gtk-doc/html/libtracker-miner/ch05s04.html
/usr/share/gtk-doc/html/libtracker-miner/ch05s05.html
/usr/share/gtk-doc/html/libtracker-miner/ch05s06.html
/usr/share/gtk-doc/html/libtracker-miner/ch05s07.html
/usr/share/gtk-doc/html/libtracker-miner/home.png
/usr/share/gtk-doc/html/libtracker-miner/index.html
/usr/share/gtk-doc/html/libtracker-miner/left-insensitive.png
/usr/share/gtk-doc/html/libtracker-miner/left.png
/usr/share/gtk-doc/html/libtracker-miner/libtracker-miner-Enumerations.html
/usr/share/gtk-doc/html/libtracker-miner/libtracker-miner-TrackerFileDataProvider.html
/usr/share/gtk-doc/html/libtracker-miner/libtracker-miner-reference.html
/usr/share/gtk-doc/html/libtracker-miner/libtracker-miner.devhelp2
/usr/share/gtk-doc/html/libtracker-miner/right-insensitive.png
/usr/share/gtk-doc/html/libtracker-miner/right.png
/usr/share/gtk-doc/html/libtracker-miner/style.css
/usr/share/gtk-doc/html/libtracker-miner/tracker-migrating-1-to-2.html
/usr/share/gtk-doc/html/libtracker-miner/tracker-overview-compiling.html
/usr/share/gtk-doc/html/libtracker-miner/tracker-overview.html
/usr/share/gtk-doc/html/libtracker-miner/up-insensitive.png
/usr/share/gtk-doc/html/libtracker-miner/up.png
/usr/share/gtk-doc/html/libtracker-sparql/TrackerNotifier.html
/usr/share/gtk-doc/html/libtracker-sparql/TrackerResource.html
/usr/share/gtk-doc/html/libtracker-sparql/TrackerSparqlBuilder.html
/usr/share/gtk-doc/html/libtracker-sparql/TrackerSparqlConnection.html
/usr/share/gtk-doc/html/libtracker-sparql/TrackerSparqlCursor.html
/usr/share/gtk-doc/html/libtracker-sparql/accompanying-metadata.html
/usr/share/gtk-doc/html/libtracker-sparql/annotation-glossary.html
/usr/share/gtk-doc/html/libtracker-sparql/base-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/ch18s02.html
/usr/share/gtk-doc/html/libtracker-sparql/ch18s03.html
/usr/share/gtk-doc/html/libtracker-sparql/creating-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/dc-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/defining-cardinality.html
/usr/share/gtk-doc/html/libtracker-sparql/defining-classes.html
/usr/share/gtk-doc/html/libtracker-sparql/defining-fts-indexes.html
/usr/share/gtk-doc/html/libtracker-sparql/defining-indexes.html
/usr/share/gtk-doc/html/libtracker-sparql/defining-properties.html
/usr/share/gtk-doc/html/libtracker-sparql/defining-uniqueness.html
/usr/share/gtk-doc/html/libtracker-sparql/home.png
/usr/share/gtk-doc/html/libtracker-sparql/index.html
/usr/share/gtk-doc/html/libtracker-sparql/left-insensitive.png
/usr/share/gtk-doc/html/libtracker-sparql/left.png
/usr/share/gtk-doc/html/libtracker-sparql/libtracker-sparql-TrackerNamespaceManager.html
/usr/share/gtk-doc/html/libtracker-sparql/libtracker-sparql-Utilities.html
/usr/share/gtk-doc/html/libtracker-sparql/libtracker-sparql-Version-Information.html
/usr/share/gtk-doc/html/libtracker-sparql/libtracker-sparql-reference.html
/usr/share/gtk-doc/html/libtracker-sparql/libtracker-sparql.devhelp2
/usr/share/gtk-doc/html/libtracker-sparql/nao-Tag.html
/usr/share/gtk-doc/html/libtracker-sparql/nao-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/nrl-InverseFunctionalProperty.html
/usr/share/gtk-doc/html/libtracker-sparql/nrl-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/predefined-elements.html
/usr/share/gtk-doc/html/libtracker-sparql/private-daemons.html
/usr/share/gtk-doc/html/libtracker-sparql/rdf-Property.html
/usr/share/gtk-doc/html/libtracker-sparql/rdf-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/rdfs-Class.html
/usr/share/gtk-doc/html/libtracker-sparql/rdfs-Literal.html
/usr/share/gtk-doc/html/libtracker-sparql/rdfs-Resource.html
/usr/share/gtk-doc/html/libtracker-sparql/recommendations.html
/usr/share/gtk-doc/html/libtracker-sparql/right-insensitive.png
/usr/share/gtk-doc/html/libtracker-sparql/right.png
/usr/share/gtk-doc/html/libtracker-sparql/style.css
/usr/share/gtk-doc/html/libtracker-sparql/tracker-Namespace.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-Ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-examples-builder.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-examples-readonly.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-examples-writeonly-with-blank-nodes.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-examples-writeonly.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-examples.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-migrating-1-to-2.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-ontologies.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-overview-compiling.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-overview-connection-methods.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-overview-environment-variables.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-overview.html
/usr/share/gtk-doc/html/libtracker-sparql/tracker-private-store.html
/usr/share/gtk-doc/html/libtracker-sparql/up-insensitive.png
/usr/share/gtk-doc/html/libtracker-sparql/up.png
/usr/share/gtk-doc/html/libtracker-sparql/updating-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/xsd-boolean.html
/usr/share/gtk-doc/html/libtracker-sparql/xsd-date.html
/usr/share/gtk-doc/html/libtracker-sparql/xsd-dateTime.html
/usr/share/gtk-doc/html/libtracker-sparql/xsd-double.html
/usr/share/gtk-doc/html/libtracker-sparql/xsd-integer.html
/usr/share/gtk-doc/html/libtracker-sparql/xsd-ontology.html
/usr/share/gtk-doc/html/libtracker-sparql/xsd-string.html

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/user/tracker-store.service
/usr/share/dbus-1/services/org.freedesktop.Tracker1.service
/usr/share/xdg/autostart/tracker-store.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtracker-control-2.0.so.0
/usr/lib64/libtracker-control-2.0.so.0.3.0
/usr/lib64/libtracker-miner-2.0.so.0
/usr/lib64/libtracker-miner-2.0.so.0.3.0
/usr/lib64/libtracker-sparql-2.0.so.0
/usr/lib64/libtracker-sparql-2.0.so.0.3.0
/usr/lib64/tracker-2.0/libtracker-common.so
/usr/lib64/tracker-2.0/libtracker-common.so.0
/usr/lib64/tracker-2.0/libtracker-common.so.0.0.0
/usr/lib64/tracker-2.0/libtracker-data.so
/usr/lib64/tracker-2.0/libtracker-data.so.0
/usr/lib64/tracker-2.0/libtracker-data.so.0.0.0

%files locales -f tracker.lang
%defattr(-,root,root,-)

