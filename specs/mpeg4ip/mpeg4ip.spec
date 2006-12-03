# $Id$
# Authority: dag
# Upstream: <mpeg4ip-discussion@lists.sourceforge.net>

Summary: Open MPEG-4 streaming tools
Name: mpeg4ip
Version: 1.5.0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://mpeg4ip.net/

Source: http://dl.sf.net/mpeg4ip/mpeg4ip-%{version}.tar.gz
Patch0: mpeg4ip-1.5.0.1-nowerror.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtool, SDL-devel, gcc-c++
BuildRequires: id3lib-devel, xvidcore-devel, a52dec-devel,libmad-devel
BuildRequires: mpeg2dec-devel, libvorbis-devel, ffmpeg-devel, lame-devel
BuildRequires: faac-devel, x264-devel, gtk2-devel, nasm
BuildRequires: arts-devel, esound-devel

%description
MPEG4IP provides an end-to-end system to explore streaming multimedia. The
package includes many existing open source packages and the "glue" to
integrate them together. This is a tool for streaming video and audio that
is standards-oriented and free from proprietary protocols and extensions.


%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%setup
%patch0 -p1 -b .nowerror


%build
sh bootstrap --disable-warns-as-err
%configure \
    --disable-warns-as-err \
    --disable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# Remove all *.la files
find %{buildroot} -name '*.la' -exec rm -f {} \;


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FEATURES.html README* TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/mp4player_plugin/
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%{_mandir}/man3/*
%{_mandir}/manm/*


%changelog
* Tue Jul 11 2006 Matthias Saou <http://freshrpms.net/> 1.5.0.1-1
- Update to 1.5.0.1.
- Move man3 files to devel package.
- Add missing ldconfig calls.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 01 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)

