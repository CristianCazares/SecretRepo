dataHour = 0
timezoneOffset = -6

def fixTime():
    global timezoneOffset
    timezoneOffset = -6
    if(dataHour < abs(timezoneOffset)):
            timezoneOffset += 24
    

for i in range(0, 25):
    dataHour = i
    fixTime()
    newHour = dataHour + timezoneOffset
    print("Hour: ", dataHour, "->", newHour)