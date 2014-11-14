%define		_state		stable
%define		orgname		kmix
%define		qtver		4.8.1

Summary:	KDE audio mixer
Summary(pl.UTF-8):	Mikser dźwięku dla KDE
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	0291dc7fb9fae98a56e875ea883397cd
BuildRequires:	alsa-lib-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	glib2-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libcanberra-devel
BuildRequires:	libstdc++-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdemultimedia-kmix < 4.8.99-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sound mixer application for KDE.

%description -l pl.UTF-8
Mikser dźwięku dla KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang kmix		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kmix.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_bindir}/kmixremote
%attr(755,root,root) %{_libdir}/libkdeinit4_kmix.so
%attr(755,root,root) %{_libdir}/libkdeinit4_kmixctrl.so
%attr(755,root,root) %{_libdir}/kde4/kded_kmixd.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_mixer.so
%{_datadir}/apps/kmix
%{_datadir}/apps/plasma/services/mixer.operations
%{_datadir}/autostart/restore_kmix_volumes.desktop
%{_datadir}/autostart/kmix_autostart.desktop
%{_datadir}/kde4/services/kmixctrl_restore.desktop
%{_datadir}/kde4/services/kded/kmixd.desktop
%{_datadir}/kde4/services/plasma-engine-mixer.desktop
%{_desktopdir}/kde4/kmix.desktop
%{_iconsdir}/*/*/*/kmix.png
%{_datadir}/dbus-1/interfaces/org.kde.kmix.*.xml
