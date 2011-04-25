%define upstream_name    JQuery
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    JQuery Interface
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI::Application)
BuildRequires: perl(CGI::Carp)
BuildRequires: perl(CGI::Util)
BuildRequires: perl(CSS)
BuildRequires: perl(HTML::Table)
BuildRequires: perl(IO::String)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Writer)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
JQuery is a frontend for the jQuery language. I use *JQuery* to refer to
the Perl part or the package, and *jQuery* to reference the javascript part
or the package.

A quote from the http://jquery.com manpage: jQuery is a fast, concise,
JavaScript Library that simplifies how you traverse HTML documents, handle
events, perform animations, and add Ajax interactions to your web pages.

JQuery.pm is the main module. There are other modules such as Form,
TableSorter, Splitter, Taconite ..., all of which provide different
functionality. The main module needs to be instantiated, and each instance
of the other modules needs to be registered with the main module. It is
then the responsibility of JQuery.pm to produce the relevant HTML, css and
javascript code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


