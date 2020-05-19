#!/bin/bash

# MACHINENAME is a variable whose value is obtained from the first argument when the script is run, ie the name of the planned virtual machine.

MACHINENAME="VIRTUAALMASINALE_PANDAV_NIMI"

# ISO_NAME is a variable whose value is derived from another argument when the script is run, namely the name of a previously created ISO file.

ISO_NAME="ISO_FAILI_NIMI"

# The script is run with two variables: ./script_name.sh "name of the virtual machine to be created" "ISO name"

# The following materials were used: https://www.andreafortuna.org/2019/10/24/how-to-create-a-virtualbox-vm-from-command-line/

# You can read more about the commands used in the script in the VirtualBox documentation.

# https://www.virtualbox.org/manual/ch08.htm

# Creating and registering a virtual machine with VirtualBox. In case --register parameter is used, the manually created machine does not need to be registered separately for the VirtualBox software, registration is carried out automatically during creation.

# All different --ostype variants can be displayed with the command: “VBoxManage list ostypes”

# --basefolder indicates where the virtual machine to be created will be located.

VBoxManage createvm --name $MACHINENAME --ostype "Ubuntu_64" --register --basefolder $(xdg-user-dir DESKTOP)

# Enable I/O APIC

VBoxManage modifyvm $MACHINENAME --ioapic on

# Assigning Random Access Memory and Video Memory

VBoxManage modifyvm $MACHINENAME --memory 2048 --vram 128

# Graphics controller selection. Options:

# -graphicscontroller none|vboxvga|vmsvga|vboxsvga

VBoxManage modifyvm $MACHINENAME --graphicscontroller vmsvga

# Network interface type selection, addins several is also possible. The format is as follows: --nic <1-N> and type: none|null|nat|natnetwork|bridged|intnet|hostonly|generic

VBoxManage modifyvm $MACHINENAME --nic1 nat

# Creating a virtual hard disk. --size parameter is in megabytes.

# --variant Standard dynamically expanding disk.

VBoxManage createmedium disk --filename $(xdg-user-dir DESKTOP)/$MACHINENAME/$MACHINENAME_DISK.vdi --size 25000 --format VDI --variant Standard

# Adding a controller for storage devices.

VBoxManage storagectl $MACHINENAME --name "SATA Controller" --add sata --controller IntelAhci

# Attaching a hard drive

VBoxManage storageattach $MACHINENAME --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium $(xdg-user-dir DESKTOP)/$MACHINENAME/$MACHINENAME_DISK.vdi

# Attaching a CD/DVD

VBoxManage storageattach $MACHINENAME --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium $(xdg-user-dir DESKTOP)/$ISO_NAME

# Setting boot order

VBoxManage modifyvm $MACHINENAME --boot1 dvd --boot2 disk --boot3 none --boot4 none

# Starting the virtual machine

VBoxManage startvm $MACHINENAME