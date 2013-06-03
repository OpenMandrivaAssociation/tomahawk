%define major %{version}
%define libname %mklibname tomahawklib %{major}
%define devname %mklibname tomahawklib -d

Summary:	Qt playdar social music player
Name:		tomahawk
Version:	0.7.0
Release:	0.1
License:	GPLv3
Group:		Sound
Url:		http://tomahawk-player.org
Source0:	http://downloads.tomahawk-player.org/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	liblastfm-devel
BuildRequires:	qt4-devel
BuildRequires:	qtweetlib-devel
BuildRequires:	quazip-devel
BuildRequires:	pkgconfig(libattica)
BuildRequires:	pkgconfig(libclucene-core) >= 2.3.3.4
BuildRequires:	pkgconfig(libechonest) >= 2.0.3
BuildRequires:	pkgconfig(libjreen)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(taglib)
Provides:	tomahawk-player = %{version}-%{release}

%description
Tomahawk Player is a next generation music player.

It features custom stations (building upon the beatuiful Echo Nest),
a playlist importer, social connection to Twitter, Google Chat, and Jabber.

Maybe most important of all: It's able to find and pull music from different 
sources like YouTube, last.fm, SoundCloud, Skreemr, Spotify, and more using 
the Playdar approach. Of course, it can also play songs from a local library.

Make sure to check out the video if you like to know more.

%files
%{_bindir}/tomahawk
%{_libdir}/libtomahawk_*.so
%{_prefix}/libexec/tomahawk_crash_reporter
%{_datadir}/applications/tomahawk.desktop
%{_iconsdir}/hicolor/*/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package provides shared library for %{name}.

%files -n %{libname}
%{_libdir}/libtomahawklib.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package provides development libraries and headers needed to build
software using %{name}.

%files -n %{devname}
%{_includedir}/libtomahawk
%{_libdir}/cmake/Tomahawk
%{_libdir}/libtomahawklib.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake \
	-DINTERNAL_JREEN=OFF \
	-DBUILD_RELEASE=ON
%make

%install
%makeinstall_std -C build

