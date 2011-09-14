Summary:	Cuberok music player and a collection manager
Name:		cuberok
Version:	0.0.11
Release:	0.3
License:	GPL v3+
Group:		X11/Applications/Multimedia
Source0:	http://cuberok.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	0b09935acbf8e94645680b5a51081820
Patch0:		ffmpeg-headers.patch
URL:		https://sites.google.com/site/cuberok/
BuildRequires:	audiere-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	libstdc++-devel
BuildRequires:	phonon-devel
BuildRequires:	qt4-build
BuildRequires:	taglib-devel
# for Amarok 1.4 import
Suggests:	QtSql-sqlite3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cuberok is a music player and a collection manager based on Qt4. It
has lightweight interface, music collection support and many features,
e.g. music autorating and Last.FM scrobbler.

%package backend-audiere
Summary:	Audiere backend for Cuberok
Summary(pl.UTF-8):	Wtyczki Audiere dla Cuberok
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-audiere
The Audiere Audio System is a portable audio library which supports
playing MP3, Ogg Vorbis, WAV, IT, XM, S3M, and MOD files.

This package contains Audiere backend for Cuberok.

%description backend-audiere -l pl.UTF-8
Wtyczki Audiere dla Cuberok.

%package backend-ffmpeg
Summary:	FFmpeg backend for Cuberok
Summary(pl.UTF-8):	Wtyczki FFmpeg dla Cuberok
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-ffmpeg
FFmpeg is a complete solution to record, convert and stream audio and
video.

This package contains FFmpeg backend for Cuberok.

%description backend-ffmpeg -l pl.UTF-8
Wtyczki FFmpeg dla Cuberok.

%package backend-gstreamer
Summary:	GStreamer backend for Cuberok
Summary(pl.UTF-8):	Wtyczki GStreamera dla Cuberok
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-plugins-good >= 0.10

%description backend-gstreamer
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related.

This package contains GStreamer backend for Cuberok.

%description backend-gstreamer -l pl.UTF-8
Wtyczki GStreamera dla Cuberok.

%package backend-phonon
Summary:	Phonon backend for Cuberok
Summary(pl.UTF-8):	Wtyczki Phonon dla Cuberok
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-phonon
Phonon is the multimedia API for Qt4/KDE4. Phonon was created to allow
KDE4 to be independent of any single multimedia framework such as
GStreamer or Xine and to provide a stable API for KDE4's lifetime. It
was done to fix problems of frameworks becoming unmaintained, API
instability, and to create a simple multimedia API.

This package contains Phonon backend for Cuberok.

%description backend-phonon -l pl.UTF-8
Wtyczki Phonon dla Cuberok.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 Cuberok.pro \
	CONFIG+=player_phonon
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README license.txt
%attr(755,root,root) %{_bindir}/cuberok
%dir %{_libdir}/cuberok
%attr(755,root,root) %{_libdir}/%{name}/libcuberok_style.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%lang(ru) %{_datadir}/%{name}/locale/%{name}_ru.qm
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm

%files backend-audiere
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libplayer_audiere.so

%files backend-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libplayer_ffmpeg.so

%files backend-gstreamer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libplayer_gst.so

%files backend-phonon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libplayer_phonon.so
%defattr(644,root,root,755)
