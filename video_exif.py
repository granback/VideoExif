#!/usr/bin/python

import ffmpeg
import sys
from pprint import pprint, pformat
import os
from pathlib import Path
import filetype

NoneTypeList = []
VideoCounter = 0
NoneTypeCounter = 0


WorkDir = str(Path(sys.argv[1]))

for file in os.listdir(WorkDir):
    FilePath = WorkDir + '/' + file
    Typ = filetype.guess(FilePath)
    
    if Typ is None:
        NoneTypeList.append(FilePath)
        #print('Could not determine file type: ', FilePath)
        NoneTypeCounter +=1
        continue
    else:
        mime = Typ.mime
    if mime and mime.startswith("video"):

        TxtName = os.path.splitext(file)[0] + '.txt'
        with open(os.path.join(WorkDir, TxtName), 'w') as f:
            f.write(pformat(ffmpeg.probe(FilePath)))
        VideoCounter +=1
    else:
        print('Could not determine filetype: ', FilePath)
    

print('Totalt antal videofiler:',VideoCounter)
if NoneTypeCounter >0:
    print(NoneTypeCounter,'filer kunde inte identifieras:')
    pprint(NoneTypeList)
    
else:
    exit()
    