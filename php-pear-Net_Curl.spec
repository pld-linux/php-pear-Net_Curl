%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Curl
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an OO interface to the cURL extension
Summary(pl):	%{_pearname} - obiektowy interfejs do rozszerzenia cURL
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	1.2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8b207ccf47795495b788034ef1049140
URL:		http://pear.php.net/package/Net_Curl/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-curl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Curl is an object oriented interface which abstracts away the
messy parts of dealing with PHP's cURL extension.

In PEAR status of this package is: %{_status}.

%description -l pl
Net_Curl to obiektowo zorientowany interfejs, który tworzy warstwê
abstrakcji dla nieprzyjaznych fragmentów obs³ugi rozszerzenia PHP
cURL.

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
