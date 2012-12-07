#!/bin/bash

APP=mogrify
OPTS="-format png"
OPTS2="-resize 500x500"

for file in mapsRaw/*/*
do
	if [ ${file##*.} =  "dds" ]
	then
		echo "converting ${file}"
		$APP $OPTS ${file%.*}.dds
		$APP $OPTS2 ${file%.*}.png
	fi
done

