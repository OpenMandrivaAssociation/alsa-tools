# TODO FIXME: WE SHOULD SPLIT alsa-firmware from alsa-tools

# sb16_csp is added conditionally!
%define MODULES_NOCSPCTL ac3dec as10k1 echomixer envy24control hdspconf hdsploader hdspmixer ld10k1 mixartloader pcxhrloader rmedigicontrol seq/sbiload sscape_ctl us428control usx2yloader vxloader
# qlo10k1 needs l10k1 and thus this package will only bootstrap if it's installed first

%ifarch ppc %mips %arm
%define MODULES %{MODULES_NOCSPCTL}
%else
%define MODULES %{MODULES_NOCSPCTL} sb16_csp
%endif

%define tool_fver 1.0.25
%define firmware_fver 1.0.25
%define firm_beta 0
%define tool_beta 0
%define ld10k1_major 0

%define ld10k1_name lo10k1
%define ld10k1_libname_orig lib%ld10k1_name
%define ld10k1_libname %mklibname %ld10k1_name %ld10k1_major

%if %tool_beta
%define fname %name-%tool_fver%tool_beta
%else
%define fname %name-%tool_fver
%endif
%if %firm_beta
%define firm_name alsa-firmware-%firmware_fver%firm_beta
%else
%define firm_name alsa-firmware-%firmware_fver
%endif

Name:		alsa-tools
Version:	%tool_fver
%if %firm_beta
Release:	0.%{firm_beta}.1
%else
Release:	1
%endif
Summary:	Advanced Linux Sound Architecture (ALSA) tools
License:	GPL
URL:		http://alsa-project.org
Source0:	ftp://ftp.alsa-project.org/pub/tools/%fname.tar.bz2
Source1:	ftp://ftp.alsa-project.org/pub/firmware/%firm_name.tar.bz2
Source2:	audio_dock_netlist.h
Patch0:		alsa-tools-1.0.18-sscape_ctl.c.patch
# From Debian: adapt to udev instead of hotplug - AdamW 2008/03
Patch2:		alsa-tools-1.0.16-usx2yloader-udev.patch
# (tv) fix underlinking:
Patch3:		alsa-tools-1.0.17rc1-fix-link.patch
# (hk) fix build errors with -Wformat -Werror=format-security
Patch4:		alsa-tools-1.0.19-format-security.patch
Group:		Sound
BuildRequires:	libalsa-devel >= %version
BuildRequires:	fltk-devel
BuildRequires:	gtk2-devel
BuildRequires:	ncurses-devel
BuildRequires:	automake

%description
Advanced Linux Sound Architecture (ALSA) utils. Modularized 
architecture with support for a large range of ISA and PCI cards.
Fully compatible with OSS/Lite (kernel sound drivers), but 
contains many enhanced features.

This source rpm package provides several sub packages:
* ac3dec - A free AC-3 stream decoder
* as10k1 - AS10k1 Assembler version A0.99
* cspctl - Sound Blaster 16 ASP/CSP control program
* envy24control - Control tool for Envy24 (ice1712) based soundcards
* hdsploader - Firmware loader for RME Hammerfall cards
* hdspmixer - Mixer for the RME Hammerfall DSP cards
* mixartloader - Firmware loader for Digigram's miXart
* rmedigicontrol - Control panel for RME Hammerfall cards
* sbiload - An OPL2/3 FM instrument loader for ALSA sequencer
* sscape_ctl - ALSA SoundScape control utility
* us428control - Control tool for Tascam 428
* usx2yloader - Firmware loader for Tascam USX2Y USB soundcards
* vxloader - Firmware loader for Digigram's VX-board

%package -n	ac3dec
Summary:	A free AC-3 stream decoder
License:	GPL
Group:		Sound

%description -n	ac3dec
This software is completely useless to 99.99 percent of users
out there. It is mostly of use to those interested in audio
coding research and evaluating codecs. It could theoretically
be used as a portion of a DVD playback system for unix systems. 

%package -n	aica-firmware
Summary:	Firwmare for Sega Dreamcast
License:	GPL
Group:		Sound

%description -n	aica-firmware
This is the firmware data for Sega Dreamcast.

