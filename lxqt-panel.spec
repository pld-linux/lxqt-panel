#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Main panel bar for LXQt desktop suite
Summary(pl.UTF-8):	Główny panel dla środowiska graficznego LXQt
Name:		lxqt-panel
Version:	2.3.2
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-panel/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	acb37b56e739f88689ed2818f8e36fef
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Concurrent-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kf6-kwindowsystem-devel >= 6.0.0
BuildRequires:	kp6-layer-shell-qt-devel >= 6.0.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	libstatgrab-devel
BuildRequires:	libsysstat-devel >= 1.1.0
BuildRequires:	libxcb-devel
BuildRequires:	lm_sensors-devel >= 3.3.5
BuildRequires:	lxqt-globalkeys-devel >= 2.3.0
BuildRequires:	lxqt-menu-data >= 2.3.0
BuildRequires:	pulseaudio-devel
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	wayland-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Main panel bar for LXQt desktop suite.

%description -l pl.UTF-8
Główny panel dla środowiska graficznego LXQt.

%package devel
Summary:	Developer files for %{name}
Summary(pl.UTF-8):	Pliki dla programistów %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
Developer files for %{name}.

%description devel -l pl.UTF-8
Pliki dla programistów %{name}.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%dir %{_sysconfdir}/xdg/lxqt
%{_sysconfdir}/xdg/lxqt/panel.conf
%attr(755,root,root) %{_bindir}/lxqt-panel
%dir %{_libdir}/lxqt-panel
%{_libdir}/lxqt-panel/libbacklight.so
%{_libdir}/lxqt-panel/libcolorpicker.so
%{_libdir}/lxqt-panel/libcpuload.so
%{_libdir}/lxqt-panel/libcustomcommand.so
%{_libdir}/lxqt-panel/libdirectorymenu.so
%{_libdir}/lxqt-panel/libdom.so
%{_libdir}/lxqt-panel/libkbindicator.so
%{_libdir}/lxqt-panel/libmount.so
%{_libdir}/lxqt-panel/libnetworkmonitor.so
%{_libdir}/lxqt-panel/libqeyes.so
%{_libdir}/lxqt-panel/libsensors.so
%{_libdir}/lxqt-panel/libsysstat.so
%{_libdir}/lxqt-panel/libvolume.so
%dir %{_libdir}/lxqt-panel/backend
%{_libdir}/lxqt-panel/backend/libwmbackend_kwin_wayland.so
%{_libdir}/lxqt-panel/backend/libwmbackend_wayfire.so
%{_libdir}/lxqt-panel/backend/libwmbackend_wlroots.so
%{_libdir}/lxqt-panel/backend/libwmbackend_xcb.so
%{_desktopdir}/lxqt-panel.desktop
%dir %{_datadir}/lxqt/lxqt-panel
%{_datadir}/lxqt/lxqt-panel/colorpicker.desktop
%{_datadir}/lxqt/lxqt-panel/cpuload.desktop
%{_datadir}/lxqt/lxqt-panel/desktopswitch.desktop
%{_datadir}/lxqt/lxqt-panel/directorymenu.desktop
%{_datadir}/lxqt/lxqt-panel/kbindicator.desktop
%{_datadir}/lxqt/lxqt-panel/mainmenu.desktop
%{_datadir}/lxqt/lxqt-panel/mount.desktop
%{_datadir}/lxqt/lxqt-panel/networkmonitor.desktop
%{_datadir}/lxqt/lxqt-panel/quicklaunch.desktop
%{_datadir}/lxqt/lxqt-panel/sensors.desktop
%{_datadir}/lxqt/lxqt-panel/showdesktop.desktop
%{_datadir}/lxqt/lxqt-panel/spacer.desktop
%{_datadir}/lxqt/lxqt-panel/statusnotifier.desktop
%{_datadir}/lxqt/lxqt-panel/sysstat.desktop
%{_datadir}/lxqt/lxqt-panel/taskbar.desktop
%{_datadir}/lxqt/lxqt-panel/tray.desktop
%{_datadir}/lxqt/lxqt-panel/volume.desktop
%{_datadir}/lxqt/lxqt-panel/worldclock.desktop
%{_datadir}/lxqt/lxqt-panel/backlight.desktop
%{_datadir}/lxqt/lxqt-panel/customcommand.desktop
%{_datadir}/lxqt/lxqt-panel/dom.desktop
%{_datadir}/lxqt/lxqt-panel/fancymenu.desktop
%{_datadir}/lxqt/lxqt-panel/qeyes.desktop
%dir %{_datadir}/lxqt/panel
%{_datadir}/lxqt/panel/qeyes-types
%dir %{_datadir}/lxqt/translations/lxqt-panel
%dir %{_datadir}/lxqt/translations/lxqt-panel/colorpicker
%dir %{_datadir}/lxqt/translations/lxqt-panel/cpuload
%dir %{_datadir}/lxqt/translations/lxqt-panel/customcommand
%dir %{_datadir}/lxqt/translations/lxqt-panel/desktopswitch
%dir %{_datadir}/lxqt/translations/lxqt-panel/directorymenu
%dir %{_datadir}/lxqt/translations/lxqt-panel/dom
%dir %{_datadir}/lxqt/translations/lxqt-panel/fancymenu
%dir %{_datadir}/lxqt/translations/lxqt-panel/kbindicator
%dir %{_datadir}/lxqt/translations/lxqt-panel/mainmenu
%dir %{_datadir}/lxqt/translations/lxqt-panel/mount
%dir %{_datadir}/lxqt/translations/lxqt-panel/networkmonitor
%dir %{_datadir}/lxqt/translations/lxqt-panel/qeyes
%dir %{_datadir}/lxqt/translations/lxqt-panel/quicklaunch
%dir %{_datadir}/lxqt/translations/lxqt-panel/sensors
%dir %{_datadir}/lxqt/translations/lxqt-panel/showdesktop
%dir %{_datadir}/lxqt/translations/lxqt-panel/spacer
%dir %{_datadir}/lxqt/translations/lxqt-panel/statusnotifier
%dir %{_datadir}/lxqt/translations/lxqt-panel/sysstat
%dir %{_datadir}/lxqt/translations/lxqt-panel/taskbar
%dir %{_datadir}/lxqt/translations/lxqt-panel/volume
%dir %{_datadir}/lxqt/translations/lxqt-panel/worldclock
%{_mandir}/man1/lxqt-panel.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqt/*
