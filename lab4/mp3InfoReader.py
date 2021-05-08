import os
import struct
import argparse

path = os.getcwd() +'\\mp3Dir'
parser = argparse.ArgumentParser()
parser.add_argument('-d', type = bool, default = False)
args = parser.parse_args()

class mp3InfoReader():
    
    def __init__(self):
        music_list=[]
        count = 0
        files = os.listdir(path)
        for file in files:
            with open(path +'\\' + file, 'rb') as file:
                track = Track()
                file.seek(-128, 2)
                track.track_tag,track.track_name,track.track_artist,track.track_album,track.track_year,track.track_comment,track.track_genre = struct.unpack("!3s30s30s30s4s30sb", file.read())
                music_list.append(track)
        for i in range(len(music_list)):
            print(music_list[i])
class Track():
    
    def __init__(self):
        self.track_tag=''
        self.track_name=''
        self.track_artist=''
        self.track_album=''
        self.track_year=''
        self.track_comment=''
        self.track_genre=''
    
    def __str__(self):
        return "%s - %s - %s - %s - %s - %s - %s" % (self.track_tag , self.track_name , self.track_artist , self.track_album , self.track_year , self.track_comment,self.track_genre)
    