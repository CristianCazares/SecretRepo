import os
import random
import datetime


date = datetime.datetime.now()
print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)

def commit():
    os.system("clear")
    os.system("git add .")
    os.system("git commit -m '[ENHANCEMENT] Secret commit'")
    os.system("git push origin main")
def gitConfig():
    os.system('git config --global user.email "cm_cjavier@hotmail.com"')
    os.system('git config --global user.name "CristianCazares"')

gitConfig()
commit()