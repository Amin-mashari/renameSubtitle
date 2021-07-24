"""
author: Amin_mashari
DATE: 1400 / 05 / 02
this code rename subtitles and set same name of the movie for them

"""
import os 
import re

dir = "./" # current directory
codename = "renameSubtitle.py"

#dir = input("please inter folder directory:")

movies = []
subtitles = []

subtitleType = "srt"

def save(value):
    find = re.findall( subtitleType +"$" , value )
    # find = true : so we find a srt 
    # otherwise we found a mkv
    if find :
        subtitles.append(value)
    else :
        movies.append(value)


# search files in dir
for root, dirs, files in os.walk(dir):
    # search in files
    for filename in files:
        if filename != codename:
            #print (filename)
            # save mkv and srt files in list
            save(filename)


#movies.sort()
#subtitles.sort()

subIndex = 0
for name in movies:
    # name : movieName.mkv
    dst = os.path.splitext(name)[0] # split movie name from is type
    # dst : moviename
    if subIndex >= len(subtitles):
        break
    preName = subtitles[subIndex]
    newName = dst +"." + subtitleType # dst.srt

    os.rename(preName , newName)
    subIndex += 1
    
    

