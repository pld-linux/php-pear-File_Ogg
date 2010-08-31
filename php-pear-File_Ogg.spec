%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Ogg
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - access Ogg bitstreams
Summary(pl.UTF-8):	%{_pearname} - dostęp do strumieni Ogg
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ff2b90cb862818eeadb521a0547cbe3b
URL:		http://pear.php.net/package/File_Ogg/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides access to various media types inside an Ogg
bitstream.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet umożliwia dostęp do różnego rodzaju mediów wewnątrz
strumienia Ogg.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
