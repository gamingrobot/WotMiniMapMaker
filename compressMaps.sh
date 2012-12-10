#!/bin/bash

rm -rf ./jpg/*

APP=mogrify
OPTS="-format jpg"
OPTS2="-quality 85" # default 92

for file in ./gridding/out/*
do
	$APP $OPTS ${file}
	$APP $OPTS2 ${file%.*}.jpg
	mv -v ${file%.*}.jpg ./jpg/
done