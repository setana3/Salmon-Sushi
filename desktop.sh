#!/bin/bash

echo "Give a name to your desktop file! :"

read userInput 

filepath=/home/$USER/Desktop/$userInput.desktop

if [ -e $filepath ]; then
    echo"Can't creat that file, already exists"

else
    cat > $filename <<EOF
[Desktop Entry]
Version=1.0
Terminal=false
Name="Fill in"
Comment="Fill in"
Exec=/opt/"Fill in"
Type=Application
Categories=Utility;Application;
Icon="Fill in"
EOF

fi
