mkdir -v $(xdg-user-dir DOWNLOAD)/ISO

#Ubuntu 18.04 TLS
wget -q --show-progress -O $(xdg-user-dir DOWNLOAD)/ISO/ubuntu-mate-18.04.4-desktop-amd64.iso http://cdimage.ubuntu.com/ubuntu-mate/releases/18.04/release/ubuntu-mate-18.04.4-desktop-amd64.iso
wget -q --show-progress -O $(xdg-user-dir DOWNLOAD)/ISO/SHA256SUMS_ubuntu-1804_desktop http://cdimage.ubuntu.com/ubuntu-mate/releases/18.04/release/SHA256SUMS
cd $(xdg-user-dir DOWNLOAD)/ISO/ && sha256sum -c SHA256SUMS_ubuntu-1804_desktop --ignore-missing

#Ubuntu Server
wget -q --show-progress -O $(xdg-user-dir DOWNLOAD)/ISO/ubuntu-18.04.4-server-amd64.iso http://cdimage.ubuntu.com/releases/18.04.4/release/ubuntu-18.04.4-server-amd64.iso
wget -O $(xdg-user-dir DOWNLOAD)/ISO/SHA256SUMS_ubuntu-1804_server -q --show-progress http://cdimage.ubuntu.com/releases/18.04.4/release/SHA256SUMS
cd $(xdg-user-dir DOWNLOAD)/ISO/ && sha256sum -c SHA256SUMS_ubuntu-1804_server --ignore-missing

mkdir -v $(xdg-user-dir DESKTOP)/Workstation_ISO

#Decompression of ISO file
engrampa -e $(xdg-user-dir DESKTOP)/Workstation_ISO $(xdg-user-dir DOWNLOAD)/ISO/ubuntu-mate-18.04.4-desktop-amd64.iso

rm $(xdg-user-dir DESKTOP)/Workstation_ISO/isolinux/txt.cfg
touch $(xdg-user-dir DESKTOP)/Workstation_ISO/isolinux/txt.cfg

#makes isolinux/txt.cfg which should be the same as /srv/tftp/linux0.cfg/default
cat <<EOT >> $(xdg-user-dir DESKTOP)/Workstation_ISO/isolinux/txt.cfg
default auto-install
label auto-install
menu label ^Ubuntu MATE Automaatpaigaldus
kernel /casper/vmlinuz
append file=/cdrom/preseed/autoinstall.seed boot=casper automatic-ubiquity initrd=/casper/initrd quiet splash noprompt ---
EOT

#makes autoinstall.seed
cat <<EOT >> $(xdg-user-dir DESKTOP)/Workstation_ISO/preseed/autoinstall.seed
# WORKSTATION

# This preset file was created based on the documentation: # https://help.ubuntu.com/lts/installation-guide/amd64/apbs04.html

# Since this is the "Desktop" version, I use the debian-installer commands in ubiquity format. Ubiquity is a live-installation environment.

# Creating disk partitions

# Select to use the first SCSI / SATA drive

ubiquity partman-auto/disk string /dev/sda

# Select a method for creating partitions. Variants "regular", "lvm" or "crypto". In the latter two cases, the LVM disk partition system is used. In the latter case, encryption is also used.

ubiquity partman-auto/method string regular

# Avoiding warnings if LVM partitions have previously been selected on the drive and will be deleted.

ubiquity partman-lvm/device_remove_lvm boolean true

# Avoiding warnings if a RAID array has previously been selected on the disk and will be deleted.

ubiquity partman-md/device_remove_md boolean true

# Select a "recipe" for creating predefined partitions. In this case, separate / (system) and / home disk partitions are created.

ubiquity partman-auto/choose_recipe select home

# Disk partitions are created without asking for confirmation. Because it is a BIOS-type machine, MBR-type partitions come by default.

ubiquity partman-partitioning/confirm_write_new_label boolean true

ubiquity partman/choose_partition select finish

ubiquity partman/confirm boolean true

ubiquity partman/confirm_nooverwrite boolean true

# System language selection, input language selection and keyboard

# Operating system language.

ubiquity debian-installer/locale string en_US.UTF-8

# If necessary, add support for other languages

# ubiquity localechooser / supported-locales multiselect en_US.UTF-8 nl_NL.UTF-8

# To select the keyboard layout Estonian. The possible variants can be viewed with the command: localectl list-x11-keymap-layouts. Only one can be used for installation.

ubiquity keyboard-configuration/layoutcode string ee

# Turns off the automatic keyboard layout detection question.

ubiquity console-setup/ask_detect boolean false

# Set the clock and time zone

# Check if the hardware clock is set to UTC.

ubiquity clock-setup/utc-auto boolean true

ubiquity clock-setup/utc boolean true

# Time zone selection

ubiquity time/zone string Europe/Tallinn

# Check whether to use NTP (Network Time Protocol) to set the time during installation.

ubiquity clock-setup/ntp boolean true

# Minimal installation option

ubiquity ubiquity/minimal_install boolean true

# Downloading updates during installation

ubiquity unattended-upgrades/enable_auto_updates boolean true

# Assignment of repositories

# Selection of the country whose servers are used. The https://docs.moodle.org/dev/Table_of_locales table lists the locales from which the country code can be used

ubiquity mirror/country string EE

# Enabling multiverse, universe, and restricted APT repositories

ubiquity apt-setup/multiverse boolean true

ubiquity apt-setup/restricted boolean true

ubiquity apt-setup/universe boolean true

# Creating a user “student” with a password

# User's full name

ubiquity passwd/user-fullname string Student

# Username

ubiquity passwd/username string student

# User password

ubiquity passwd/user-password password student

ubiquity passwd/user-password-again password student

# Enabling a weak password

ubiquity user-setup/allow-password-weak boolean true

# Installing additional software

# Installing system updates

# Adding GIMP image editing software

# Adding an APT repository and installing Byobu software

# Commands must be separated by a semicolon, use "\" for line breaks.

# Symbol "\" Cannot be used inside commands.

ubiquity ubiquity/success_command \

in-target add-apt-repository -y ppa:byobu/ppa; \

in-target apt-get update -y; \

in-target apt-get upgrade -y; \

in-target apt-get dist-upgrade; \

in-target apt-get autoremove; \

in-target apt-get autoclean; \

in-target apt-get clean; \

in-target apt-get install -y byobu; \

in-target apt-get install -y gimp;

# Automatic restart after installation is complete. To turn it off: ubiquity ubiquity / poweroff boolean true

ubiquity ubiquity/reboot boolean true
EOT 

mkisofs -r -V "UbuntuAutomaatpaigaldus" -cache-inodes -J -l -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o $(xdg-user-dir DESKTOP)/ubuntu-desktop-automaatpaigaldus.iso $(xdg-user-dir DESKTOP)/Workstation_ISO
