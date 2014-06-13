Summary:	Create a DOS image from a directory
Name:		mkdosfs-with-dir
Version:	1.0
Release:	15
License:	GPLv2
Group:		File tools
Source0:	%{name}
BuildArch:	noarch
Requires:	dosfstools

%description
Create a DOS image from a directory without being superuser.

%install
install -D -m 4755 %SOURCE0 %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/*

