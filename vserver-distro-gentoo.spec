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
Version:	1.0
Release:	1.6
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.linux.ee/pub/gentoo/distfiles/distfiles/rc-scripts-1.6.13.tar.bz2
# Source0-md5:	0ec4cdbd7d430e1fdf82840a083863ff
Source1:	http://dev.gentoo.org/~hollow/vserver/util-vserver/util-vserver-0.30.208-gentoo-r3.tar.bz2
# Source1-md5:	97ee5692ab45124f59ffa78f37cfdb2c
Source2:	ftp://ftp.linux.ee/pub/gentoo/distfiles/snapshots/portage-20051007.tar.bz2
# NoSource2-md5:	be45da32a8c8c420a3c45de125566311
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
%setup -q -c -a1
%patch0 -p1

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
