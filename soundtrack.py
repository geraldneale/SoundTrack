import sqlite3 
from datetime import datetime
con = sqlite3.connect('soundtrack.db')

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
    
    con = sqlite3.connect('soundtrack.db')
    table='shuffle_count'
    statement ='SELECT cnt,COUNT(name) shuffle_cnt FROM {} GROUP BY cnt ORDER BY shuffle_cnt ASC'.format(table)
    cursor=con.execute(statement)
    rows = cursor.fetchall()
    for row in rows:
        mode=row[0]
    con.close()
    return mode

#check if the song exists in the db table shuffle_count already
def getShuffleCountExists(name):
    
    con = sqlite3.connect('soundtrack.db')
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

#create shuffle list (replaces cronjob pickle that does same thing 4x/day 20190819
def getMusicDicts():
    
    import operator
    con = sqlite3.connect('soundtrack.db')
    table='shuffle_count'
    statement ='SELECT * FROM {} ORDER BY cnt ASC'.format(table)
    cursor=con.execute(statement)
    rows = cursor.fetchall()
    i=0
    dicts = {}
    for row in rows:
        file=row[0]
        cnt=row[1]
        duration=row[3]
        dicts[file]=cnt,i,duration
        i=i+1
    con.close()
    music_dicts=sorted(dicts.items(),key=operator.itemgetter(1))
    return music_dicts

def getNearbySchedule(dow,time):
    
    from datetime import datetime, timedelta
    #current_dow=datetime.now().strftime('%w')
    db="soundtrack.db"
    table='song_schedule'
    #current_time=datetime.now().strftime('%H:%M:%S')
    end_tm=datetime.now() + timedelta(0,float(3000))
    end_tm=end_tm.strftime('%H:%M:%S')
    beg_tm=datetime.now() + timedelta(0,float(-3000))
    beg_tm=beg_tm.strftime('%H:%M:%S')
    statement="SELECT * FROM {} WHERE dow={} ORDER BY dow ASC, time ASC".format(table,dow)
    con = sqlite3.connect(db) 
    cursor=con.execute(statement)
    rows = cursor.fetchall()
    con.close()
    i=0
    for row2 in rows:
        if str(beg_tm) < row2[1] < str(end_tm):
            #print a few st songs before and after now
            if ((str(time) < row2[1]) and i==0):
                print("Next: {}: {}".format(row2[1],row2[2]))
                i=i+1
            else:
                print("{}: {}".format(row2[1],row2[2]))

def getDBStatus(): #loop through shuffle songs checking in the DB and if not output to list
    
    import glob
    import sqlite3
    pathMusic,music_source="/home/pi/Music/","*.mp3"
    db,table='soundtrack.db','shuffle_count'
    con=sqlite3.connect(db)
    music_list=glob.glob(pathMusic+music_source)
    new_files=[]
    #print(music_list)
    for file in music_list:
        #print(file)
        statement ='SELECT cnt FROM {} WHERE name="{}" LIMIT 0,1'.format(table,file)
        #print(statement)
        cursor=con.execute(statement)
        row = cursor.fetchall()
        if row:
            pass
        else:
            new_files.append(file)     
    return new_files
    
def addToDB():
    
    table='shuffle_count'
    new_files=getDBStatus()
    mode=getShuffleCountMode()
    for file in new_files:        
        duration=round(float(getMediaDuration(file)))
        print(file,mode-4,duration)
        dtime="00:00:00"
        try:
            statement ="INSERT INTO {} (name,duration_sec,cnt,time) VALUES ('{}','{}',{},'{}')".format(table,file,duration,mode-4,dtime)
            con.execute(statement)
            print("Successfully entered into database.\n{}".format(statement))
        except sqlite3.Error as e:
            print(e)
    con.commit()
    con.close()
    
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

