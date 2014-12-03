#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libxcb
Version  : 1.11.1
Release  : 6
URL      : http://xorg.freedesktop.org/releases/individual/xcb/libxcb-1.11.1.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/xcb/libxcb-1.11.1.tar.gz
Summary  : XCB DRI3 Extension
Group    : Development/Tools
License  : MIT
Requires: libxcb-lib
Requires: libxcb-doc
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(pthread-stubs)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xcb-proto)
BuildRequires : pkgconfig(xdmcp)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : xcb-proto-python

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


%prep
%setup -q -n libxcb-1.11.1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libxcb/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
