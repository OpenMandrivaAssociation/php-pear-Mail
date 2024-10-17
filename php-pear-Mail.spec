%define _class		Mail
%define modname	%{_class}

Summary:	Class that provides multiple interfaces for sending emails
Name:		php-pear-%{modname}
Version:	1.3.0
Release:	4
License:	PHP License
Group:		Development/PHP
Url:		https://pear.php.net/package/%{modname}
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
PEAR's Mail package defines an interface for implementing mailers under the
PEAR hierarchy. It also provides supporting functions useful to multiple mailer
backends. Currently supported backends include: PHP's native mail() function,
sendmail, and SMTP. This package also provides a RFC822 email address list
validation utility class.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{modname}.xml
%{_datadir}/pear/test/Mail
