#!/bin/sh

set -o nounset

NEXTLINE=0
FIND=""
for I in `file /boot/vmlinuz*`; do
  if [ ${NEXTLINE} -eq 1 ]; then
    FIND="${I}"
    NEXTLINE=0
   else
    if [ "${I}" = "version" ]; then NEXTLINE=1; fi
  fi
done
if [ ! "${FIND}" = "" ]; then
  CURRENT_KERNEL=`uname -r`
  if [ ! "${CURRENT_KERNEL}" = "${FIND}" ]; then
    echo "REBOOT"
  fi
fi
