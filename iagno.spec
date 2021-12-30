%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1
%define ltstgt	20211230

Name:		iagno
Version:	3.38.1
Release:	2.%{ltstgt}.0
Summary:	GNOME Reversi game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Boards
URL:		https://wiki.gnome.org/Iagno
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  librsvg-vala-devel
BuildRequires:  pkgconfig(gsound)
BuildRequires:  cmake
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	meson
BuildRequires:	libxml2-utils
BuildRequires:  vala
BuildRequires:  pkgconfig(vapigen)
BuildRequires:	librsvg-vala-devel

Obsoletes:	iagno-extra-data
# for help
Requires:	yelp

%description
The GNOME version of Reversi. The goal is to control the most disks
on the board.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Reversi.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Reversi.gschema.xml
%{_datadir}/%{name}/
#{_iconsdir}/*/*/apps/org.gnome.Reversi.png
%{_iconsdir}/*/*/apps/org.gnome.Reversi-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Reversi.svg
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/org.gnome.Reversi.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Reversi.service
