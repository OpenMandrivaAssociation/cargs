%global upstream likle
%global gitbase  https://github.com

%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary: A lightweight cross-platform getopt alternative
Name:    cargs
Version: 1.0.3
Release: 1
License: MIT
Url:     https://%{upstream}.github.io/%{name}
Source0: %{gitbase}/%{upstream}/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ninja

%description
A lightweight cross-platform getopt alternative.
Command line argument parser library for C/C++.
Can be used to parse argv and argc parameters.

%package -n %{libname}
Summary:  %{summary}
Group:    System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the %{name} runtime library.

%package -n %{devname}
Summary:  %{summary}
Group:    Development/C
Requires: %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the %{name} development headers and library.

%prep
%autosetup
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/lib%{name}*.so

%files -n %{devname}
%doc README.md
%license LICENSE.md
%{_includedir}/%{name}.h
%{_libdir}/cmake/%{name}
