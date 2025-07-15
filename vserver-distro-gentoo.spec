Summary:	VServer build template for Gentoo
Summary(pl.UTF-8):	Szablon do budowania VServera dla Gentoo
Name:		vserver-distro-gentoo
Version:	1.0
Release:	1.12
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.linux.ee/pub/gentoo/distfiles/distfiles/rc-scripts-1.6.13.tar.bz2
# Source0-md5:	0ec4cdbd7d430e1fdf82840a083863ff
Source1:	http://dev.gentoo.org/~hollow/vserver/util-vserver/util-vserver-0.30.208-gentoo-r3.tar.bz2
# Source1-md5:	97ee5692ab45124f59ffa78f37cfdb2c
Source2:	ftp://ftp.linux.ee/pub/gentoo/distfiles/snapshots/portage-20051007.tar.bz2
# NoSource2-md5:	be45da32a8c8c420a3c45de125566311
Patch0:		%{name}.patch
Patch1:		vserver-new_dev-fix.patch
Patch2:		vserver-new_drop-defaulttar.patch
URL:		http://dev.gentoo.org/~hollow/vserver/
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	bzip2
Requires:	tar
Requires:	util-vserver-build
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_distro		gentoo
%define		_sysconfdir	/etc/vservers/.distributions/%{_distro}
%define		_distdir	%{_libdir}/util-vserver/distributions/%{_distro}
%define		_portagedir	/usr/portage

%description
VServer build template for Gentoo Linux.

%description -l pl.UTF-8
Szablon do budowania VServera dla Gentoo.

%prep
%setup -q -c -a1
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_distdir},%{_sbindir},%{_portagedir}}
P=$(basename %{SOURCE0} .tar.bz2)
install ${P}/sbin/functions.sh $RPM_BUILD_ROOT%{_distdir}
sed -e '
s,@distdir@,%{_distdir},
s,@portagedir@,%{_portagedir},
' tools/vserver-new > $RPM_BUILD_ROOT%{_sbindir}/vserver-gentoo-new
chmod +x $RPM_BUILD_ROOT%{_sbindir}/vserver-gentoo-new

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
Please read http://www.gentoo.org/doc/en/vserver-howto.xml#doc_chap3
how to create gentoo guest vservers.

vserver-new is called vserver-gentoo-new in PLD Linux.

You will also need unpacked portage tree in /usr/portage. You can get
one from your closest gentoo mirror. If you can't find one then
ftp://ftp.linux.ee/pub/gentoo/distfiles/snapshots/portage-latest.tar.bz2
will do.
EOF
#' vim
fi

%files
%defattr(644,root,root,755)
%dir %{_distdir}
%attr(755,root,root) %{_sbindir}/vserver-gentoo-new
%{_sysconfdir}
%{_portagedir}
%{_distdir}
