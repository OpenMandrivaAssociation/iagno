%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		iagno
Version:	3.30.0
Release:	1
Summary:	GNOME Reversi game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Boards
URL:		https://wiki.gnome.org/Iagno
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Obsoletes:	iagno-extra-data
# for help
Requires:	yelp

%description
The GNOME version of Reversi. The goal is to control the most disks
on the board.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_datadir}/%{name}/
%{_iconsdir}/*/*/apps/%{name}.png
%{_iconsdir}/*/*/apps/%{name}-symbolic.svg
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/%{name}.appdata.xml
