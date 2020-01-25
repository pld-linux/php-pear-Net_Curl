%define		_class		Net
%define		_subclass	Curl
%define		_status		stable
%define		_pearname	Net_Curl
Summary:	%{_pearname} - an OO interface to the cURL extension
Summary(pl.UTF-8):	%{_pearname} - obiektowy interfejs do rozszerzenia cURL
Name:		php-pear-%{_pearname}
Version:	1.2.5
Release:	4
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0bb20480301256a7c5a04b4ca7e6f755
URL:		http://pear.php.net/package/Net_Curl/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php(curl)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Curl is an object oriented interface which abstracts away the
messy parts of dealing with PHP's cURL extension.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Net_Curl to obiektowo zorientowany interfejs, który tworzy warstwę
abstrakcji dla nieprzyjaznych fragmentów obsługi rozszerzenia PHP
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
%{php_pear_dir}/Net/*.php
