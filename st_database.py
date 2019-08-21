import sqlite3

def int_pick(question,cnt):
    global reply
    reply = input(question+' (0-{}): '.format(cnt-1))
    try:
        reply=int(reply)
        if (0 <= reply < cnt):
            return reply
        else:
            return int_pick("Please Re-enter ",cnt)
    except:
        return int_pick("Only Numbers. Please Re-enter ",cnt)

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+" (y/n): ")).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
        else:
            return yes_or_no("Please re-enter ")
        
def print_pick(plist):
    i,maxp=0,len(plist)
    for p in plist:
        if i < maxp-1:
            print("{}->{} ".format(i,p,),end=" ")
        else:
            print("{}->{} ".format(i,p,))
        i=i+1