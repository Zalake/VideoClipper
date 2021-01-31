# import re
import os
import os.path
import sys
filepath = './vol.txt'
durationFilePath = "./startEnd.txt"
vidFileName = ""+sys.argv[1]
if(os.path.exists(durationFilePath)):
    os.remove(durationFilePath)
if(os.path.exists("./temp.txt")):
    os.remove("./temp.txt")
f = open(durationFilePath, "a")
f.write("00:00:00")
f.write("\n")
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
        timeString=""
        indexStart = line.find("silence_start")
        endIndex = line.find("silence_end")
        if(indexStart!=-1):
            newLineIndex = line.find("\n")
            indexStart+=15
            time = int(float(line[indexStart:newLineIndex-1]))
            time+=1
            temp = str(int(time/3600));
            timeString+=("0"+temp+":") if(len(temp)==1) else (temp+":")
            time = time%3600;
            temp2 = str(int(time/60));
            timeString+=("0"+temp2+":") if(len(temp2)==1) else (temp2+":")
            time=str(time%60)
            timeString+=("0"+time) if(len(time)==1) else (time)
            f.write(timeString)
            f.write("\n")
        if(endIndex!=-1):
            pipeIndex = line.find("|")
            endIndex+=13
            time = int(float(line[endIndex:pipeIndex-2]))
            temp = str(int(time/3600));
            timeString+=("0"+temp+":") if(len(temp)==1) else (temp+":")
            time = time%3600;
            temp2 = str(int(time/60));
            timeString+=("0"+temp2+":") if(len(temp2)==1) else (temp2+":")
            time=str(time%60)
            timeString+=("0"+time) if(len(time)==1) else (time)
            f.write(timeString)
            f.write("\n")
        line = fp.readline()
import subprocess

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)
tempString = ""
time = int(get_length(vidFileName))
temp = str(int(time/3600));
timeString+=("0"+temp+":") if(len(temp)==1) else (temp+":")
time = time%3600;
temp2 = str(int(time/60));
timeString+=("0"+temp2+":") if(len(temp2)==1) else (temp2+":")
time=str(time%60)
timeString+=("0"+time) if(len(time)==1) else (time)
f.write(timeString)
f.write("\n")
f.write("end")
f.close()
fp.close()

tmp = open("./temp.txt","a")
tmp.close()



