%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Ogg
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - access Ogg bitstreams
Summary(pl):	%{_pearname} - dost�p do strumieni Ogg
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	0.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6d5737d79779d6aecb94c3e359e78261
URL:		http://pear.php.net/package/File_Ogg/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides access to various media types inside an Ogg
bitstream.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet umo�liwia dost�p do r�nego rodzaju medi�w wewn�trz
strumienia Ogg.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Vorbis

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Vorbis/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Vorbis

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}