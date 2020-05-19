# Automated PXE ubuntu-mate

In premise that you're using Ubuntu OS 

To disasseble ISO run the command
```
engrampa -e $(xdg-user-dir DESKTOP)/Workstation_ISO $(xdg-user-dir DOWNLOAD)/ISO/ubuntu-mate-18.04.4-desktop-amd64.iso
```

If you're not using Ubuntu OS. Use p7zip

```
p7zip x -o extracted_image $(xdg-user-dir DOWNLOAD)/ISO/ubuntu-mate-18.04.4-desktop-amd64.iso
```

Change isolinu/cfg.txt, pressed/autoinstall.seed to change boot process and installation process respectively.

