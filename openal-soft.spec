#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openal-soft
Version  : 1.17.2
Release  : 9
URL      : http://www.openal-soft.org/openal-releases/openal-soft-1.17.2.tar.bz2
Source0  : http://www.openal-soft.org/openal-releases/openal-soft-1.17.2.tar.bz2
Summary  : OpenAL is a cross-platform 3D audio API
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: openal-soft-bin
Requires: openal-soft-lib
Requires: openal-soft-data
BuildRequires : alsa-lib-dev
BuildRequires : cmake
BuildRequires : pkgconfig(libpulse)

%description
Source Install
==============
To install OpenAL Soft, use your favorite shell to go into the build/
directory, and run:

%package bin
Summary: bin components for the openal-soft package.
Group: Binaries
Requires: openal-soft-data

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
Requires: openal-soft-lib
Requires: openal-soft-bin
Requires: openal-soft-data
Provides: openal-soft-devel

%description dev
dev components for the openal-soft package.


%package lib
Summary: lib components for the openal-soft package.
Group: Libraries
Requires: openal-soft-data

%description lib
lib components for the openal-soft package.


%prep
%setup -q -n openal-soft-1.17.2

%build
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DLIB_SUFFIX=64
make V=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/altonegen
/usr/bin/bsincgen
/usr/bin/makehrtf
/usr/bin/openal-info

%files data
%defattr(-,root,root,-)
/usr/share/openal/alsoftrc.sample
/usr/share/openal/hrtf/default-44100.mhr
/usr/share/openal/hrtf/default-48000.mhr

%files dev
%defattr(-,root,root,-)
/usr/include/AL/al.h
/usr/include/AL/alc.h
/usr/include/AL/alext.h
/usr/include/AL/efx-creative.h
/usr/include/AL/efx-presets.h
/usr/include/AL/efx.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
