#!/bin/bash

if [ $# -lt 1 ]; then
	echo "ERROR: $0 requires full path to WoT installation directory as a first parameter"
elif [ $# -ge 1 ]; then
	for file in "$1"res/packages/[0-9][0-9]_*.pkg
	do
		BN=`basename "${file}" .pkg`
		unzip -j "${file}" spaces/* -x *.chunk *.cdata -d mapsRaw/${BN}
	done

	while [ $# -gt 1 ]; do
		shift
		echo "WARNING: $0 discarded argument:" $1
	done
fi
