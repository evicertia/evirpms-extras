%global sname   sqlite_fdw
%global sversion 1.2.1
%global pgmajorversion 12
%global pginstdir /usr/pgsql-%{pgmajorversion}

%ifarch ppc64 ppc64le
# Define the AT version and path.
%global atstring        at10.0
%global atpath          /opt/%{atstring}
%endif

# Disable tests by default.
%{!?runselftest:%global runselftest 0}

Summary:        SQLite Foreign Data Wrapper for PostgreSQL

Name:           %{sname}%{pgmajorversion}
Version:        %{sversion}+evi
Release:        1%{?dist}
License:        PostgreSQL
URL:            https://github.com/pgspider/%{sname}
Source0:        https://github.com/pgspider/%{sname}/archive/v%{sversion}.tar.gz
Patch0:         %{sname}-pg%{pgmajorversion}-makefile-pgxs.patch
BuildRequires:  postgresql%{pgmajorversion}-devel
BuildRequires:  postgresql%{pgmajorversion}-server sqlite-devel
Requires:       postgresql%{pgmajorversion}-server
%if 0%{?fedora} >= 27
Requires:       sqlite-libs
%endif
%if 0%{?rhel} <= 7
Requires:       sqlite
%endif

%ifarch ppc64 ppc64le
AutoReq:        0
Requires:       advance-toolchain-%{atstring}-runtime
%endif

%ifarch ppc64 ppc64le
BuildRequires:  advance-toolchain-%{atstring}-devel
%endif

%description
This PostgreSQL extension is a Foreign Data Wrapper for SQLite.

%prep
%setup -q -n %{sname}-%{sversion}
%patch0 -p0

%build
%ifarch ppc64 ppc64le
        CFLAGS="${CFLAGS} $(echo %{__global_cflags} | sed 's/-O2/-O3/g') -m64 -mcpu=power8 -mtune=power8 -I%{atpath}/include"
        CXXFLAGS="${CXXFLAGS} $(echo %{__global_cflags} | sed 's/-O2/-O3/g') -m64 -mcpu=power8 -mtune=power8 -I%{atpath}/include"
        LDFLAGS="-L%{atpath}/%{_lib}"
        CC=%{atpath}/bin/gcc; export CC
%endif
USE_PGXS=1 %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
USE_PGXS=1 %{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}
# Install README and howto file under PostgreSQL installation directory:
%{__install} -d %{buildroot}%{pginstdir}/doc/extension
%{__install} -m 644 README.md %{buildroot}%{pginstdir}/doc/extension/README-%{sname}.md
%{__rm} -f %{buildroot}%{pginstdir}/doc/extension/README.md

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{pginstdir}/lib/*.so
%{pginstdir}/share/extension/*.sql
%{pginstdir}/share/extension/*.control
%{pginstdir}/doc/extension/README-%{sname}.md
%ifarch ppc64 ppc64le
 %else
 %if %{pgmajorversion} >= 11 && %{pgmajorversion} < 90
  %if 0%{?rhel} && 0%{?rhel} <= 6
  %else
   %{pginstdir}/lib/bitcode/%{sname}*.bc
   %{pginstdir}/lib/bitcode/%{sname}/*.bc
  %endif
 %endif
%endif

%changelog
* Thu Aug 27 2020 David Bueno <dbueno@evicertia.com> - 1.2.1-1
- Update to 1.2.1

* Thu Jul 30 2020 Pablo Ruiz <pruiz@evicertia.com> - 1.2.0-1
- Initial packaging for Sqlite_fdw RPM repositories