%package -n	asihpi-firmware
Summary:	Firwmare for asihpi drivers
License:	GPL
Group:		Sound
Obsoletes:  asihpi-firwmare
Provides:   asihpi-firwmare

%description -n	asihpi-firmware
This is the firmware data for ASIHPI drivers.

%package -n	as10k1
Summary:	AS10k1 Assembler version A0.99
License:	GPL
Group:		Sound

%description -n	as10k1
This is an assembler for the emu10k1 DSP chip present in the
creative SB live, PCI 512, and emu APS sound cards. It is used to
make audio effects such as a flanger, chorus or reverb.

%package -n	echomixer
Summary:	Control tool for Echoaudio soundcards
License:	GPL
Group:		Sound

%description -n	echomixer
Emixer is a tool to control all the features of any Echoaudio soundcard.
This includes clock sources, input and output gains, mixers, etc.

%package -n	emagic-firmware
Summary:	Firwmare for Emagic EMI 2|6 Audio Interface
License:	GPL
Group:		Sound

%description -n	emagic-firmware
This is the firmware data for Emagic EMI 2|6 Audio Interface.

%package -n	emu1010-firmware
Summary:	Firwmare for EMU Systems EMU1010 PCI card
License:	GPL
Group:		Sound

%description -n	emu1010-firmware
This is the firmware data for EMU Systems EMU1010 PCI card.

%package -n	envy24control
Summary:	Control tool for Envy24 (ice1712) based soundcards
License:	GPL
Group:		Sound

%description -n	envy24control
envy24control allows control of the digital mixer, channel gains
and other hardware settings for sound cards based on the ice1712
chipset (Midiman Delta series, Terratec EWS and EWX series). It 
also displays a level meter for each input and output channel.

%package -n	hdspconf
Summary:	GUI to control the Hammerfall HDSP ALSA settings
License:	GPL
Group:		Sound

%description -n	hdspconf
HDSPConf is a GUI to control the Hammerfall HDSP ALSA Settings.

%package -n	hdsploader
Summary:	Firmware loader for the RME Hammerfall DSP cards
License:	GPL
Group:		Sound

%description -n	hdsploader
Firmware loader for the RME Hammerfall DSP cards

%package -n	hdspmixer
Summary:	Mixer for the RME Hammerfall DSP cards
License:	GPL
Group:		Sound

%description -n	hdspmixer
Mixer for the RME Hammerfall DSP cards

%package -n	korg1212-firmware
Summary:	Firwmare for Korg1212
License:	GPL
Group:		Sound

%description -n	korg1212-firmware
This is the firmware data for Korg1212.

%package -n	ld10k1
Summary:	AS10k1 Assembler version A0.99
License:	GPL
Group:		Sound

%description -n	ld10k1
This is patch loader for EMU10K1 (EMU10K2) for ALSA.
This dissables AC3 passthrough on SB Live.

There are two parts:
Server - ld10k1 - runing as service - it is storing driver state - it must run
        under root or by setuided
Client - lo10k1 - controls server
and dump loader dl10k1 - loads dumps previously created with lo10k1 & ld10k1.

ld10k1 will clear card DSP program and you will hear nothing.
You must load some patches to route sound from inputs to outputs (use
audigy_init script for audigy 1, 2 or init_live for sb live).
After loading patch check and set oss mixer emulation through proc file
(/proc/asound/card/oss_mixer)

In directory setup are some patches which I use on my Audigy for testing.
With this you will have exactly same mixer as with original driver (+headphone
control, not tested AudigyDrive inputs and outputs, AC3 passthrought).
Use as10k1 compiler from alsa-tools package to compile patches.

%package -n %ld10k1_libname
Summary:	Ld10k1_ library
Group:		Sound
Provides:	%ld10k1_libname_orig = %version
Obsoletes:	%ld10k1_libname_orig
Conflicts:	ld10k1 < 1.0.12

%description -n %ld10k1_libname
This is the library of ld10k1.

%package -n %{ld10k1_libname}-devel
Summary:    Development files for l10k1
Group:      Development/C
Requires:   %{ld10k1_libname} >= %version
Provides:   %{ld10k1_libname_orig}-devel = %version-%release
Obsoletes:  %{ld10k1_libname_orig}-devel

