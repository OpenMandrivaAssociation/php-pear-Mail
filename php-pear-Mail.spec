%define		_class		Mail
%define		pre		        b1
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.2.0
Release:	%mkrel 0.%{pre}.1
Summary:	Class that provides multiple interfaces for sending emails
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}%{pre}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PEAR's Mail package defines an interface for implementing mailers under the
PEAR hierarchy. It also provides supporting functions useful to multiple mailer
backends. Currently supported backends include: PHP's native mail() function,
sendmail, and SMTP. This package also provides a RFC822 email address list
validation utility class.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}%{pre}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}%{pre}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :

%preun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml

