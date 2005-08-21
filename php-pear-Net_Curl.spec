%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Curl
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an OO interface to the cURL extension
Summary(pl):	%{_pearname} - obiektowy interfejs do rozszerzenia cURL
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	184d23b7054483dcb61fee5d1d6cc692
URL:		http://pear.php.net/package/Net_Curl/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_Curl is an object oriented interface which abstracts away the
messy parts of dealing with PHP's cURL extension.

In PEAR status of this package is: %{_status}.

%description -l pl
Net_Curl to obiektowo zorientowany interfejs, kt�ry tworzy warstw�
abstrakcji dla nieprzyjaznych fragment�w obs�ugi rozszerzenia PHP
cURL.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
