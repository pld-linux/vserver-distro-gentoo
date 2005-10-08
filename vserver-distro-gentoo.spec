# NOTE
# - to update md5 either copy them from web, or run:
%if 0
./builder vserver-distro-gentoo.spec -5
./builder vserver-distro-gentoo.spec -5 --target i386
./builder vserver-distro-gentoo.spec -5 --target pentium3
./builder vserver-distro-gentoo.spec -5 --target pentium4
./builder vserver-distro-gentoo.spec -5 --target athlon
%endif
#
Summary:	VServer build template for Gentoo
Name:		vserver-distro-gentoo
%define	_snap 20051003
Version:	1.0
Release:	0.%{_snap}.6
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.linux.ee/pub/gentoo/distfiles/distfiles/rc-scripts-1.6.13.tar.bz2
# Source0-md5:	0ec4cdbd7d430e1fdf82840a083863ff
Source1:	http://dev.gentoo.org/~hollow/vserver/util-vserver/util-vserver-0.30.208-gentoo-r3.tar.bz2
# Source1-md5:	97ee5692ab45124f59ffa78f37cfdb2c
%ifarch %{ix86}
Source2:	http://dev.gentoo.org/~hollow/vserver/stages/x86/x86/stage1-x86-%{_snap}.tar.bz2
# Source2-md5:	6af78bb1d8b9c296abfc7b8a57848cc7
# NoSource2-md5:	6af78bb1d8b9c296abfc7b8a57848cc7
NoSource:	2
%endif
%ifarch i386 i486 i586
Source3:	http://dev.gentoo.org/~hollow/vserver/stages/x86/x86/stage2-x86-%{_snap}.tar.bz2
# NoSource3-md5:	b7c48312833c74c90430d5c93a9de17b
NoSource:	3
Source4:	http://dev.gentoo.org/~hollow/vserver/stages/x86/x86/stage3-x86-%{_snap}.tar.bz2
# NoSource4-md5:	589eacc5ec6711fd2310d816154363dc
NoSource:	4
%endif
%ifarch i686
Source5:	http://dev.gentoo.org/~hollow/vserver/stages/x86/i686/stage2-i686-%{_snap}.tar.bz2
# NoSource5-md5:	71990bf0c572281885a5f35557667bac
NoSource:	5
Source6:	http://dev.gentoo.org/~hollow/vserver/stages/x86/i686/stage3-i686-%{_snap}.tar.bz2
# NoSource6-md5:	5b0042d6ff51da8e0a153072c55ab6aa
NoSource:	6
%endif
%ifarch pentium3
Source7:	http://dev.gentoo.org/~hollow/vserver/stages/x86/pentium3/stage2-pentium3-%{_snap}.tar.bz2
# NoSource7-md5:	1d03ab580ca52b4e9b13fd8be8c1ffd3
NoSource:	7
Source8:	http://dev.gentoo.org/~hollow/vserver/stages/x86/pentium3/stage3-pentium3-%{_snap}.tar.bz2
# NoSource8-md5:	52b6b94e3f44961ffc1a0d10a2a1d5f4
NoSource:	8
%endif
%ifarch pentium4
Source9:	http://dev.gentoo.org/~hollow/vserver/stages/x86/pentium4/stage2-pentium4-%{_snap}.tar.bz2
# NoSource9-md5:	2554a44086f58ef8168f064b79fbd814
NoSource:	9
Source10:	http://dev.gentoo.org/~hollow/vserver/stages/x86/pentium4/stage3-pentium4-%{_snap}.tar.bz2
# NoSource10-md5:	e4faa29e3fea7b13333510224a6b5e16
NoSource:	10
%endif
%ifarch athlon
Source11:	http://dev.gentoo.org/~hollow/vserver/stages/x86/athlon-xp/stage2-athlon-xp-%{_snap}.tar.bz2
# NoSource11-md5:	ddc5baeb1588335b727a36906c28cdf3
NoSource:	11
Source12:	http://dev.gentoo.org/~hollow/vserver/stages/x86/athlon-xp/stage3-athlon-xp-%{_snap}.tar.bz2
# NoSource12-md5:	6eb0474c2e459dc89990152489e3f055
NoSource:	12
%endif
Source13:	ftp://ftp.linux.ee/pub/gentoo/distfiles/snapshots/portage-20051007.tar.bz2
# NoSource13-md5:	be45da32a8c8c420a3c45de125566311
NoSource:	13
Patch0:		%{name}.patch
URL:		http://dev.gentoo.org/~hollow/vserver/
BuildRequires:	fakeroot
Requires:	bash
Requires:	util-vserver-build
Requires:	wget
Requires:	tar
Requires:	bzip2
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_distro		gentoo
%define		_sysconfdir	/etc/vservers/.distributions/%{_distro}
%define		_distdir	%{_libdir}/util-vserver/distributions/%{_distro}
%define		_portagedir	/usr/portage

%description
VServer build template for Gentoo

%prep
%setup -q -c -a1 -a13
%patch0 -p1

%if 0
%ifarch i386 i486 i586
%setup -q -c -a1 -a2 -a3
%endif
%ifarch i686
%setup -q -c -a1 -a4 -a5
%endif
%ifarch pentium3
%setup -q -c -a1 -a6 -a7
%endif
%ifarch pentium4
%setup -q -c -a1 -a8 -a9
%endif
%ifarch athlon
%setup -q -c -a1 -a10 -a11
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_distdir},%{_sbindir},%{_portagedir}}
install rc-scripts-1.6.13/sbin/functions.sh $RPM_BUILD_ROOT%{_distdir}
sed -e '
s,@distdir@,%{_distdir},
s,@portagedir@,%{_portagedir},
' tools/vserver-new > $RPM_BUILD_ROOT%{_sbindir}/vserver-gentoo-new

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_distdir}
%attr(755,root,root) %{_sbindir}/vserver-gentoo-new
%{_sysconfdir}
%{_portagedir}
%{_distdir}
