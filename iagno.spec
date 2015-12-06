%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		iagno
Version:	3.18.2
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
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.2-2.mga5
+ Revision: 815323
- require yelp for showing help

* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796300
- new version 3.14.2

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 748673
- Second Mageia 5 Mass Rebuild

* Fri Oct 10 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 737810
- new version 3.14.1

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719181
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.91-2.mga5
+ Revision: 680403
- Mageia 5 Mass Rebuild

* Mon Sep 01 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670556
- new version 3.13.91

* Sat Aug 23 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 666673
- new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655175
- new version 3.13.4

* Sun Jun 15 2014 ovitters <ovitters> 3.12.2-2.mga5
+ Revision: 636448
- obsolete iagno-extra-data

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622087
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614073
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 607935
- new version 3.12.0

* Sun Mar 16 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604239
- new version 3.11.92

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 593375
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.2-1.mga5
+ Revision: 582982
- add appdata
- new version 3.11.2

* Sat Nov 09 2013 ovitters <ovitters> 3.10.1-3.mga4
+ Revision: 550178
- fix url

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 541416
- Mageia 4 Mass Rebuild

* Sat Oct 12 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 495863
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 483894
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480608
- new version 3.9.92

* Mon Sep 02 2013 ovitters <ovitters> 3.9.91-1.mga4
+ Revision: 474501
- new version 3.9.91

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468996
- new version 3.9.90
- cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.1-3.mga4
+ Revision: 440904
- Remove useless 'obsoletes'

* Sun Jun 09 2013 dams <dams> 3.8.1-2.mga4
+ Revision: 440828
- Better 'Obsoletes'

* Sun Jun 09 2013 dams <dams> 3.8.1-1.mga4
+ Revision: 440812
- add 'libxml2-utils' as BR
- imported package iagno

