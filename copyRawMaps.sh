#!/bin/bash

# full path to WoT installation directory
for file in /path/to/WoT/res/packages/[0-9][0-9]_*.pkg
do
	BN=`basename "${file}" .pkg`
	unzip -j "${file}" spaces/* -x *.chunk *.cdata -d mapsRaw/${BN}
done