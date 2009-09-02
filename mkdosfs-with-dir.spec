%define name mkdosfs-with-dir
%define version 1.0
%define release %mkrel 5

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


