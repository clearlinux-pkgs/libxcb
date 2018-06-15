#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libxcb
Version  : 1.13
Release  : 35
URL      : http://xorg.freedesktop.org/releases/individual/xcb/libxcb-1.13.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/xcb/libxcb-1.13.tar.gz
Summary  : X-protocol C Binding
Group    : Development/Tools
License  : MIT
Requires: libxcb-lib
Requires: libxcb-doc
BuildRequires : check
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : libXau-dev
BuildRequires : libXau-dev32
BuildRequires : libXi-dev
BuildRequires : libXi-dev32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32xcb-proto)
BuildRequires : pkgconfig(32xdmcp)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(xcb-proto)
BuildRequires : pkgconfig(xdmcp)
BuildRequires : pkgconfig(xorg-macros)

BuildRequires : python3
BuildRequires : xcb-proto
BuildRequires : xorgproto-dev

%description
About libxcb
============
libxcb provides an interface to the X Window System protocol, which
replaces the current Xlib interface. It has several advantages over
Xlib, including:
- size: small, simple library, and lower memory footprint
- latency hiding: batch several requests and wait for the replies later
- direct protocol access: interface and protocol correspond exactly
- proven thread support: transparently access XCB from multiple threads
- easy extension implementation: interfaces auto-generated from XML-XCB

%package dev
Summary: dev components for the libxcb package.
Group: Development
Requires: libxcb-lib
Provides: libxcb-devel

%description dev
dev components for the libxcb package.


%package dev32
Summary: dev32 components for the libxcb package.
Group: Default
Requires: libxcb-lib32
Requires: libxcb-dev

%description dev32
dev32 components for the libxcb package.


%package doc
Summary: doc components for the libxcb package.
Group: Documentation

%description doc
doc components for the libxcb package.


%package lib
Summary: lib components for the libxcb package.
Group: Libraries

%description lib
lib components for the libxcb package.


%package lib32
Summary: lib32 components for the libxcb package.
Group: Default

%description lib32
lib32 components for the libxcb package.


%prep
%setup -q -n libxcb-1.13
pushd ..
cp -a libxcb-1.13 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526134981
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static --enable-dri3 \
PYTHON=/usr/bin/python2
make

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --enable-dri3 \
PYTHON=/usr/bin/python2   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1526134981
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)


