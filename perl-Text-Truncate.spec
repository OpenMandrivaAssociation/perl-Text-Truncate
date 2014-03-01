%define	module	Text-Truncate

Name:		perl-%{module}
Version:	%perl_convert_version 1.06
Release:	1

Summary:	Perl module with simple string truncating routine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Truncate-1.06.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch


%description
This is a simple, no-brainer subroutine to truncate a string and add an
optional cutoff marker (defaults to ``...'').

(Yes, this is a really brain-dead sort of thing to make a module out of,
but then again, I use it so often that it might as well be in a module.)

The synopsis gives examples of how to use it.

%prep
%setup -qn Text-Truncate-1.06

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.04-1
+ Revision: 768269
- adapt to mandriva
- imported package perl-Text-Truncate


* Tue Jan 18 2011 jquelin <jquelin> 1.40.0-1.mga1
+ Revision: 22973
- cleaning spec file
- imported package perl-Text-Truncate


* Fri Jan 14 2011 cpan2dist 1.04-1mdv
- initial mdv release, generated with cpan2dist


