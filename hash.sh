#!/bin/bash
mode=${1?Error: no mode given}
output=${2?Error: no output given}
cap=${3?Error: no cap given}
wordlist=${4?Error: no wordlist given}
hashcat -m $mode -o output/$output cap2hccapx/$cap wordlist/$wordlist --potfile-disable --status