%define	ver	2.04
Summary:	unACE - extract, test and view ACE archives
Summary(pl):	unACE - rozpakowuje, testuje i przegl�da archiwa ACE
Name:		winace
Version:	%{ver}
Release:	1
License:	Shareware
Group:		Applications/Archiving
Source0:	http://www.winace.mewa.net/mirror/linunace%(echo %{ver} | sed -e 's#\.##g').tgz
URL:		http://www.winace.com/
Obsoletes:	unace
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unACE utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the ACE archiver.

%description -l pl
UnACE jest programem freeware, rozpowszechnianym wraz z kodem
�r�d�owym, przeznaczonym do rozpakowywania, testowania oraz
przegl�dania zawarto�ci archiw�w stworzonych przez program ACE.

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