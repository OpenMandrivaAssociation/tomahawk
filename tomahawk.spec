Name:		tomahawk
Version:	0.5.5
Release:	1
Summary:	Qt playdar social music player
License:	GPLv3
Group:		Sound
URL:		http://tomahawk-player.org
Source0:	http://downloads.tomahawk-player.org/%{name}-%{version}.tar.bz2
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
BuildRequires:	qtweetlib-devel
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(libattica)
Provides:	tomahawk-player

%description
Tomahawk Player is a next generation music player. 
It features custom stations (building upon the
beatuiful Echo Nest), a playlist importer, 
social connection to Twitter, Google Chat,
and Jabber. Maybe most important of all: 
It's able to find and pull music from
different sources like YouTube, last.fm,
SoundCloud, Skreemr, Spotify, and more
using the Playdar approach.
Of course, it can also play songs from
your local library.
Make sure to check out the video 
if you like to know more.

%prep
%setup -q

%build
%cmake -DINTERNAL_JREEN=OFF -DBUILD_RELEASE=ON
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/tomahawk
%{_libdir}/*.so

%{_prefix}/libexec/tomahawk_crash_reporter

%{_datadir}/applications/tomahawk.desktop
%{_datadir}/icons/hicolor/*/*
