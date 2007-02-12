Summary:	Tlen.pl client library
Summary(pl.UTF-8):   Biblioteka kliencka Tlen.pl
Name:		libtlen2
Version:	0.0.2
%define	snap	20060309
Release:	0.%{snap}.1
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	%{name}-cvs-%{snap}.tar.bz2
# Source0-md5:	502faa748bb2871cb982b9a0524b528c
URL:		http://libtlen2.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnet-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libtlen is a library providing an API for client programs which want
to use Tlen.pl, an Instant Messanging protocol based on Jabber, but
with some modifications.

%description -l pl.UTF-8
Biblioteka libtlen dostarcza API dla programów klienckich
korzystających z protokołu Tlen.pl który bazuje na Jabber z
niewielkimi modyfikacjami.

%package devel
Summary:	Header files for developping programs using libtlen
Summary(pl.UTF-8):   Pliki nagłówkowe do biblioteki libtlen
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package is required to develop programs that use Tlen.pl
protocol.

%description devel -l pl.UTF-8
Pakiet wymagany przy pisaniu programów korzystających z protokołu
Tlen.pl.

%package static
Summary:	Static version of libtlen library
Summary(pl.UTF-8):   Biblioteka statyczna libtlen
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libtlen library.

%description static -l pl.UTF-8
Biblioteka statyczna libtlen.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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
