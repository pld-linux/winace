Summary:	unACE - extract, test and view ACE archives
Summary(pl):	unACE - rozpakowuje, testuje i przegl±da archiwa ACE
Name:		winace
Version:	2.5
Release:	1
License:	Shareware
Group:		Applications/Archiving
Source0:	http://www.winace.com/files/linunace%(echo %{version} | tr -d .).tgz
# Source0-md5:	ad1f8cb7ff3a6c6019da869b72300719
URL:		http://www.winace.com/
Obsoletes:	unace
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unACE utility is a shareware program, distributed without source
code and developed for extracting, testing and viewing the contents of
archives created with the ACE archiver.

%description -l pl
UnACE jest programem shareware, rozpowszechnianym bez kodu ¼ród³owego,
przeznaczonym do rozpakowywania, testowania oraz przegl±dania
zawarto¶ci archiwów stworzonych przez program ACE.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install unace $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unace
