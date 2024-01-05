#!/bin/sh
unclutter --root &
dunst &
nitrogen --restore
picom --config ~/.config/picom/picom.conf &
nm-applet &
udiskie -A -t &
#clipmenud &
greenclip daemon &
/usr/bin/lxqt-policykit-agent &
#/usr/bin/emacs --daemon
