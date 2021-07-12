from fontTools.ttLib import TTFont
from pathlib import Path
import glob

for count, filename in enumerate(glob.glob('input/**/*.*', recursive=True), start=1):
    font = TTFont(filename)
    font.flavor = 'woff2'
    font.save('output/' + Path(filename).stem + '.woff2')
    print(count, filename)
