#!/bin/bash

for file in ./jpg/*
do
	BN=`basename "${file}" .jpg`

	# destroy all but map id and game mode from file name
	IDMODE=`echo $BN | sed -r 's/_.*_/_/'`

	ID=(`echo $IDMODE | cut -d "_" -f 1`)
	MODE=(`echo $IDMODE | cut -d "_" -f 2`)

	case "$ID" in
	"01") NAME="karelia"; ;;
	"02") NAME="malinovka"; ;;
	"03") NAME="province"; ;;
	"04") NAME="himmelsdorf"; ;;
	"05") NAME="prokhorovka"; ;;
	"06") NAME="ensk"; ;;
	"07") NAME="lakeville"; ;;
	"08") NAME="ruinberg"; ;;
	"10") NAME="mines"; ;;
	"11") NAME="murovanka"; ;;
	"13") NAME="erlenberg"; ;;
	"14") NAME="siegfried_line"; ;;
	"15") NAME="komarin"; ;;
	"17") NAME="widepark"; ;;
	"18") NAME="cliff"; ;;
	"19") NAME="abbey"; ;;
	"22") NAME="swamp"; ;;
	"23") NAME="westfield"; ;;
	"28") NAME="sand_river"; ;;
	"29") NAME="el_halluf"; ;;
	"31") NAME="airfield"; ;;
	"33") NAME="fjords"; ;;
	"34") NAME="redshire"; ;;
	"35") NAME="steppes"; ;;
	"36") NAME="fishermans_bay"; ;;
	"37") NAME="mountain_pass"; ;;
	"38") NAME="arctic_region"; ;;
	"39") NAME="south_coast"; ;;
	"42") NAME="port"; ;;
	"43") NAME="northwest"; ;;
	"44") NAME="live_oaks"; ;;
	"45") NAME="highway"; ;;
	"47") NAME="serene_coast"; ;;
	"51") NAME="dragon_ridge"; ;;
	"60") NAME="pearl_river"; ;;
	"63") NAME="tundra"; ;;
	"73") NAME="sacred_valley"; ;;
	"85") NAME="severogorsk"; ;;
	*)
		echo "WARNING: Unknown map ID" $ID
		continue;
	;;
	esac

	case "$MODE" in
	"ctf") MODE=""; ;;
	"dom") MODE="_encounter"; ;;
	"ass") MODE="_assault"; ;;
	esac

	mv -v "$file" "./jpg/$NAME$MODE.jpg"

done
