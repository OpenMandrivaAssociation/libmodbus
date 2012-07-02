%define Werror_cflags %nil
%define libname %mklibname modbus
%define devellibname %mklibname -d modbus


Name:		libmodbus
Version:	3.1.0
Release:	1
Summary:	A Modbus library
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.libmodbus.org/
Source0:	https://github.com/downloads/stephane/libmodbus/libmodbus-%{version}.tar.gz
BuildRequires:	autoconf, automake, libtool, xmlto, asciidoc

%description
libmodbus is a C library designed to provide
a fast and robust implementation of
the Modbus protocol.
It runs on Linux, Mac OS X,
FreeBSD, QNX and Windows.
This package contains the
libmodbus shared library.

%package -n	%libname
Summary:	A Modbus library
Group:		System/Libraries

%description -n %libname
libmodbus is a C library designed to provide
a fast and robust implementation of
the Modbus protocol.
It runs on Linux, Mac OS X, FreeBSD,
QNX and Windows.
This package contains the
libmodbus shared library.


%package -n	%devellibname
Summary:	Development files for libmodbus
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	modbus-devel = %{version}-%{release}


%description -n	%devellibname

libmodbus is a C library designed
to provide a fast and robust implementation of
the Modbus protocol.
It runs on Linux, Mac OS X,
FreeBSD, QNX and Windows.

This package contains libraries,
header files and developer documentation needed
for developing software which
uses the libmodbus library.

%prep
%setup -q

%build
autoreconf -fi
./configure --prefix=/usr --libdir=%{_libdir}
#% configure2_5x --disable-silent-rules
%make

%install
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS MIGRATION NEWS COPYING* README.rst
%{_libdir}/libmodbus.so.*

%files -n %{devellibname}
%{_includedir}/modbus/
%{_libdir}/pkgconfig/libmodbus.pc
%{_libdir}/libmodbus.so
%{_mandir}/man7/*.7.*
%{_mandir}/man3/*.3.*
