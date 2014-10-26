#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-panel
Name:		lxqt-panel
Version:	0.8.0
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	2d2c2251659f285031f65bfb30c741c3
URL:		http://www.lxqt.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.8.0
BuildRequires:	liblxqt-mount-devel >= 0.8.0
BuildRequires:	libqtxdg-devel >= 1.0.0
BuildRequires:	libstatgrab-devel
BuildRequires:	libsysstat-devel >= 0.1.0
BuildRequires:	lm_sensors-devel >= 3.3.5
BuildRequires:	lxqt-globalkeys-devel >= 0.7.0
BuildRequires:	menu-cache-devel >= 0.3.3
BuildRequires:	pulseaudio-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXcomposite-devel
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
    -DUSE_QT5=ON \
	../
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{_sysconfdir}/qt5/lxqt/panel.conf
%attr(755,root,root) %{_bindir}/lxqt-panel
%dir %{_includedir}/lxqt
%{_includedir}/lxqt/ilxqtpanel.h
%{_includedir}/lxqt/ilxqtpanelplugin.h
%{_includedir}/lxqt/lxqtpanelglobals.h
%dir %{_libdir}/lxqt-panel
%attr(755,root,root) %{_libdir}/lxqt-panel/libclock.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libcolorpicker.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libcpuload.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libdesktopswitch.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libdom.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libmainmenu.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libmount.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libnetworkmonitor.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libpanelkbindicator.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libpanelsysstat.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libpanelvolume.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libpanelworldclock.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libquicklaunch.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libscreensaver.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libsensors.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libshowdesktop.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libtaskbar.so
%attr(755,root,root) %{_libdir}/lxqt-panel/libtray.so
%dir %{_datadir}/lxqt/lxqt-panel
%{_datadir}/lxqt/lxqt-panel/clock.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel
%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_es.qm
%lang(es_UY) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_es_UY.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/clock/clock_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/colorpicker.desktop
%{_datadir}/lxqt/lxqt-panel/cpuload.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_hu_HU.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_ja.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_ru_RU.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_sl.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/cpuload/cpuload_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/desktopswitch.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_es.qm
%lang(es_UY) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_es_UY.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/desktopswitch/desktopswitch_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/dom.desktop

%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_es.qm
%lang(es_UY) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_es_UY.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_it.qm
%lang(it_IT) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_pl.qm
%lang(pl_PL) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_sk_SK.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/lxqt-panel_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/mainmenu.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_es.qm
%lang(es_UY) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_es_UY.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mainmenu/mainmenu_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/mount.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_es.qm
%lang(es_UY) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_es_UY.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/mount/mount_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/networkmonitor.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_hu_HU.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_ja.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_ru_RU.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_sl.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/networkmonitor/networkmonitor_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/panelkbindicator.desktop
%{_datadir}/lxqt/lxqt-panel/panelsysstat.desktop
%{_datadir}/lxqt/lxqt-panel/panelvolume.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_fr_FR.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_it_IT.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_ru_RU.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_sl.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_th_TH.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/panelvolume/panelvolume_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/panelworldclock.desktop
%{_datadir}/lxqt/lxqt-panel/quicklaunch.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_pl.qm
%lang(pl_PL) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/quicklaunch/quicklaunch_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/screensaver.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_pl.qm
%lang(pl_PL) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/screensaver/screensaver_zh_TW.qm

%{_datadir}/lxqt/lxqt-panel/sensors.desktop
%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors
%lang(ca) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_ca.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_el_GR.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_fr_FR.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_it_IT.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_ru_RU.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_th_TH.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/sensors/sensors_zh_TW.qm

%{_datadir}/lxqt/lxqt-panel/showdesktop.desktop
%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/showdesktop/showdesktop_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/taskbar.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-panel/taskbar/taskbar_zh_TW.qm
%{_datadir}/lxqt/lxqt-panel/tray.desktop
