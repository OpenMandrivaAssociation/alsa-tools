# sb16_csp is added conditionally!
%define MODULES_NOCSPCTL as10k1 echomixer envy24control hdspconf hdsploader hdspmixer ld10k1 mixartloader pcxhrloader rmedigicontrol seq/sbiload sscape_ctl us428control usx2yloader vxloader
# qlo10k1 needs l10k1 and thus this package will only bootstrap if it's installed first
%define EXTRAS hdajackretask hda-verb hwmixvolume

%ifarch ppc %mips %arm
%define MODULES %{MODULES_NOCSPCTL}
%else
%define MODULES %{MODULES_NOCSPCTL} sb16_csp %{EXTRAS}
%endif

%define major 0
%define libname %mklibname lo10k1_ %{major}
%define devname %mklibname lo10k1 -d

Summary:	Advanced Linux Sound Architecture (ALSA) tools
Name:		alsa-tools
Version:	1.2.5
Release:	4
License:	GPLv2+
Group:		Sound
Url:		http://alsa-project.org
Source0:	ftp://ftp.alsa-project.org/pub/tools/%{name}-%{version}.tar.bz2
Source1:	90-alsa-tools-firmware.rules
Patch1:		alsa-tools-1.0.18-sscape_ctl.c.patch
# From Debian: adapt to udev instead of hotplug - AdamW 2008/03
Patch2:		alsa-tools-1.0.16-usx2yloader-udev.patch
# (tv) fix underlinking:
Patch3:		alsa-tools-1.0.17rc1-fix-link.patch

BuildRequires:	desktop-file-utils
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(xft)
BuildRequires:	systemd-rpm-macros

%rename		sb16_csp
%rename		sbiload
%rename		sscape_ctl
%rename		us428control
%rename		as10k1
Obsoletes:	ac3dec < 1.0.27-1

%description
Advanced Linux Sound Architecture (ALSA) utils. Modularized 
architecture with support for a large range of ISA and PCI cards.
Fully compatible with OSS/Lite (kernel sound drivers), but 
contains many enhanced features.

This source rpm package provides several sub packages:
* as10k1 - AS10k1 Assembler version A0.99
* cspctl - Sound Blaster 16 ASP/CSP control program
* envy24control - Control tool for Envy24 (ice1712) based sound cards
* hdspmixer - Mixer for the RME Hammerfall DSP cards
* rmedigicontrol - Control panel for RME Hammerfall cards
* sbiload - An OPL2/3 FM instrument loader for ALSA sequencer
* sscape_ctl - ALSA SoundScape control utility
* us428control - Control tool for Tascam 428

%package firmware
Summary:	ALSA tools for uploading firmware to some sound cards
License:	GPLv1
Group:		System/Kernel and hardware
Requires:	alsa-firmware >= 1.0.25
%rename		hdsploader
%rename		mixartloader
%rename		pcxhrloader
%rename		usx2yloader
%rename		vxloader

%description firmware
This package contains tools for flashing firmware into certain sound cards.
The following tools are available:

* hdsploader   - for RME Hammerfall DSP cards
* mixartloader - for Digigram miXart sound cards
* pcxhrloader  - for Digigram PCXHR sound cards
* usx2yloader  - second phase firmware loader for Tascam USX2Y USB sound cards
* vxloader     - for Digigram VX sound cards

%package -n ld10k1
Summary:	AS10k1 Assembler version A0.99
License:	GPLv1
Group:		System/Kernel and hardware

%description -n ld10k1
This is patch loader for EMU10K1 (EMU10K2) for ALSA.
This disables AC3 passthrough on SB Live.

There are two parts:
Server - ld10k1 - running as service - it is storing driver state - it must run
under root or by setuided
Client - lo10k1 - controls server and dump loader dl10k1 - loads dumps
previously created with lo10k1 & ld10k1.

ld10k1 will clear card DSP program and you will hear nothing.
You must load some patches to route sound from inputs to outputs (use
audigy_init script for audigy 1, 2 or init_live for sb live).
After loading patch check and set oss mixer emulation through proc file
(/proc/asound/card/oss_mixer)

In directory setup are some patches which I use on my Audigy for testing.
With this you will have exactly same mixer as with original driver (+headphone
control, not tested AudigyDrive inputs and outputs, AC3 passthrought).
Use as10k1 compiler from alsa-tools package to compile patches.

%package -n %{libname}
Summary:	Ld10k1_ library
Group:		System/Libraries
Obsoletes:	%{_lib}lo10k10 < 1.0.27-2
Obsoletes:	%{_lib}lo10k1_0_ < 1.1.0-3

%description -n %{libname}
This is the library of ld10k1.

%package -n %{devname}
Summary:	Development files for l10k1
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	%{_lib}lo10k10-devel < 1.0.27-2

