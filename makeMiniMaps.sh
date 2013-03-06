#!/bin/bash

# WoT installation directory, may contain spaces
WOT="/path/to/World of Tanks/"

# remove old files
rm -rf ./mapsRaw/*
rm -rf ./arena_defs/*
rm -rf ./arena_defs_decoded/*
rm -rf ./gridding/in/*
rm -rf ./gridding/out/*

./copyRawMaps.sh "$WOT"

./imgconverter.sh

cp -v "$WOT"res/scripts/arena_defs/* ./arena_defs/
rm -vrf ./arena_defs/_common_.xml
rm -vrf ./arena_defs/_default_.xml
rm -vrf ./arena_defs/_list_.xml
rm -vrf ./arena_defs/00_tank_tutorial.xml

python ./fixdefnames.py

mono xmlconverter.exe arena_defs/ arena_defs_decoded/

python ./makemaps.py

python ./gridding/gridder.py

./compressMaps.sh