%description -n %{ld10k1_libname}-devel
This package contains files needed in order to develop an application
that made use of the ld10k1 library.

%package -n	maestro3-firmware
Summary:	Firwmare for Maestro3
License:	GPL
Group:		Sound

%description -n	maestro3-firmware
This is the firmware data for Maestro3.

%package -n	mixartloader
Summary:	Firmware loader for Digigram miXart
License:	GPL
Group:		Sound

%description -n	mixartloader
Firmware loader for Digigram miXart

%package -n	pcxhrloader
Summary:	Firmware loader for Digigram PCXHR soundcards
License:	GPL
Group:		Sound

%description -n	pcxhrloader
Helper program to load the firmware binaries onto the Digigram's PCXHR-board
sound drivers.

%package -n	rmedigicontrol
Summary:	Control panel for the RME Hammerfall DSP cards
License:	GPL
Group:		Sound

%description -n	rmedigicontrol
Control panel for the RME Hammerfall DSP cards

%ifnarch ppc %mips %arm
%package -n	sb16_csp
Summary:	Sound Blaster 16 ASP/CSP control program
License:	GPL
Group:		Sound
Provides:   cspctl
Obsoletes:   cspctl

%description -n	sb16_csp
Cspctl is a Sound Blaster 16 ASP/CSP control program. It is a simple CSP
microcode loader for Crative Sound Blaster 16ASP and some Sound Blaster AWE32
sound cards with Creative Signal Processor (CSP) chip (CT1748A) installed.
cspctl can also be used as a post-install function to snd-sb16-csp module to
load default codec at module installation.
If CSP chip is successfully detected and initialized, it will be installed as a
hardware dependent device hwC0D2 into /dev/snd directory. Currently, following
codecs can be loaded to CSP device:

- wfm0001a.csp  QSound decoder
- wfm0006a.csp  A-law codec
- wfm0007a.csp  u-law codec
- wfm0011a.csp  IMA ADPCM codec (distorted output for IMA test files)
- wfm0200a.csp  Creative ADPCM codec (maybe Intel/DVI IMA ADPCM compatible)
- wfm0202a.csp  Fast Speech 8 codec
- wfm0203a.csp  Fast Speech 10 codec

These codecs are not yet supported by ALSA:
- wfm0201a.csp  Text2Speech decoder

With QSound decoder microcode loaded, all simple PCM file formats can be
played with QSound 180 degree positioning applied. QSound element is
dynamically added into mixer structure as 3DEffect1-space element. It will
only show if support for CSP has been compiled into ALSA drivers, CSP chip
has been found, and QSound codec is loaded into CSP. When enabled, QSound
position can be dynamically changed by mixer slider.

Driver supports autoloading of u-Law, A-Law and Ima-ADPCM hardware codecs.
Autoloading is active only when there is no microcode loaded to CSP, and there
is no need to preload appropriate *.csp files.

If hardware codec microcode has been manually loaded, then CSP will support
only loaded PCM format and autoloading will be disabled.  In such case, proc
interface will show loaded codec properties:
%endif

%package -n	sb16-firmware
Summary:	Firwmare for SB16 Advanced Signal Processor
License:	GPL
Group:		Sound

%description -n	sb16-firmware
This is the firmware data for SB16 Advanced Signal Processor.

%package -n	sbiload
Summary:	An OPL2/3 FM instrument loader for ALSA sequencer
License:	GPL
Group:		Sound

%description -n	sbiload
An OPL2/3 FM instrument loader for ALSA sequencer

%package -n	sscape_ctl
Summary:	ALSA SoundScape control utility
License:	GPL
Group:		Sound

%description -n	sscape_ctl
ALSA SoundScape control utility

%package -n	turtlebeach-firmware
Summary:	Firwmare for turtlebeach
License:	GPL
Group:		Sound

%description -n	turtlebeach-firmware
This is the firmware data for turtlebeach.

%package -n	usx2yloader
Summary:	Firmware loader for Tascam USX2Y USB
License:	GPL
Group:		Sound
Requires:	fxload

%description -n	usx2yloader
Helper program to load the firmware binaries onto the Tascam USX2Y USB.

