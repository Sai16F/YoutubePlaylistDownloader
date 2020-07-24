import os

containerFolder = input("Set a name to the Container Folder (Required!.. DO NOT LEAVE IT EMPTY!!): ")
if (containerFolder == ''):
  os.system('cmd /c "exit"')
else:
  PlaylistLink = input("Past youtube playlist link to download: ")
  os.system('cmd /k "youtube-dl -o \"./' + containerFolder + '/%(playlist)s/%(playlist_index)s %(title)s.%(ext)s\"" -i ' + PlaylistLink)

# Coded By Saif Al-Tahawy <3
# this file was compiled to .exe file using pyinstaller