# TODO
# - build ext
%define		pkgname	reader
%define		php_min_version 5.3.1
Summary:	MaxMind DB Reader API
Name:		php-maxmind-db-%{pkgname}
Version:	0.2.0
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	https://github.com/maxmind/MaxMind-DB-Reader-php/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	a5206ff1abe4c4b49c428b964fda92d1
URL:		https://github.com/maxmind/MaxMind-DB-Reader-php
Requires:	php(bcmath)
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP Reader for the MaxMind DB Database Format.

This is the pure PHP API for reading MaxMind DB files. MaxMind DB is a
binary file format that stores data indexed by IP address subnets
(IPv4 or IPv6).

%prep
%setup -qn MaxMind-DB-Reader-php-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_examplesdir}/%{name}-%{version}}
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%dir %{php_data_dir}/MaxMind
%dir %{php_data_dir}/MaxMind/Db
%{php_data_dir}/MaxMind/Db/Reader.php
%{php_data_dir}/MaxMind/Db/Reader
%{_examplesdir}/%{name}-%{version}
