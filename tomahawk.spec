Name:		tomahawk
Version:	0.3.2
Release:	1
Summary:	Qt playdar social music player
License:	GPLv3
Group:		Sound
URL:		http://tomahawk-player.org
Source:		http://downloads.tomahawk-player.org/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	quazip-devel
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	qjson-devel
BuildRequires:	taglib-devel
BuildRequires:	clucene-devel => 2.3.3.4
BuildRequires:	libechonest-devel
BuildRequires:	liblastfm-devel
BuildRequires:	jreen-devel
BuildRequires:	attica-devel
BuildRequires:	qtweetlib-devel
Patch0:		tomahawk-0.3.2-clucene.patch

%description
Tomahawk Player is a next generation music player. 
It features custom stations (building upon the beatuiful Echo Nest), a playlist importer, 
social connection to Twitter, Google Chat, and Jabber. Maybe most important of all: 
It's able to find and pull music from different sources like YouTube, last.fm,
SoundCloud, Skreemr, Spotify, and more using the Playdar approach.
Of course, it can also play songs from your local library. Make sure to check out the video if you like to know more.

%prep
%setup -q
%patch0 -p1

%build
%cmake -DINTERNAL_JREEN=OFF -DBUILD_RELEASE=ON
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/tomahawk
%{_libdir}/libtomahawk_portfwd.so
%{_libdir}/libtomahawk_sipjabber.so
%{_libdir}/libtomahawk_sipgoogle.so
%{_libdir}/libtomahawk_siptwitter.so
%{_libdir}/libtomahawk_sipzeroconf.so
%{_libdir}/libtomahawklib.so

%{_prefix}/libexec/tomahawk_crash_reporter

%{_datadir}/applications/tomahawk.desktop
%{_datadir}/icons/
