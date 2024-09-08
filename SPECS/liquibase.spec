Name:           liquibase
Version:        4.29.2
Release:        1%{?dist}
Summary:        Database Refactoring Tool
License:        ASL 2.0
BuildArch:      noarch
Url:            http://liquibase.org/
Group:          Applications/Databases
Source0:        https://github.com/liquibase/liquibase/releases/download/v%{version}/%{name}-%{version}.tar.gz

Requires:       java >= 11

%description
LiquiBase is an open source (Apache 2.0 License), database-independent library
for tracking, managing and applying database changes. It is built on a simple
premise: All database changes are stored in a human readable but tracked in
source control.

%prep
%setup -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -r ./ $RPM_BUILD_ROOT/%{_datadir}/%{name}
rm -r $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples
ln -sf %{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
/usr/share/*

%changelog
* Sun Sep  08 2024 Luiz B <luizplayer2016@hotmail.com> - 4.29.2
- Bump version 4.29.2

* Sun Sep  08 2024 Luiz B <luizplayer2016@hotmail.com> - 4.29.1
- Bump version 4.29.1

* Fri July  26 2024 Luiz B <luizplayer2016@hotmail.com> - 4.29.0
- Bump version 4.29.0

* Mon  May  27  2024 Luiz B <luizplayer2016@hotmail.com> - 4.28.0
- Bump version

* Fri Mar  29 2024 Luiz B <luizplayer2016@hotmail.com> - 4.27.0
- First version being packaged

