import sqlite3 
from datetime import datetime

def db_name():
    #db_name='soundtrack.db'
    db_name='soundtrack-gn.db'
    return db_name

def getMediaDuration(file):
    
    import subprocess
    args=("ffprobe","-show_entries", "format=duration","-i",file)
    popen = subprocess.Popen(args, stdout = subprocess.PIPE)
    output2=str(popen.stdout.read())
    a,b=output2.split('=')
    b = b[:6]
    return b

def getMediaName(file):
    
    a=file.split('/')
    end=len(a)
    a = a[end-1]
    return a

def getShuffleCountMode():
    
    con = sqlite3.connect(db_name())
    table='shuffle_count'
    statement ='SELECT cnt,COUNT(name) shuffle_cnt FROM {} GROUP BY cnt ORDER BY shuffle_cnt ASC'.format(table)
    cursor=con.execute(statement)
    rows = cursor.fetchall()
    for row in rows:
        mode=row[0]
    con.close()
    return mode

def incrementShuffleCount(statement,song):
    
    con = sqlite3.connect(db_name())
    table='shuffle_count'
    statement=getShuffleCountExists(song[0])
    print(statement)
    con.execute(statement)
    con.commit()
    con.close()
    

#check if the song exists in the db table shuffle_count already
def getShuffleCountExists(name):
    
    con = sqlite3.connect(db_name())
    table='shuffle_count'
    statement ='SELECT cnt FROM {} WHERE name="{}" LIMIT 0,1'.format(table,name)
    cursor=con.execute(statement)
    rows = cursor.fetchall()
    dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if rows:
        cnt=rows[0][0]+1
        statement='UPDATE {} SET cnt={},time="{}" WHERE name="{}"'.format(table,cnt,dt,name)
    else:      
        mode=getShuffleCountMode()
        cnt=mode-4
        data = []
        statement ='INSERT INTO {} (name,cnt,time) VALUES ("{}",{},"{}")'.format(table,name,cnt,dt)
    con.close()
    return statement

#implement this function below when you get a chance 20190316
def getNextSTDifference(current_dow,current_time):

    table='song_schedule'
    statement="SELECT * FROM {} WHERE dow='{}' AND time>'{}' ORDER BY dow ASC, time ASC LIMIT 0,1".format(table,current_dow,current_time)
    cursor=con.execute(statement)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        next_song_time=datetime.strptime(row[1],'%H:%M:%S').time()
    song_dt = dt.datetime.combine(dt.date.today(), next_song_time)
    now=dt.datetime.now()
    difference=song_dt-now
    difference=difference.seconds
    con.close()
    return difference