%package -n	us428control
Summary:	Control for Tascam 428
License:	GPL
Group:		Sound

%description -n	us428control
Controller program for the Tascam 428 workstation.

%package -n	vxloader
Summary:	Firmware loader for Digigram VX soundcards
License:	GPL
Group:		Sound

%description -n	vxloader
Helper program to load the firmware binaries onto the Digigram's VX-board sound
drivers.

%package -n	yamaha-firmware
Summary:	Firwmare for Yamaha DS-1 sound cards
License:	GPL
Group:		Sound

%description -n	yamaha-firmware
This is the firmware data for Yamaha DS-1 sound cards.

%prep
%setup -q -a 1 -n %fname
%patch0 -p0
%patch2 -p1 -b .usx2yudev
%patch3 -p1 -b .link
%patch4 -p1 -b .format-security
cp %SOURCE2 ./%firm_name/emu/audio_dock_netlist.h
pushd envy24control
touch NEWS ChangeLog
popd

%build
for i in %{MODULES} %firm_name; do
pushd ${i}
# (tv) force it not to lookup aclocal-1.9 & co
libtoolize -c -f
autoreconf
%configure2_5x --with-hotplug-dir=/lib/firmware
%make
popd
done

%install
rm -rf %{buildroot}

for i in %{MODULES} %firm_name; do
pushd ${i}
%makeinstall_std
popd
done

# install some extra stuff for ac3dec
install -m755 ac3dec/test/dither_test %{buildroot}%{_bindir}/dither_test
install -m755 ac3dec/test/imdct_test %{buildroot}%{_bindir}/imdct_test

# install menu entries


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-echomixer.desktop << EOF
[Desktop Entry]
Name=Echo mixer
Comment=Control tool for Echoaudio soundcards
Exec=%{_bindir}/echomixer
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Mixer;
EOF


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-envy24control.desktop << EOF
[Desktop Entry]
Name=Envy24control
Comment=Control tool for Envy24 (ice1712) based soundcards
Exec=%{_bindir}/envy24control
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Mixer;
EOF



mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-rmedigicontrol.desktop << EOF
[Desktop Entry]
Name=RME Digicontrol
Comment=Control panel for RME Hammerfall
Exec=%{_bindir}/rmedigicontrol
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Mixer;
EOF

# udev rules file for usx2yloader - AdamW 2008/03
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
cat > %{buildroot}%{_sysconfdir}/udev/rules.d/55-alsa-tascam-firmware-loaders.rules << EOF
# TASCAM US-428 usb sound card.
    BUS=="usb", ACTION=="add", SYSFS{idVendor}=="1604", SYSFS{idProduct}=="8000", RUN+="/lib/udev/tascam_fw"
    BUS=="usb", ACTION=="add", SYSFS{idVendor}=="1604", SYSFS{idProduct}=="8001", RUN+="/lib/udev/tascam_fpga"
# TASCAM US-224 usb sound card.
    BUS=="usb", ACTION=="add", SYSFS{idVendor}=="1604", SYSFS{idProduct}=="8004", RUN+="/lib/udev/tascam_fw"
    BUS=="usb", ACTION=="add", SYSFS{idVendor}=="1604", SYSFS{idProduct}=="8005", RUN+="/lib/udev/tascam_fpga"
# TASCAM US-112 usb sound card.
    BUS=="usb", ACTION=="add", SYSFS{idVendor}=="1604", SYSFS{idProduct}=="8006", RUN+="/lib/udev/tascam_fw"
    BUS=="usb", ACTION=="add", SYSFS{idVendor}=="1604", SYSFS{idProduct}=="8007", RUN+="/lib/udev/tascam_fpga"
EOF


%files -n	ac3dec
%doc ac3dec/COPYING ac3dec/README ac3dec/TODO
%{_bindir}/ac3dec
%{_bindir}/extract_ac3
%{_bindir}/dither_test
%{_bindir}/imdct_test

%files -n	aica-firmware
/lib/firmware/aica_firmware.bin

%files -n	asihpi-firmware
/lib/firmware/asihpi

%files -n	as10k1
%doc as10k1/README as10k1/COPYING as10k1/examples
%{_bindir}/as10k1

