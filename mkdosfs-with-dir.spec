%define name mkdosfs-with-dir
%define version 1.0
%define release %mkrel 8

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
rm -rf %{buildroot}
install -D -m 4755 %SOURCE0 %{buildroot}/usr/bin/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*


