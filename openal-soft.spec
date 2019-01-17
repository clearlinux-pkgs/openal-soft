#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openal-soft
Version  : 1.19.0
Release  : 27
URL      : http://www.openal-soft.org/openal-releases/openal-soft-1.19.0.tar.bz2
Source0  : http://www.openal-soft.org/openal-releases/openal-soft-1.19.0.tar.bz2
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
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libpulse)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pulseaudio-dev
BuildRequires : pulseaudio-dev32
Patch1: std-gnu.patch

%description
OpenAL soft
===========
`master` branch CI status :  [![Build Status](https://travis-ci.org/kcat/openal-soft.svg?branch=master)](https://travis-ci.org/kcat/openal-soft) [![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/kcat/openal-soft?branch=master&svg=true)](https://ci.appveyor.com/api/projects/status/github/kcat/openal-soft?branch=master&svg=true)

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
%setup -q -n openal-soft-1.19.0
%patch1 -p1
pushd ..
cp -a openal-soft-1.19.0 build32
popd
pushd ..
cp -a openal-soft-1.19.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547683816
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -march=haswell "
export FCFLAGS="$CFLAGS -O3 -march=haswell "
export FFLAGS="$CFLAGS -O3 -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build32
pushd clr-build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 ..
make  %{?_smp_mflags} VERBOSE=1
unset PKG_CONFIG_PATH
popd

%install
export SOURCE_DATE_EPOCH=1547683816
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openal-soft
cp COPYING %{buildroot}/usr/share/package-licenses/openal-soft/COPYING
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/alrecord
/usr/bin/altonegen
/usr/bin/haswell/alrecord
/usr/bin/haswell/altonegen
/usr/bin/haswell/makehrtf
/usr/bin/haswell/openal-info
/usr/bin/makehrtf
/usr/bin/openal-info

%files data
%defattr(-,root,root,-)
/usr/share/openal/alsoftrc.sample
/usr/share/openal/hrtf/default-44100.mhr
/usr/share/openal/hrtf/default-48000.mhr
/usr/share/openal/presets/3D7.1.ambdec
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
/usr/lib64/cmake/OpenAL/OpenALConfig-relwithdebinfo.cmake
/usr/lib64/cmake/OpenAL/OpenALConfig.cmake
/usr/lib64/haswell/libopenal.so
/usr/lib64/libopenal.so
/usr/lib64/pkgconfig/openal.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/OpenAL/OpenALConfig-relwithdebinfo.cmake
/usr/lib32/cmake/OpenAL/OpenALConfig.cmake
/usr/lib32/libopenal.so
/usr/lib32/pkgconfig/32openal.pc
/usr/lib32/pkgconfig/openal.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libopenal.so.1
/usr/lib64/haswell/libopenal.so.1.19.0
/usr/lib64/libopenal.so.1
/usr/lib64/libopenal.so.1.19.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libopenal.so.1
/usr/lib32/libopenal.so.1.19.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openal-soft/COPYING
