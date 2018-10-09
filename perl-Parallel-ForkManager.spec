#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Parallel-ForkManager
Version  : 2.02
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Parallel-ForkManager-2.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Parallel-ForkManager-2.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libparallel-forkmanager-perl/libparallel-forkmanager-perl_1.19-1.debian.tar.xz
Summary  : 'A simple parallel processing fork manager'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Moo::Role)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Warn)

%description
# NAME
Parallel::ForkManager - A simple parallel processing fork manager
# VERSION

%package dev
Summary: dev components for the perl-Parallel-ForkManager package.
Group: Development
Provides: perl-Parallel-ForkManager-devel = %{version}-%{release}

%description dev
dev components for the perl-Parallel-ForkManager package.


%prep
%setup -q -n Parallel-ForkManager-2.02
cd ..
%setup -q -T -D -n Parallel-ForkManager-2.02 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Parallel-ForkManager-2.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Parallel/ForkManager.pm
/usr/lib/perl5/site_perl/5.26.1/Parallel/ForkManager/Child.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Parallel::ForkManager.3
/usr/share/man/man3/Parallel::ForkManager::Child.3
