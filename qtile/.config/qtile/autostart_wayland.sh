#!/bin/sh

nm-applet &
udiskie -A -t &
greenclip daemon &
/usr/bin/lxqt-policykit-agent &

systemctl --user import-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=$XDG_CURRENT_DESKTOP