%files dev
%defattr(-,root,root,-)
/usr/include/xcb/bigreq.h
/usr/include/xcb/composite.h
/usr/include/xcb/damage.h
/usr/include/xcb/dpms.h
/usr/include/xcb/dri2.h
/usr/include/xcb/dri3.h
/usr/include/xcb/ge.h
/usr/include/xcb/glx.h
/usr/include/xcb/present.h
/usr/include/xcb/randr.h
/usr/include/xcb/record.h
/usr/include/xcb/render.h
/usr/include/xcb/res.h
/usr/include/xcb/screensaver.h
/usr/include/xcb/shape.h
/usr/include/xcb/shm.h
/usr/include/xcb/sync.h
/usr/include/xcb/xc_misc.h
/usr/include/xcb/xcb.h
/usr/include/xcb/xcbext.h
/usr/include/xcb/xevie.h
/usr/include/xcb/xf86dri.h
/usr/include/xcb/xfixes.h
/usr/include/xcb/xinerama.h
/usr/include/xcb/xinput.h
/usr/include/xcb/xkb.h
/usr/include/xcb/xprint.h
/usr/include/xcb/xproto.h
/usr/include/xcb/xselinux.h
/usr/include/xcb/xtest.h
/usr/include/xcb/xv.h
/usr/include/xcb/xvmc.h
/usr/lib64/libxcb-composite.so
/usr/lib64/libxcb-damage.so
/usr/lib64/libxcb-dpms.so
/usr/lib64/libxcb-dri2.so
/usr/lib64/libxcb-dri3.so
/usr/lib64/libxcb-glx.so
/usr/lib64/libxcb-present.so
/usr/lib64/libxcb-randr.so
/usr/lib64/libxcb-record.so
/usr/lib64/libxcb-render.so
/usr/lib64/libxcb-res.so
/usr/lib64/libxcb-screensaver.so
/usr/lib64/libxcb-shape.so
/usr/lib64/libxcb-shm.so
/usr/lib64/libxcb-sync.so
/usr/lib64/libxcb-xf86dri.so
/usr/lib64/libxcb-xfixes.so
/usr/lib64/libxcb-xinerama.so
/usr/lib64/libxcb-xinput.so
/usr/lib64/libxcb-xkb.so
/usr/lib64/libxcb-xtest.so
/usr/lib64/libxcb-xv.so
/usr/lib64/libxcb-xvmc.so
/usr/lib64/libxcb.so
/usr/lib64/pkgconfig/xcb-composite.pc
/usr/lib64/pkgconfig/xcb-damage.pc
/usr/lib64/pkgconfig/xcb-dpms.pc
/usr/lib64/pkgconfig/xcb-dri2.pc
/usr/lib64/pkgconfig/xcb-dri3.pc
/usr/lib64/pkgconfig/xcb-glx.pc
/usr/lib64/pkgconfig/xcb-present.pc
/usr/lib64/pkgconfig/xcb-randr.pc
/usr/lib64/pkgconfig/xcb-record.pc
/usr/lib64/pkgconfig/xcb-render.pc
/usr/lib64/pkgconfig/xcb-res.pc
/usr/lib64/pkgconfig/xcb-screensaver.pc
/usr/lib64/pkgconfig/xcb-shape.pc
/usr/lib64/pkgconfig/xcb-shm.pc
/usr/lib64/pkgconfig/xcb-sync.pc
/usr/lib64/pkgconfig/xcb-xf86dri.pc
/usr/lib64/pkgconfig/xcb-xfixes.pc
/usr/lib64/pkgconfig/xcb-xinerama.pc
/usr/lib64/pkgconfig/xcb-xinput.pc
/usr/lib64/pkgconfig/xcb-xkb.pc
/usr/lib64/pkgconfig/xcb-xtest.pc
/usr/lib64/pkgconfig/xcb-xv.pc
/usr/lib64/pkgconfig/xcb-xvmc.pc
/usr/lib64/pkgconfig/xcb.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libxcb-composite.so
/usr/lib32/libxcb-damage.so
/usr/lib32/libxcb-dpms.so
/usr/lib32/libxcb-dri2.so
/usr/lib32/libxcb-dri3.so
/usr/lib32/libxcb-glx.so
/usr/lib32/libxcb-present.so
/usr/lib32/libxcb-randr.so
/usr/lib32/libxcb-record.so
/usr/lib32/libxcb-render.so
/usr/lib32/libxcb-res.so
/usr/lib32/libxcb-screensaver.so
/usr/lib32/libxcb-shape.so
/usr/lib32/libxcb-shm.so
/usr/lib32/libxcb-sync.so
/usr/lib32/libxcb-xf86dri.so
/usr/lib32/libxcb-xfixes.so
/usr/lib32/libxcb-xinerama.so
/usr/lib32/libxcb-xinput.so
/usr/lib32/libxcb-xkb.so
/usr/lib32/libxcb-xtest.so
/usr/lib32/libxcb-xv.so
/usr/lib32/libxcb-xvmc.so
/usr/lib32/libxcb.so
/usr/lib32/pkgconfig/32xcb-composite.pc
/usr/lib32/pkgconfig/32xcb-damage.pc
/usr/lib32/pkgconfig/32xcb-dpms.pc
/usr/lib32/pkgconfig/32xcb-dri2.pc
/usr/lib32/pkgconfig/32xcb-dri3.pc
/usr/lib32/pkgconfig/32xcb-glx.pc
/usr/lib32/pkgconfig/32xcb-present.pc
/usr/lib32/pkgconfig/32xcb-randr.pc
/usr/lib32/pkgconfig/32xcb-record.pc
/usr/lib32/pkgconfig/32xcb-render.pc
/usr/lib32/pkgconfig/32xcb-res.pc
/usr/lib32/pkgconfig/32xcb-screensaver.pc
/usr/lib32/pkgconfig/32xcb-shape.pc
/usr/lib32/pkgconfig/32xcb-shm.pc
/usr/lib32/pkgconfig/32xcb-sync.pc
/usr/lib32/pkgconfig/32xcb-xf86dri.pc
/usr/lib32/pkgconfig/32xcb-xfixes.pc
/usr/lib32/pkgconfig/32xcb-xinerama.pc
/usr/lib32/pkgconfig/32xcb-xinput.pc
/usr/lib32/pkgconfig/32xcb-xkb.pc
/usr/lib32/pkgconfig/32xcb-xtest.pc
/usr/lib32/pkgconfig/32xcb-xv.pc
/usr/lib32/pkgconfig/32xcb-xvmc.pc
/usr/lib32/pkgconfig/32xcb.pc
/usr/lib32/pkgconfig/xcb-composite.pc
/usr/lib32/pkgconfig/xcb-damage.pc
/usr/lib32/pkgconfig/xcb-dpms.pc
/usr/lib32/pkgconfig/xcb-dri2.pc
/usr/lib32/pkgconfig/xcb-dri3.pc
/usr/lib32/pkgconfig/xcb-glx.pc
/usr/lib32/pkgconfig/xcb-present.pc
/usr/lib32/pkgconfig/xcb-randr.pc
/usr/lib32/pkgconfig/xcb-record.pc
/usr/lib32/pkgconfig/xcb-render.pc
/usr/lib32/pkgconfig/xcb-res.pc
/usr/lib32/pkgconfig/xcb-screensaver.pc
/usr/lib32/pkgconfig/xcb-shape.pc
/usr/lib32/pkgconfig/xcb-shm.pc
/usr/lib32/pkgconfig/xcb-sync.pc
/usr/lib32/pkgconfig/xcb-xf86dri.pc
/usr/lib32/pkgconfig/xcb-xfixes.pc
/usr/lib32/pkgconfig/xcb-xinerama.pc
/usr/lib32/pkgconfig/xcb-xinput.pc
/usr/lib32/pkgconfig/xcb-xkb.pc
/usr/lib32/pkgconfig/xcb-xtest.pc
/usr/lib32/pkgconfig/xcb-xv.pc
/usr/lib32/pkgconfig/xcb-xvmc.pc
/usr/lib32/pkgconfig/xcb.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libxcb/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxcb-composite.so.0
/usr/lib64/libxcb-composite.so.0.0.0
/usr/lib64/libxcb-damage.so.0
/usr/lib64/libxcb-damage.so.0.0.0
/usr/lib64/libxcb-dpms.so.0
/usr/lib64/libxcb-dpms.so.0.0.0
/usr/lib64/libxcb-dri2.so.0
/usr/lib64/libxcb-dri2.so.0.0.0
/usr/lib64/libxcb-dri3.so.0
/usr/lib64/libxcb-dri3.so.0.0.0
/usr/lib64/libxcb-glx.so.0
/usr/lib64/libxcb-glx.so.0.0.0
/usr/lib64/libxcb-present.so.0
/usr/lib64/libxcb-present.so.0.0.0
/usr/lib64/libxcb-randr.so.0
/usr/lib64/libxcb-randr.so.0.1.0
/usr/lib64/libxcb-record.so.0
/usr/lib64/libxcb-record.so.0.0.0
/usr/lib64/libxcb-render.so.0
/usr/lib64/libxcb-render.so.0.0.0
/usr/lib64/libxcb-res.so.0
/usr/lib64/libxcb-res.so.0.0.0
/usr/lib64/libxcb-screensaver.so.0
/usr/lib64/libxcb-screensaver.so.0.0.0
/usr/lib64/libxcb-shape.so.0
/usr/lib64/libxcb-shape.so.0.0.0
/usr/lib64/libxcb-shm.so.0
/usr/lib64/libxcb-shm.so.0.0.0
/usr/lib64/libxcb-sync.so.1
/usr/lib64/libxcb-sync.so.1.0.0
/usr/lib64/libxcb-xf86dri.so.0
/usr/lib64/libxcb-xf86dri.so.0.0.0
/usr/lib64/libxcb-xfixes.so.0
/usr/lib64/libxcb-xfixes.so.0.0.0
/usr/lib64/libxcb-xinerama.so.0
/usr/lib64/libxcb-xinerama.so.0.0.0
/usr/lib64/libxcb-xinput.so.0
/usr/lib64/libxcb-xinput.so.0.1.0
/usr/lib64/libxcb-xkb.so.1
/usr/lib64/libxcb-xkb.so.1.0.0
/usr/lib64/libxcb-xtest.so.0
/usr/lib64/libxcb-xtest.so.0.0.0
/usr/lib64/libxcb-xv.so.0
/usr/lib64/libxcb-xv.so.0.0.0
/usr/lib64/libxcb-xvmc.so.0
/usr/lib64/libxcb-xvmc.so.0.0.0
/usr/lib64/libxcb.so.1
/usr/lib64/libxcb.so.1.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libxcb-composite.so.0
/usr/lib32/libxcb-composite.so.0.0.0
/usr/lib32/libxcb-damage.so.0
/usr/lib32/libxcb-damage.so.0.0.0
/usr/lib32/libxcb-dpms.so.0
/usr/lib32/libxcb-dpms.so.0.0.0
/usr/lib32/libxcb-dri2.so.0
/usr/lib32/libxcb-dri2.so.0.0.0
/usr/lib32/libxcb-dri3.so.0
/usr/lib32/libxcb-dri3.so.0.0.0
/usr/lib32/libxcb-glx.so.0
/usr/lib32/libxcb-glx.so.0.0.0
/usr/lib32/libxcb-present.so.0
/usr/lib32/libxcb-present.so.0.0.0
/usr/lib32/libxcb-randr.so.0
/usr/lib32/libxcb-randr.so.0.1.0
/usr/lib32/libxcb-record.so.0
/usr/lib32/libxcb-record.so.0.0.0
/usr/lib32/libxcb-render.so.0
/usr/lib32/libxcb-render.so.0.0.0
/usr/lib32/libxcb-res.so.0
/usr/lib32/libxcb-res.so.0.0.0
/usr/lib32/libxcb-screensaver.so.0
/usr/lib32/libxcb-screensaver.so.0.0.0
/usr/lib32/libxcb-shape.so.0
/usr/lib32/libxcb-shape.so.0.0.0
/usr/lib32/libxcb-shm.so.0
/usr/lib32/libxcb-shm.so.0.0.0
/usr/lib32/libxcb-sync.so.1
/usr/lib32/libxcb-sync.so.1.0.0
/usr/lib32/libxcb-xf86dri.so.0
/usr/lib32/libxcb-xf86dri.so.0.0.0
/usr/lib32/libxcb-xfixes.so.0
/usr/lib32/libxcb-xfixes.so.0.0.0
/usr/lib32/libxcb-xinerama.so.0
/usr/lib32/libxcb-xinerama.so.0.0.0
/usr/lib32/libxcb-xinput.so.0
/usr/lib32/libxcb-xinput.so.0.1.0
/usr/lib32/libxcb-xkb.so.1
/usr/lib32/libxcb-xkb.so.1.0.0
/usr/lib32/libxcb-xtest.so.0
/usr/lib32/libxcb-xtest.so.0.0.0
/usr/lib32/libxcb-xv.so.0
/usr/lib32/libxcb-xv.so.0.0.0
/usr/lib32/libxcb-xvmc.so.0
/usr/lib32/libxcb-xvmc.so.0.0.0
/usr/lib32/libxcb.so.1
/usr/lib32/libxcb.so.1.1.0
