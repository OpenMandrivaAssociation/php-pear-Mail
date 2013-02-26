%define		_class		Mail
%define		pre		        b1
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.2.0
Release:	%mkrel 0.%{pre}.8
Summary:	Class that provides multiple interfaces for sending emails
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}%{pre}.tgz
Patch0:		Mail-1.2.0b1-CVE-2009-4023,4111.diff
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

%patch0 -p0 -b .CVE-2009-4023,4111

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



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-0.b1.7mdv2011.0
+ Revision: 667621
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-0.b1.6mdv2011.0
+ Revision: 607120
- rebuild

* Mon Jan 25 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-0.b1.5mdv2010.1
+ Revision: 496118
- P0: security fix for CVE-2009-4023,4111

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-0.b1.4mdv2010.1
+ Revision: 470143
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Nov 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-0.b1.3mdv2010.1
+ Revision: 463810
- use rpm filetriggers to register starting from mandriva 2010.1

* Thu Oct 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-0.b1.2mdv2010.0
+ Revision: 452035
- fix %%postun

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-0.b1.1mdv2010.0
+ Revision: 450209
- import php-pear-Mail


* Fri Sep 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-0.b1.1mdv2010.0
- split out from php-pear package
