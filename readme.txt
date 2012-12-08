unpack all packages and put the maps into mapsRaw
remove all .chunk .cdata files via del /S *.chunk from the mapsRaw directory
run imgconverter.bat to convert all dds to png
then copy all arena_defs from res/scripts/arena_defs
run fixdefnames.py to fix the arena_defs names
run usexmlconverter.bat to convert all xml to readable
run makemaps.py
copy all maps to gridding in
run gridding.py
move all out to mapsFinal

Requirements:
- Python 2.x
- Python libraries: beautifulsoup4, lxml, PIL
- mogrify (from ImageMagick)

Linux:
- Additional requirements:
  - unzip
  - mono
- Permissions to execute:
  - imgconverter.sh
  - copyRawMaps.sh