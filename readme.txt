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
- SWFExtract (part of SWFTools, http://www.swftools.org/)

Linux:
- Additional requirements:
  - unzip
  - mono
- Permissions to execute:
  - makeMiniMaps.sh
  - imgconverter.sh
  - copyRawMaps.sh

First run:
- remove FolderHolder.txt files
- extract icons from res/packages/gui.pkg/gui/flash/Minimap.swf with SWFExtract into icon/
  - you need at least base flags and starting points, IDs ~280-350, rename those to:
    - green.png
    - gs1.png
    - gs2.png
    - gs3.png
    - red.png
    - rs1.png
    - rs2.png
    - rs3.png
    - blank.png
- set WoT installation path in makeMiniMaps.sh
- execute makeMiniMaps.sh
