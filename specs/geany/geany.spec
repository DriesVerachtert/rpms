# $Id$
# Authority: dries
# Upstream: Enrico Troeger <enrico,troeger$uvena,de>

Summary: Small C editor
Name: geany
Version: 0.8
Release: 1
License: GPL
Group: Applications/Editors
URL: http://geany.uvena.de/

Source: http://dl.sf.net/geany/geany-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gtk2-devel

%description
Geany is a small C editor using GTK2 with basic features of an integrated 
development environment. It features syntax highlighting, code completion, 
call tips, many supported filetypes (including C, Java, PHP, HTML, DocBook, 
Perl, LateX, and Bash), and symbol lists.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}
%{__mv} %{buildroot}%{_datadir}/doc/geany rpmdocs

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc INSTALL THANKS rpmdocs/*
%doc %{_mandir}/man1/geany*
%{_bindir}/geany
%{_datadir}/geany/
%{_datadir}/pixmaps/geany.*
%{_datadir}/applications/geany.desktop

%changelog
* Fri Aug 11 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
