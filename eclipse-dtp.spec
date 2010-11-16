%include	/usr/lib/rpm/macros.java
Summary:	Eclipse Data Tools Platform
Name:		eclipse-dtp
Version:	1.6.2
Release:	1
License:	EPL
Group:		Libraries
Source0:	ftp://ftp.man.szczecin.pl/pub/eclipse/datatools/downloads/1.6/dtp_%{version}.zip
# Source0-md5:	bdfcffa15403c913099958afe1b7f432
URL:		http://www.eclipse.org/datatools/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	eclipse >= 3.3.2
Requires:	eclipse-emf-sdo-xsd >= 2.2.2
Requires:	eclipse-gef >= 3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

%description
The Eclipse Data Tools Platform provides extensible frameworks and
exemplary tools, enabling a diverse set of plug-in offerings specific
to particular data-centric technologies and supported by the DTP
ecosystem.

%prep
%setup -qc
mv eclipse/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/org.eclipse.datatools.*
%{eclipsedir}/plugins/org.eclipse.datatools.*.jar

# deps
%{eclipsedir}/plugins/javax.wsdl_*.jar
%{eclipsedir}/plugins/javax.xml_*.jar
%{eclipsedir}/plugins/net.sourceforge.lpg.lpgjavaruntime_*.jar
%{eclipsedir}/plugins/org.apache.xerces_*.jar
%{eclipsedir}/plugins/org.apache.xml.resolver_*.jar
%{eclipsedir}/plugins/org.apache.xml.serializer_*.jar
