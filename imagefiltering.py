import zipfile
import re

ziplocation = "/content/gtFine_trainvaltest.zip"
outziplocation = "/content/output.zip"
stringincommon = "color"

with zipfile.ZipFile(outziplocation, "w") as outfil:
    with zipfile.ZipFile(ziplocation, "r") as fil:
        for file in fil.namelist():
            if file.endswith(".png") and stringincommon in file:
                outziplocation.write(fil.extract(file), file)  
                if len(outfil.namelist()) >= 100:
                    break
