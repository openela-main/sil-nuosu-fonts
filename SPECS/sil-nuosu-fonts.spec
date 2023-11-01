%global fontname sil-nuosu
%global fontconf 66-%{fontname}.conf

%global archivename NuosuSIL-2.200.tar.xz

Name:           %{fontname}-fonts
Version:        2.200
Release:        2%{?dist}
Summary:        The Nuosu SIL Font

License:        OFL
URL:            http://scripts.sil.org/SILYi_home
Source0:        %{archivename}
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
The Nuosu SIL Font is a single Unicode font for the standardized Yi script
used by a large ethnic group in southwestern China.
Until this version, the font was called SIL Yi.

%prep
%setup -q -n NuosuSIL-%{version}
sed -i 's/\r//' OFL.txt FONTLOG.txt

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc OFL.txt FONTLOG.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Apr  1 2021 Peng Wu <pwu@redhat.com> - 2.200-2
- Rebuild the package
- Resolves: #1762623

* Tue Mar 30 2021 Peng Wu <pwu@redhat.com> - 2.200-1
- Update to 2.200
- Corrected shape of U+300D and U+300F
- Resolves: #1762623

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.1.1-9
- Add metainfo file to show this font in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Feb 12 2011  Peng Wu <pwu@redhat.com> - 2.1.1-3
- Add document.

* Sun Jan 30 2011  Peng Wu <pwu@redhat.com> - 2.1.1-2
- Clean the spec file and add fontconfig file

* Wed Jan 26 2011  Peng Wu <pwu@redhat.com> - 2.1.1-1
- Initial package
