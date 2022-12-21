import subprocess
import sqlite3
from datetime import datetime, timedelta
import calendar
import IPython
from time import sleep

#constants
MODE_OFFSET = 3 #new songs enter the shuffle count at a deficit relative to mode so that they play more frequently at first


#functions
#not in use yet but soon 2022-12-11
def now_play(song,song_count,song_file,song_seconds):
    
        print("Now playing:\t\t{}\t\tShuffle_count: {}".format(song,song_count))
        IPython.display.display(IPython.display.Audio(song_file,autoplay=True, embed=None))
        shuffle_count_increment(song,song_count)
        sleep(song_seconds)
                        
#use this to determine if we are in DST
def is_dst ():
    """Determine whether or not Daylight Savings Time (DST)
    is currently in effect"""
    
    import pytz
    x = datetime(datetime.now().year, 1, 1, 0, 0, 0, tzinfo=pytz.timezone('US/Eastern')) # Jan 1 of this year
    y = datetime.now(pytz.timezone('US/Eastern'))

    # if DST is in effect, their offsets will be different
    return not (y.utcoffset() == x.utcoffset())
        
def get_now():
    """Determine local time as opposed to server time"""
    
    if is_dst():
        offset_hours = 5
    else:
        offset_hours = 4
        
    return datetime.now() - timedelta(hours=offset_hours)
    
def create_music_list(path_music):
    """the big shuffle song list"""
    
    import glob
    music_source="*.mp3"
    return glob.glob(path_music + music_source)

#add song with a count of the mode minus MODE_OFFSET (currently 3)
#this makes it so that newly added songs are played often before becoming normalized in shuffle
def shuffle_count_insert(sng_name, mode, song_seconds):
    
    from datetime import timedelta
    con = sqlite3.connect('soundtrak.db')
    table = "shuffle_count"      
    count = mode - MODE_OFFSET
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    statement = 'INSERT INTO {} (name,count,time,duration_sec) \
    VALUES ("{}",{},"{}","{}")'.format(table,sng_name,count,dt,song_seconds)
    con.execute(statement)
    con.commit()  
    con.close()
    
    return statement

def sort_shuffle_count(music_list, path_music):
    
    from operator import itemgetter
    #import sqlite3
    con = sqlite3.connect('soundtrak.db')
    table = "shuffle_count"
    music_list_sorted=[]
    for sng_name in music_list:
        #print(sng_name)
        sng_name = sng_name.replace(path_music,"")
        statement = 'SELECT count,duration_sec FROM {} WHERE name="{}" LIMIT 0,1'.format(table,sng_name)
        cursor = con.execute(statement)
        rows = cursor.fetchall()       
        if rows:
            #print("{} in db...".format(name))
            count,duration = rows[0][0],rows[0][1]
            music_list_sorted.append([sng_name,count,int(duration)])            
        else:
            #song_name = sng_name
            print("{} NOT in db...".format(sng_name))
            mode = sc_mode()
            print(f"Mode from db: {mode}")
            song_seconds = song_duration(path_music+sng_name)
            shuffle_count_insert(sng_name, mode[0], song_seconds)
            music_list_sorted.append([sng_name,mode[0] - MODE_OFFSET,int(song_seconds)])        
    con.close()
            
        
        
    return sorted(music_list_sorted,key=itemgetter(1))


def shuffle_count_increment(song_name,song_count):
    
    con = sqlite3.connect('soundtrak.db')
    table = "shuffle_count"
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    statement = 'UPDATE {} SET count={},time="{}" WHERE name="{}"'.format(table,song_count + 1,dt,song_name)
    con.execute(statement)
    con.commit()  
    con.close()
    
    return statement


def next_song_info(cal_code, now):
    
        #import sqlite3
        con = sqlite3.connect('soundtrak.db')
        table='song_schedule'
        current_time=now.strftime('%H:%M:%S')
        statement="SELECT * FROM {} WHERE dow='{}' AND time >'{}' ORDER BY dow ASC, time ASC LIMIT 0,1"\
            .format(table,cal_code,current_time)
        #print(statement)
        cursor=con.execute(statement)
        rows = cursor.fetchall()
        #print(rows)
        #todo change to try-except 20220512
        if rows:
            for row in rows:
                ns_time = datetime.strptime(row[1],'%H:%M:%S').time()
                ns_name = row[2]
        else:
            ns_time = datetime.strptime(current_time,'%H:%M:%S').time()
            ns_name = "Unknown"
        con.close()   
            
        return ns_time, ns_name

def week_of_month(year, month, DOM):
    """for use creating calendar code for multiple weeks of scheudling"""
    
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    monthcal = c.monthdayscalendar(year,month)
    #print(DOM)
    i = 1
    for week in monthcal:
        #print(week)
        for dow in week:
            #print(dow)
            if dow == DOM:
                return i
        i = i+1


def sc_mode():
    """used adding new songs to the shuffle db table and making them near the mode of play counts"""

    con = sqlite3.connect('soundtrak.db')
    table='shuffle_count'
    statement ='SELECT count, COUNT(name) shuffle_cnt FROM {} GROUP BY count ORDER BY shuffle_cnt ASC'.format(table)
    cursor=con.execute(statement)
    rows = cursor.fetchall()
    for row in rows:
        #mode=row[0]
        mode = row
    con.close()
    
    return mode

#get the song duration in seconds using *NIX ffprobe
def song_duration(file):
    
    args = ("ffprobe","-show_entries", "format=duration","-i", file)
    popen = subprocess.Popen(args, stdout = subprocess.PIPE)
    output1 = str(popen.stdout.read())
    a = output1.split('=')
    b = a[1].split(".")
    
    return int(b[0])

#extract the song(file) name from the path for various uses
def song_name(file):
    
    a = file.split('/')
    
    return a[-1]
