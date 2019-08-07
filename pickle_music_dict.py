def getMediaDuration(file):
    
    import subprocess
    args=("ffprobe","-show_entries", "format=duration","-i",file)
    popen = subprocess.Popen(args, stdout = subprocess.PIPE)
    output2=str(popen.stdout.read())
    a,b=output2.split('=')
    b = b[:6]
    return b 

def MusicDict(pathMusic,music_source):
    
    import sqlite3
    import operator
    import glob
    import random
    music_list=glob.glob(pathMusic+music_source)
    random.shuffle(music_list)
    dicts = {}
    randomizer=0
    for item in music_list:
        #get song duration
        b=getMediaDuration(item)
        b=round(float(b[:6])) 
        #check db for count of previous plays
        con = sqlite3.connect('/home/pi/.jupyter/soundtrack/soundtrack.db')
        table='shuffle_count'
        statement ='SELECT cnt FROM {} WHERE name="{}" LIMIT 0,1'.format(table,item)
        #print(statement)
        cursor=con.execute(statement)
        rows = cursor.fetchall()
        if rows:
            cnt=rows[0][0]
        else:
            cnt=0
        #create list of count, randomizer based on position in glob list, and song duration in seconds    
        dicts[item]=cnt,randomizer,b    
        randomizer=randomizer+1 

    music_dicts = sorted(dicts.items(), key=operator.itemgetter(1))
    
    return music_dicts
    

pathMusic="/home/pi/Music/"
music_source="*.mp3"
music_dicts=MusicDict(pathMusic,music_source)
print(music_dicts)
import pickle
filename='/home/pi/.jupyter/soundtrack/music_dict.p'
pickle.dump(music_dicts,open(filename,'wb'))       