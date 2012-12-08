%define name mkdosfs-with-dir
%define version 1.0
%define release %mkrel 10

Summary: Create a DOS image from a directory
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}
License: GPL
Group: File tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: dosfstools

%description
Create a DOS image from a directory without being superuser.

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 4755 %SOURCE0 $RPM_BUILD_ROOT/usr/bin/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-8mdv2011.0
+ Revision: 666433
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2011.0
+ Revision: 606648
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2010.1
+ Revision: 523321
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-5mdv2010.0
+ Revision: 426148
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 223291
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2008.1
+ Revision: 134225
- rebuild

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2008.1
+ Revision: 130021
- kill re-definition of %%buildroot on Pixel's request


* Fri Jan 26 2007 Pixel <pixel@mandriva.com> 1.0-2mdv2007.0
+ Revision: 113955
- mkdosfs is needed (from pkg dosfstools)

* Tue Jan 23 2007 Pixel <pixel@mandriva.com> 1.0-1mdv2007.1
+ Revision: 112483
- creation
- Create mkdosfs-with-dir

