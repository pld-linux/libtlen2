
%define		_snap	20040301

Summary:	Tlen.pl client library
Summary(pl):	Biblioteka kliencka Tlen.pl
Name:		libtlen2
Version:	0.0.1
Release:	0.%{_snap}.2
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://libtlen.eu.org/libtlen2_files/%{name}-%{_snap}.tar.gz
# Source0-md5:	3f360a494f927e2a95c1fb2905e270f8
URL:		http://www.libtlen.eu.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnet-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libtlen is a library providing an API for client programs which want
to use Tlen.pl, an Instant Messanging protocol based on Jabber, but
with some modifications.

%description -l pl
Biblioteka libtlen dostarcza API dla programów klienckich
korzystaj±cych z protoko³u Tlen.pl który bazuje na Jabber z
niewielkimi modyfikacjami.

%package devel
Summary:	Header files for developping programs using libtlen
Summary(pl):	Pliki nag³ówkowe do biblioteki libtlen
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package is required to develop programs that use Tlen.pl
protocol.

%description devel -l pl
Pakiet wymagany przy pisaniu programów korzystaj±cych z protoko³u
Tlen.pl.

%package static
Summary:	Static version of libtlen library
Summary(pl):	Biblioteka statyczna libtlen
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libtlen library.

%description static -l pl
Biblioteka statyczna libtlen.

%prep
%setup -q -n %{name}-%{_snap}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtlen2.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/protocol/protocol.txt
%doc docs/reference/*/*.html
%attr(755,root,root) %{_libdir}/libtlen2.so
%{_includedir}/*
%{_pkgconfigdir}/libtlen-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtlen2.a