%files -n	echomixer
%doc echomixer/AUTHORS echomixer/COPYING echomixer/README
%{_bindir}/echomixer
%_datadir/applications/mandriva-echomixer.desktop
/lib/firmware/ea

%files -n	emagic-firmware
/lib/firmware/emagic/

%files -n	emu1010-firmware
/lib/firmware/emu/

%files -n	envy24control
%doc envy24control/AUTHORS envy24control/COPYING envy24control/README
%{_bindir}/envy24control
%{_mandir}/man1/envy24control.1*
%_datadir/applications/mandriva-envy24control.desktop
#%{_iconsdir}/envy24control.png

%files -n	hdspconf
%doc hdspconf/COPYING hdspconf/README
%_bindir/hdspconf
%_datadir/pixmaps/hdspconf.png
%_datadir/applications/hdspconf.desktop

%files -n	hdsploader
%doc hdsploader/AUTHORS hdsploader/COPYING hdsploader/README
%{_bindir}/hdsploader
%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/hdsploader
/lib/firmware/digiface_*
/lib/firmware/multiface_*
/lib/firmware/rpm_firmware.bin

%files -n	hdspmixer
%doc hdspmixer/AUTHORS hdspmixer/COPYING hdspmixer/README
%{_bindir}/hdspmixer
%_datadir/applications/hdspmixer.desktop
%_datadir/pixmaps/hdspmixer.png

%files -n	korg1212-firmware
/lib/firmware/korg/k1212.dsp

%files -n	ld10k1
%doc as10k1/README as10k1/COPYING as10k1/examples
%_bindir/lo10k1
%_bindir/init_audigy
%_bindir/init_audigy_eq10
%_bindir/init_live
%_datadir/ld10k1
%_sbindir/ld10k1
%_sbindir/dl10k1
%_sbindir/ld10k1d

%files -n %ld10k1_libname
%_libdir/lib%{ld10k1_name}.so.*

%files -n %{ld10k1_libname}-devel
%_includedir/lo10k1
%_datadir/aclocal/ld10k1.m4
%_libdir/lib%{ld10k1_name}.so

%files -n	maestro3-firmware
/lib/firmware/ess

%files -n	mixartloader
%{_bindir}/mixartloader
%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/mixartloader
/lib/firmware/mixart/

%files -n	rmedigicontrol
%doc rmedigicontrol/COPYING rmedigicontrol/README
%{_bindir}/rmedigicontrol
%_datadir/applications/mandriva-rmedigicontrol.desktop

%files -n	sb16-firmware
/lib/firmware/sb16/

%files -n	sbiload
%doc seq/sbiload/COPYING seq/sbiload/README
%{_bindir}/sbiload
%{_datadir}/sounds/opl3/

%files -n	sscape_ctl
%{_bindir}/sscape_ctl

%files -n	us428control
%{_bindir}/us428control

%files -n	usx2yloader
%doc usx2yloader/README
%{_bindir}/usx2yloader
/lib/udev/tascam*
%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/usx2yloader
%{_sysconfdir}/udev/rules.d/55-alsa-tascam-firmware-loaders.rules

%files -n	pcxhrloader
%doc vxloader/README
%{_bindir}/pcxhrloader
%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/pcxhrloader
/lib/firmware/pcxhr/

%ifnarch ppc %mips %arm
%files -n	sb16_csp
%doc sb16_csp/COPYING sb16_csp/README
%_bindir/cspctl
%_mandir/man1/cspctl.*
%endif

%files -n	turtlebeach-firmware
/lib/firmware/turtlebeach/msndinit.bin
/lib/firmware/turtlebeach/msndperm.bin
/lib/firmware/turtlebeach/pndsperm.bin
/lib/firmware/turtlebeach/pndspini.bin

%files -n	vxloader
%doc vxloader/README
%{_bindir}/vxloader
%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/firmware
%{_datadir}/alsa/firmware/vxloader
/lib/firmware/vx/

%files -n	yamaha-firmware
/lib/firmware/yamaha/ds1_ctrl.fw
/lib/firmware/yamaha/ds1_dsp.fw
/lib/firmware/yamaha/ds1e_ctrl.fw
/lib/firmware/yamaha/yss225_registers.bin
