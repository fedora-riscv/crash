#
# crash core analysis suite
#
Summary: crash utility for live systems; netdump, diskdump, LKCD or mcore dumpfiles
Name: crash
Version: 3.8
Release: 5
License: GPL
Group: Development/Debuggers
Source: %{name}-%{version}.tar.gz
URL: ftp://people.redhat.com/anderson/%{name}-%{version}.tar.gz
ExclusiveOS: Linux
ExclusiveArch: i386 ia64 x86_64
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: ncurses-devel zlib-devel
Patch0: crash.patch

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump and diskdump packages from Red Hat Linux, the mcore kernel patch
offered by Mission Critical Linux, or the LKCD kernel patch.

%prep
%setup -n %{name}-%{version}
%patch0 -p1 -b crash.patch

%build
make RPMPKG="%{version}-%{release}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_mandir}/man8
cp crash.8 %{buildroot}%{_mandir}/man8/crash.8

%files
%defattr(-,root,root)
/usr/bin/crash
%{_mandir}/man8/crash.8*
%doc README

%changelog
* Wed Jul 14 2004 Dave Anderson <anderson@redhat.com> 3.8-5
- bump release for fc3

* Tue Jul 13 2004 Dave Anderson <anderson@redhat.com> 3.8-4
- Fix for gcc 3.4.x/gdb issue where vmlinux was mistakenly presumed non-debug 

* Fri Jun 25 2004 Dave Anderson <anderson@redhat.com> 3.8-3
- remove (harmless) error message during ia64 diskdump invocation when
  an SMP system gets booted with maxcpus=1
- several 2.6 kernel specific updates

* Thu Jun 17 2004 Dave Anderson <anderson@redhat.com> 3.8-2
- updated source package to crash-3.8.tar.gz 
- diskdump support
- x86_64 processor support 

* Mon Sep 22 2003 Dave Anderson <anderson@redhat.com> 3.7-5
- make bt recovery code start fix-up only upon reaching first faulting frame

* Fri Sep 19 2003 Dave Anderson <anderson@redhat.com> 3.7-4
- fix "bt -e" and bt recovery code to recognize new __KERNEL_CS and DS

* Wed Sep 10 2003 Dave Anderson <anderson@redhat.com> 3.7-3
- patch to recognize per-cpu GDT changes that redefine __KERNEL_CS and DS

* Wed Sep 10 2003 Dave Anderson <anderson@redhat.com> 3.7-2
- patches for netdump active_set determination and slab info gathering 

* Wed Aug 20 2003 Dave Anderson <anderson@redhat.com> 3.7-1
- updated source package to crash-3.7.tar.gz

* Wed Jul 23 2003 Dave Anderson <anderson@redhat.com> 3.6-1
- removed Packager, Distribution, and Vendor tags
- updated source package to crash-3.6.tar.gz 

* Fri Jul 18 2003 Jay Fenlason <fenlason@redhat.com> 3.5-2
- remove ppc from arch list, since it doesn't work with ppc64 kernels
- remove alpha from the arch list since we don't build it any more

* Fri Jul 18 2003 Matt Wilson <msw@redhat.com> 3.5-1
- use %%defattr(-,root,root)

* Tue Jul 15 2003 Jay Fenlason <fenlason@redhat.com>
- Updated spec file as first step in turning this into a real RPM for taroon.
- Wrote man page.
