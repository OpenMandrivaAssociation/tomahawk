%define major %{version}
%define libname %mklibname %{name} %{major}
%define libplaydarapi %mklibname %{name}-playdarapi %{major}
%define libwidgets %mklibname %{name}-widgets %{major}
%define devname %mklibname %{name} -d

Summary:	Qt playdar social music player
Name:		tomahawk
Version:	0.8.2
Release:	1
License:	GPLv3+
Group:		Sound
Url:		http://tomahawk-player.org
Source0:	http://downloads.tomahawk-player.org/%{name}-%{version}.tar.bz2
Source1:	tomahawk_ru.ts.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	liblastfm-devel
BuildRequires:	qt4-devel
BuildRequires:	qtkeychain-devel
BuildRequires:	qtweetlib-devel
BuildRequires:	quazip-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libattica)
BuildRequires:	pkgconfig(libclucene-core) >= 2.3.3.4
BuildRequires:	pkgconfig(libechonest) >= 2.2
BuildRequires:	pkgconfig(libjreen)
BuildRequires:	pkgconfig(liblucene++)
BuildRequires:	pkgconfig(libsparsehash)
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
%{_datadir}/applications/tomahawk.desktop
%{_iconsdir}/hicolor/*/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}tomahawklib0.7.0 < 0.8.0

%description -n %{libname}
This package provides shared library for %{name}.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libplaydarapi}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libplaydarapi}
This package provides shared library for %{name}.

%files -n %{libplaydarapi}
%{_libdir}/lib%{name}-playdarapi.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libwidgets}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libwidgets}
This package provides shared library for %{name}.

%files -n %{libwidgets}
%{_libdir}/lib%{name}-widgets.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	%{libplaydarapi} = %{EVRD}
Requires:	%{libwidgets} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{_lib}tomahawklib-devel < 0.8.0
Obsoletes:	%{_lib}tomahawklib-devel < 0.8.0

%description -n %{devname}
This package provides development libraries and headers needed to build
software using %{name}.

%files -n %{devname}
%{_includedir}/libtomahawk
%{_libdir}/cmake/Tomahawk
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-playdarapi.so
%{_libdir}/lib%{name}-widgets.so

#----------------------------------------------------------------------------

%prep
%setup -q

pushd lang
tar -xvzf %{SOURCE1}
popd

%build
%cmake \
	-DINTERNAL_JREEN=OFF \
	-DBUILD_RELEASE=ON \
	-DBUILD_HATCHET=OFF
%make

%install
%makeinstall_std -C build

