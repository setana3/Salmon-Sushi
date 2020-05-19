#!/bin/bash

# MACHINENAME is a variable whose value is obtained from the first argument when the script is run, ie the name of the planned virtual machine.

MACHINENAME=$1

# The script is run with one variable: ./script_name.sh "name of the virtual machine to be created"

# Used materials: https://www.andreafortuna.org/2019/10/24/how-to-create-a-virtualbox-vm-from-command-line/

# You can read more about the commands used in the script in the VirtualBox documentation.

# https://www.virtualbox.org/manual/ch08.htm

# Creating and registering a virtual machine using VirtualBox. When using --register parameter, the manually created machine does not need to be registered separately for the VirtualBox software, the registration is performed during the creation.

# All different --ostype variants can be displayed with the command: “VBoxManage list ostypes”

# --basefolder indicates where the virtual machine to be created will be located.

VBoxManage createvm --name $MACHINENAME --ostype "Ubuntu_64" --register --basefolder $(xdg-user-dir DESKTOP)

# Enable I/O APIC

VBoxManage modifyvm $MACHINENAME --ioapic on

# Defining Random Access Memory and Video Memory

VBoxManage modifyvm $MACHINENAME --memory 2048 --vram 128

# Graphics controller selection. Options:

# -graphicscontroller none|vboxvga|vmsvga|vboxsvga

VBoxManage modifyvm $MACHINENAME --graphicscontroller vmsvga

# Network interface type selection: intnet=Internal Network. Võimalik lisada ka mitu. Formaat on järgmine: --nic<1-N> ning tüüp: none|null|nat|natnetwork|bridged|intnet|hostonly|generic

VBoxManage modifyvm $MACHINENAME --nic1 intnet

# Virtuaalse kõvaketta loomine. --size parameeter on megabaitides.

# --variant Standard dünaamiliselt suurenev ketas.

VBoxManage createmedium disk --filename $(xdg-user-dir DESKTOP)/$MACHINENAME/$MACHINENAME_DISK.vdi --size 25000 --format VDI --variant Standard

# Kontrolleri lisamine mäluseadmete jaoks

VBoxManage storagectl $MACHINENAME --name "SATA Controller" --add sata --controller IntelAhci

# Kõvaketta külge haakimine

VBoxManage storageattach $MACHINENAME --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium $(xdg-user-dir DESKTOP)/$MACHINENAME/$MACHINENAME_DISK.vdi

# Alglaadimisjärjekorra seadistamine

VBoxManage modifyvm $MACHINENAME --boot1 disk --boot2 net --boot3 none --boot4 none

# Virtuaalmasina käivitus

VBoxManage startvm $MACHINENAME