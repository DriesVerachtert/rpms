# $Id$
# Authority: shuff
# Upstream: Michael Gregorowicz <mike$mg2,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Access

%define perl_prefix %{buildroot}%{_prefix}

Summary: Manipulate SVN access files
Name: perl-SVN-Access
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Access/

Source: http://search.cpan.org/CPAN/authors/id/M/MG/MGREGORO/SVN-Access-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Tie::IxHash) >= 1.21
Requires: perl
Requires: perl(Tie::IxHash) >= 1.21

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
SVN::Access includes both an object-oriented interface for manipulating SVN
access files (AuthzSVNAccessFile files), as well as a command line interface to
that object-oriented programming interface.

%prep
%setup -n %{real_name}-%{version}

# fix problem with modules generated by older versions of Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{perl_prefix}"
%{__make} %{?_smp_mflags}

# fix the shebang
%{__perl} -pi -e 's|/usr/bin/env perl$|/usr/bin/perl|;' examples/svnaclmgr.pl

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# install the executable
%{__install} -m755 -d %{buildroot}%{_bindir}
%{__install} -m755 examples/svnaclmgr.pl %{buildroot}%{_bindir}/svnaclmgr

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/SVN/Access.pm
%{perl_vendorlib}/SVN/Access/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jul 06 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.10-1
- Updated to release 0.10.

* Wed Apr 25 2012 David Hrbáč <david@hrbac.cz> - 0.08-1
- new upstream release

* Tue Feb 7 2012 Steve Huff <shuff@vecna.org> - 0.07-1
- Initial package.
