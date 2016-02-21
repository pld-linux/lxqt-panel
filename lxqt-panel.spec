#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-panel
Name:		lxqt-panel
Version:	0.10.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	4a884aa9a59b2f554204ab3491663edc
URL:		http://www.lxqt.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake >= 2.8.3
BuildRequires:	kf5-solid-devel
BuildRequires:	libdbusmenu-qt5-devel
BuildRequires:	liblxqt-devel >= 0.10.0
BuildRequires:	libqtxdg-devel >= 1.0.0
BuildRequires:	libstatgrab-devel
BuildRequires:	libsysstat-devel >= 0.3.1
BuildRequires:	lm_sensors-devel >= 3.3.5
BuildRequires:	lxqt-globalkeys-devel >= 0.7.0
BuildRequires:	menu-cache-devel >= 0.3.3
BuildRequires:	pulseaudio-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
BuildRequires:	xz-devel
Requires:	lxqt-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-panel

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/lxqt/panel.conf
%attr(755,root,root) %{_bindir}/lxqt-panel
%{_includedir}/lxqt/ilxqtpanel.h
%{_includedir}/lxqt/ilxqtpanelplugin.h
%{_includedir}/lxqt/lxqtpanelglobals.h
%dir %{_libdir}/lxqt-panel
%attr(755,root,root) %{_libdir}/lxqt-panel/libcolorpicker.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libcpuload.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libdirectorymenu.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libkbindicator.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libmount.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libnetworkmonitor.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libscreensaver.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libsensors.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libsysstat.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libvolume.so
%dir %{_datadir}/lxqt/lxqt-panel
%{_datadir}/lxqt/lxqt-panel/clock.desktop
%{_datadir}/lxqt/lxqt-panel/colorpicker.desktop
%{_datadir}/lxqt/lxqt-panel/cpuload.desktop
%{_datadir}/lxqt/lxqt-panel/desktopswitch.desktop
%{_datadir}/lxqt/lxqt-panel/directorymenu.desktop
%{_datadir}/lxqt/lxqt-panel/kbindicator.desktop
%{_datadir}/lxqt/lxqt-panel/mainmenu.desktop
%{_datadir}/lxqt/lxqt-panel/mount.desktop
%{_datadir}/lxqt/lxqt-panel/networkmonitor.desktop
%{_datadir}/lxqt/lxqt-panel/quicklaunch.desktop
%{_datadir}/lxqt/lxqt-panel/screensaver.desktop
%{_datadir}/lxqt/lxqt-panel/sensors.desktop
%{_datadir}/lxqt/lxqt-panel/showdesktop.desktop
%{_datadir}/lxqt/lxqt-panel/spacer.desktop
%{_datadir}/lxqt/lxqt-panel/statusnotifier.desktop
%{_datadir}/lxqt/lxqt-panel/sysstat.desktop
%{_datadir}/lxqt/lxqt-panel/taskbar.desktop
%{_datadir}/lxqt/lxqt-panel/tray.desktop
%{_datadir}/lxqt/lxqt-panel/volume.desktop
%{_datadir}/lxqt/lxqt-panel/worldclock.desktop
%dir %{_datadir}/lxqt/translations/lxqt-panel
%dir %{_datadir}/lxqt/translations/lxqt-panel/clock
%dir %{_datadir}/lxqt/translations/lxqt-panel/cpuload
%dir %{_datadir}/lxqt/translations/lxqt-panel/desktopswitch
%dir %{_datadir}/lxqt/translations/lxqt-panel/directorymenu
%dir %{_datadir}/lxqt/translations/lxqt-panel/kbindicator
%dir %{_datadir}/lxqt/translations/lxqt-panel/mainmenu
%dir %{_datadir}/lxqt/translations/lxqt-panel/mount
%dir %{_datadir}/lxqt/translations/lxqt-panel/networkmonitor
%dir %{_datadir}/lxqt/translations/lxqt-panel/quicklaunch
%dir %{_datadir}/lxqt/translations/lxqt-panel/screensaver
%dir %{_datadir}/lxqt/translations/lxqt-panel/sensors
%dir %{_datadir}/lxqt/translations/lxqt-panel/showdesktop
%dir %{_datadir}/lxqt/translations/lxqt-panel/spacer
%dir %{_datadir}/lxqt/translations/lxqt-panel/sysstat
%dir %{_datadir}/lxqt/translations/lxqt-panel/taskbar
%dir %{_datadir}/lxqt/translations/lxqt-panel/volume
%dir %{_datadir}/lxqt/translations/lxqt-panel/worldclock
