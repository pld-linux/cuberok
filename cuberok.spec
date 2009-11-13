Summary:	Cuberok music player and a collection manager
Name:		cuberok
Version:	0.0.11
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Multimedia
Source0:	http://cuberok.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	0b09935acbf8e94645680b5a51081820
Patch0:		ffmpeg-headers.patch
BuildRequires:	audiere-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	libstdc++-devel
BuildRequires:	phonon-devel
BuildRequires:	qt4-build
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cuberok is a music player and a collection manager based on Qt4. It
has lightweight interface, music collection support and many features,
e.g. music autorating and Last.FM scrobbler.

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
%attr(755,root,root) %{_libdir}/%{name}/libplayer_ffmpeg.so
%attr(755,root,root) %{_libdir}/%{name}/libplayer_gst.so
%attr(755,root,root) %{_libdir}/%{name}/libplayer_phonon.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%lang(ru) %{_datadir}/%{name}/locale/%{name}_ru.qm
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
