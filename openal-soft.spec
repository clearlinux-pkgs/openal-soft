#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
Name     : openal-soft
Version  : 1.24.0
Release  : 52
URL      : https://www.openal-soft.org/openal-releases/openal-soft-1.24.0.tar.bz2
Source0  : https://www.openal-soft.org/openal-releases/openal-soft-1.24.0.tar.bz2
Summary  : OpenAL is a cross-platform 3D audio API
Group    : Development/Tools
License  : LGPL-2.0
Requires: openal-soft-bin = %{version}-%{release}
Requires: openal-soft-data = %{version}-%{release}
Requires: openal-soft-lib = %{version}-%{release}
Requires: openal-soft-license = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-dev32
BuildRequires : buildreq-cmake
BuildRequires : dbus-dev
BuildRequires : extra-cmake-modules
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : git
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : mesa-dev
BuildRequires : mesa-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32dbus-1)
BuildRequires : pkgconfig(32libpulse)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pulseaudio-dev
BuildRequires : pulseaudio-dev32
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
OpenAL Soft
===========
`master` branch CI status : [![GitHub Actions Status](https://github.com/kcat/openal-soft/actions/workflows/ci.yml/badge.svg)](https://github.com/kcat/openal-soft/actions) [![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/kcat/openal-soft?branch=master&svg=true)](https://ci.appveyor.com/api/projects/status/github/kcat/openal-soft?branch=master&svg=true)

%package bin
Summary: bin components for the openal-soft package.
Group: Binaries
Requires: openal-soft-data = %{version}-%{release}
Requires: openal-soft-license = %{version}-%{release}

%description bin
bin components for the openal-soft package.


%package data
Summary: data components for the openal-soft package.
Group: Data

%description data
data components for the openal-soft package.


%package dev
Summary: dev components for the openal-soft package.
Group: Development
Requires: openal-soft-lib = %{version}-%{release}
Requires: openal-soft-bin = %{version}-%{release}
Requires: openal-soft-data = %{version}-%{release}
Provides: openal-soft-devel = %{version}-%{release}
Requires: openal-soft = %{version}-%{release}

%description dev
dev components for the openal-soft package.


%package dev32
Summary: dev32 components for the openal-soft package.
Group: Default
Requires: openal-soft-lib32 = %{version}-%{release}
Requires: openal-soft-bin = %{version}-%{release}
Requires: openal-soft-data = %{version}-%{release}
Requires: openal-soft-dev = %{version}-%{release}

%description dev32
dev32 components for the openal-soft package.


%package lib
Summary: lib components for the openal-soft package.
Group: Libraries
Requires: openal-soft-data = %{version}-%{release}
Requires: openal-soft-license = %{version}-%{release}

%description lib
lib components for the openal-soft package.


%package lib32
Summary: lib32 components for the openal-soft package.
Group: Default
Requires: openal-soft-data = %{version}-%{release}
Requires: openal-soft-license = %{version}-%{release}

%description lib32
lib32 components for the openal-soft package.


%package license
Summary: license components for the openal-soft package.
Group: Default

%description license
license components for the openal-soft package.


%prep
%setup -q -n openal-soft-1.24.0
cd %{_builddir}/openal-soft-1.24.0
pushd ..
cp -a openal-soft-1.24.0 build32
popd
pushd ..
cp -a openal-soft-1.24.0 buildavx2
popd
pushd ..
cp -a openal-soft-1.24.0 buildavx512
popd

%build
## build_prepend content
export CFLAGS="$CFLAGS -fcommon"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731946176
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
export CFLAGS="$CFLAGS -fcommon"
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd
pushd ../buildavx512/
mkdir -p clr-build-avx512
pushd clr-build-avx512
## build_prepend content
export CFLAGS="$CFLAGS -fcommon"
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=512 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd
pushd ../build32/
mkdir -p clr-build32
pushd clr-build32
## build_prepend content
export CFLAGS="$CFLAGS -fcommon"
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../../build32/clr-build32;
make test || :
cd ../../buildavx2/clr-build-avx2;
make test || :
cd ../../buildavx512/clr-build-avx512;
make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1731946176
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openal-soft
cp %{_builddir}/openal-soft-%{version}/COPYING %{buildroot}/usr/share/package-licenses/openal-soft/707b40a3e29fae6db61aa9620879f003fdda4ed2 || :
export GOAMD64=v2
pushd ../build32/
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
popd
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
pushd ../buildavx512/
GOAMD64=v4
pushd clr-build-avx512
%make_install_v4  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
rm -rf %{buildroot}/usr/lib32/cmake
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/aldebug
/V3/usr/bin/allafplay
/V3/usr/bin/alrecord
/V3/usr/bin/altonegen
/V3/usr/bin/openal-info
/V4/usr/bin/aldebug
/V4/usr/bin/allafplay
/V4/usr/bin/alrecord
/V4/usr/bin/altonegen
/V4/usr/bin/openal-info
/usr/bin/aldebug
/usr/bin/allafplay
/usr/bin/alrecord
/usr/bin/altonegen
/usr/bin/openal-info

%files data
%defattr(-,root,root,-)
/usr/share/openal/alsoftrc.sample
"/usr/share/openal/hrtf/Default HRTF.mhr"
/usr/share/openal/presets/3D7.1.ambdec
/usr/share/openal/presets/hex-quad.ambdec
/usr/share/openal/presets/hexagon.ambdec
/usr/share/openal/presets/itu5.1-nocenter.ambdec
/usr/share/openal/presets/itu5.1.ambdec
/usr/share/openal/presets/presets.txt
/usr/share/openal/presets/rectangle.ambdec
/usr/share/openal/presets/square.ambdec

%files dev
%defattr(-,root,root,-)
/usr/include/AL/al.h
/usr/include/AL/alc.h
/usr/include/AL/alext.h
/usr/include/AL/efx-creative.h
/usr/include/AL/efx-presets.h
/usr/include/AL/efx.h
/usr/lib64/cmake/OpenAL/OpenALConfig.cmake
/usr/lib64/cmake/OpenAL/OpenALTargets-relwithdebinfo.cmake
/usr/lib64/cmake/OpenAL/OpenALTargets.cmake
/usr/lib64/libopenal.so
/usr/lib64/pkgconfig/openal.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libopenal.so
/usr/lib32/pkgconfig/32openal.pc
/usr/lib32/pkgconfig/openal.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libopenal.so.1.24.0
/V4/usr/lib64/libopenal.so.1.24.0
/usr/lib64/libopenal.so.1
/usr/lib64/libopenal.so.1.24.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libopenal.so.1
/usr/lib32/libopenal.so.1.24.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openal-soft/707b40a3e29fae6db61aa9620879f003fdda4ed2
