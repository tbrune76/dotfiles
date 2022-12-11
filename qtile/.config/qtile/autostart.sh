#!/bin/sh
unclutter --root &
udiskie -A -t &
clipmenud &
/usr/bin/lxqt-policykit-agent &
/usr/bin/emacs --daemon
