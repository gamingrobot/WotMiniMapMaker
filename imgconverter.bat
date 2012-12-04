SET APP=mogrify.exe
SET OPTS=-format png
SET OPTS2=-resize 500x500
REM mogrify Usage:
REM mogrify -format png *.dds

CD mapsRaw
for /r . %%D in (.) do "%APP%" %OPTS% "%%~fD\*.dds"
for /r . %%D in (.) do "%APP%" %OPTS2% "%%~fD\*.png"

PAUSE