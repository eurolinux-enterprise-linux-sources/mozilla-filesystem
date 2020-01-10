Name:           mozilla-filesystem
Version:        1.9
Release:        11%{?dist}
Summary:        Mozilla filesytem layout
Group:          Applications/Internet
License:        MPLv1.1
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
This package provides some directories required by packages which use
Mozilla technologies such as NPAPI plugins or toolkit extensions.

%prep

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/{lib,%{_lib}}/mozilla/{plugins,extensions}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mozilla/extensions
mkdir -p $RPM_BUILD_ROOT/etc/skel/.mozilla/{plugins,extensions}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
/usr/lib*/mozilla
%{_datadir}/mozilla
/etc/skel/.mozilla

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.9-11
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.9-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.9-3
- fix license tag

* Wed Apr 30 2008 Christopher Aillon <caillon@redhat.com> 1.9-2
- Also own the */mozilla parent dirs

* Wed Apr 30 2008 Christopher Aillon <caillon@redhat.com> 1.9-1
- Initial RPM
