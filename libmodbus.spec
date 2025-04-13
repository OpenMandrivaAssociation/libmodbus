%define major 5
%define libname		%mklibname modbus
%define oldlibname	%mklibname modbus 5
%define devellibname	%mklibname -d modbus

Name:		libmodbus
Version:	3.1.11
Release:	1
Summary:	A Modbus library
Group:		System/Libraries
License:	LGPLv2+
URL:		https://www.libmodbus.org/
Source0:	https://github.com/stephane/libmodbus/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	asciidoc
BuildRequires:	slibtool
BuildRequires:	xmlto
BuildSystem:	autotools

%patchlist
libmodbus-3.1.11-dont_install_docs.patch
libmodbus-3.1.11-honor-cflags-cxxflags.patch

%description
libmodbus is a C library designed to provide a fast and robust
implementation of the Modbus protocol.

It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

#----------------------------------------------------------------------

%package -n	%libname
Summary:	A Modbus library
Group:		System/Libraries
%rename		%{oldlibname}

%description -n %libname
libmodbus is a C library designed to provide a fast and robust
implementation of the Modbus protocol.

It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

This package contains the libmodbus shared library.

%files -n %{libname}
%{_libdir}/libmodbus.so.%{major}*

#----------------------------------------------------------------------

%package -n	%devellibname
Summary:	Development files for libmodbus
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	modbus-devel = %{version}-%{release}

%description -n	%devellibname
libmodbus is a C library designed to provide a fast and robust
implementation of the Modbus protocol.

It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

This package contains libraries, header files and developer documentation
needed for developing software which uses the libmodbus library.

%files -n %{devellibname}
%license COPYING*
%doc AUTHORS NEWS README.md
%{_includedir}/modbus/
%{_libdir}/pkgconfig/libmodbus.pc
%{_libdir}/libmodbus.so

#----------------------------------------------------------------------

%prep
%autosetup -p1

