%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Curl
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - an OO interface to the cURL extension
Summary(pl):	%{_class}_%{_subclass} - obiektowy interfejs do rozszerzenia cURL
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Curl is an object oriented interface which abstracts away the
messy parts of dealing with PHP's cURL extension.

%description -l pl
Net_Curl to obiektowo zorientowany interfejs, który tworzy warstwê
abstrakcji dla nieprzyjaznych fragmentów obs³ugi rozszerzenia PHP
cURL.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
