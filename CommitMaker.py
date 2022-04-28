import os
import random
import datetime
import time


dateData = datetime.datetime.now()
date = ""
hour = ""
def getDateData():
    global date, hour
    dateData = datetime.datetime.now()
    date = str(dateData.day) + "-" + str(dateData.month).zfill(2) + "-" + str(dateData.year)
    fixedTimezone = -6
    if(dateData.hour < abs(fixedTimezone)):
        fixedTimezone += 24
    
    hour = str(dateData.hour + fixedTimezone).zfill(2) + ":" + str(dateData.minute).zfill(2) + ":" + str(dateData.second).zfill(2)

def editFile(numberOfCommits):
    getDateData()
    file = open('file.txt', 'a')
    file.write(date + " " + hour + "\n")
    file.close()
    for i in range(0, numberOfCommits):
        file = open('file.txt', 'a')
        
        file.write(str(i + 1) + "/" + str(numberOfCommits) + "\n")
        file.close()
        gitConfig()
        commit()
        time.sleep(1)

def gitConfig():
    os.system('git config --global user.email "cm_cjavier@hotmail.com"')
    os.system('git config --global user.name "CristianCazares"')
    
def commit():
    os.system("clear")
    os.system("git add .")
    os.system("git commit -m '[ENHANCEMENT] Secret commit'")
    os.system("git push origin main")
    
def determinateCommits():
    #Determinate if is weekday or weekend
    weekday = False
    if(dateData.weekday() >= 0 and dateData.weekday() < 5):
        weekday = True

    #On weekend, only 75% chance of commit and it would only be low and mid
    if(weekday == False):
        commitType = random.randint(1, 100)
        if(commitType <= 75):
            commitType = "low"
        else:
            commitType = "mid"
    else:        
        #On weekday, three types of commit, low, mid and high.
        commitType = random.randint(1, 100)
        if(commitType <= 40):
            commitType = "low"
        elif(commitType > 40 and commitType <= 90):
            commitType = "mid"
        elif(commitType > 90):
            commitType = "high"

    numberOfCommits = 0
    #Make commits
    if(commitType == "low"):
        numberOfCommits = random.randint(1,3)
    elif(commitType == "mid"):
        numberOfCommits = random.randint(3,7)
    elif(commitType == "high"):
        numberOfCommits = random.randint(8,15)

    editFile(numberOfCommits)
        

def main():
    os.system("clear")
    determinateCommits()

