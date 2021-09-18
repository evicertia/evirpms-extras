# Restore old style debuginfo creation for rpm >= 4.14.
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# -*- rpm-spec -*-
BuildRoot:      %_topdir/td-agent-bit-1.8.7-evi1-1.x86_64/RUNTIME
Summary:        Fast data collector for Linux
Name:           td-agent-bit
Version:        1.8.7_evi1
Release:        1
License:        Apache v2.0
Group:          System Environment/Daemons
Vendor:         Treasure Data
Source:         https://github.com/tuxillo/fluent-bit/archive/refs/tags/v1.8.7-evi1.tar.gz











Autoreq: ON


Prefix: /





%define _rpmdir %_topdir/RPMS
%define _srcrpmdir %_topdir/SRPMS
%define _rpmfilename td-agent-bit-1.8.7-evi1-1.x86_64.rpm
%define _unpackaged_files_terminate_build 0

%define ignore #


%description
Fluent Bit is a high performance and multi platform Log Forwarder.


# This is a shortcutted spec file generated by CMake RPM generator
# we skip _install step because CPack does that for us.
# We do only save CPack installed tree in _prepr
# and then restore it in build.
%prep
mv $RPM_BUILD_ROOT %_topdir/tmpBBroot

%install
if [ -e $RPM_BUILD_ROOT ];
then
  rm -rf $RPM_BUILD_ROOT
fi
mv %_topdir/tmpBBroot $RPM_BUILD_ROOT



%clean

%post



%postun


%pre


%preun


%files
%defattr(-,root,root,-)
%dir "/etc/td-agent-bit"
"/lib/systemd/system/td-agent-bit.service"
%dir "/lib/td-agent-bit"
"/lib/td-agent-bit/libfluent-bit.so"
%dir "/opt/td-agent-bit"
%dir "/opt/td-agent-bit/bin"
"/opt/td-agent-bit/bin/td-agent-bit"


%config(noreplace) "/etc/td-agent-bit/td-agent-bit.conf"
%config(noreplace) "/etc/td-agent-bit/parsers.conf"
%config(noreplace) "/etc/td-agent-bit/plugins.conf"
%ignore "/lib"
%ignore "/lib/systemd"
%ignore "/lib/systemd/system"
%ignore "/lib64"
%ignore "/lib64/pkgconfig"
%ignore "/usr/local"
%ignore "/usr/local/bin"
%ignore "/opt"
%ignore "/etc"


%changelog
* Sun Jul 4 2010 Eric Noulard <eric.noulard@gmail.com> - 1.8.7_evi1-1
  Generated by CPack RPM (no Changelog file were provided)


