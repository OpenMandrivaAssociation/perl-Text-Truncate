%define	module	Text-Truncate

Name:		perl-%{module}
Version:	1.04
Release:	1

Summary:	Perl module with simple string truncating routine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.gz

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*