%description -n %{devname}
This package contains files needed in order to develop an application
that made use of the ld10k1 library.

%package echomixer
Summary:	Mixer for Echoaudio cards
Group:		Sound
%rename echomixer

%description echomixer
Mixer application for Echoaudio cards

%files echomixer
%{_bindir}/echomixer
%{_datadir}/icons/hicolor/*/apps/echomixer.png
%{_datadir}/applications/echomixer.desktop

%package envy24
Summary:	Tools for working with Envy24 soundcards
Group:		Sound
%rename		envy24control

%description envy24
Tools for working with Envy24 soundcards

%files envy24
%{_bindir}/envy24control
%{_datadir}/icons/hicolor/*/apps/envy24control.png
%{_datadir}/applications/envy24control.desktop
%doc %{_mandir}/man1/envy24control.1*

%package rme
Summary:	Tools for working with RME Hammerfall soundcards
Group:		Sound
%rename		hdspconf
%rename		hdspmixer
%rename		rmedigicontrol

%description rme
Tools for working with RME Hammerfall soundcards

%files rme
%{_bindir}/hdspconf
%{_bindir}/hdspmixer
%{_bindir}/rmedigicontrol
%{_datadir}/icons/hicolor/*/apps/hdspconf.png
%{_datadir}/icons/hicolor/*/apps/hdspmixer.png
%{_datadir}/applications/hdspmixer.desktop
%{_datadir}/applications/hdspconf.desktop
%{_datadir}/applications/rmedigicontrol.desktop

%prep
%autosetup -p1

cd envy24control
touch NEWS ChangeLog
cd ..

find . -name "Make*" -o -name "configure.*" |xargs sed -i -e 's,configure\.in,configure.ac,g'

%build
for i in %{MODULES}; do
cd ${i}
libtoolize -c -f
autoreconf
%configure
%make_build
cd -
done

%install
for i in %{MODULES}; do
cd ${i}
  %make_install
cd -
done

# install menu entries
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/echomixer.desktop << EOF
[Desktop Entry]
Name=Echo mixer
Comment=Control tool for Echoaudio sound cards
Exec=%{_bindir}/echomixer
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Mixer;
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/envy24control.desktop << EOF
[Desktop Entry]
Name=Envy24control
Comment=Control tool for Envy24 (ice1712) based sound cards
Exec=%{_bindir}/envy24control
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Mixer;
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/rmedigicontrol.desktop << EOF
[Desktop Entry]
Name=RME Digicontrol
Comment=Control panel for RME Hammerfall
Exec=%{_bindir}/rmedigicontrol
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Mixer;
EOF

# fix .desktop files
sed -i 's,.png,,' %{buildroot}%{_datadir}/applications/{hdspconf,hdspmixer}.desktop

desktop-file-install \
	--vendor="" \
	--remove-key="Encoding" \
	--remove-key="FilePattern" \
	--remove-category="Application" \
	--set-key=Hidden --set-value=true \
	--dir=%{buildroot}%{_datadir}/applications/ \
	%{buildroot}%{_datadir}/applications/*

# udev rules file for usx2yloader - AdamW 2008/03
mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}

%files
%{_bindir}/as10k1
%{_bindir}/sbiload
%{_bindir}/sscape_ctl
%{_bindir}/us428control
%optional %{_datadir}/icons/hicolor/*/apps/hdajackretask.png
%optional %{_datadir}/icons/hicolor/*/apps/hwmixvolume.png
%optional %{_datadir}/applications/hdajackretask.desktop
%optional %{_datadir}/applications/hwmixvolume.desktop
%{_datadir}/sounds/opl3/

%ifnarch ppc %mips %arm
%{_bindir}/hda-verb
%{_bindir}/hdajackretask
%{_bindir}/hwmixvolume
%{_bindir}/cspctl
%doc %{_mandir}/man1/cspctl.*
%endif

%files firmware
%{_udevrulesdir}/90-alsa-tools-firmware.rules
%(dirname %{_udevrulesdir})/tascam_fpga
%(dirname %{_udevrulesdir})/tascam_fw
%{_bindir}/hdsploader
%{_bindir}/mixartloader
%{_bindir}/pcxhrloader
%{_bindir}/usx2yloader
%{_bindir}/vxloader

%files -n ld10k1
%{_bindir}/lo10k1
%{_bindir}/init_audigy
%{_bindir}/init_audigy_eq10
%{_bindir}/init_live
%{_datadir}/ld10k1
%{_sbindir}/ld10k1
%{_sbindir}/dl10k1
%{_sbindir}/ld10k1d

%files -n %{libname}
%{_libdir}/liblo10k1.so.%{major}*

%files -n %{devname}
%{_includedir}/lo10k1
%{_datadir}/aclocal/ld10k1.m4
%{_libdir}/liblo10k1.so
