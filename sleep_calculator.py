"""The hours are in te 24 format"""
hours = range(00, 24)
minutes = range(00, 61)

#Hours input
waking_hour = int(input("What hour would you like to wake up: "))
if waking_hour not in hours:
    print("Error: Hours are between 00 and 24")

#Minutes input
waking_minute = int(input("And what minute: "))
if waking_minute not in minutes:
    print("Error: Minutes are between 00 and 60")


def count():
    global waking_hour
    global waking_minute

#The first bedtime choice
    resulth1 = waking_hour - 10
    if waking_hour - 10 < 0:
        resulth1 = 24 + (waking_hour - 10)

    resultm1 = waking_minute + 45
    if resultm1 > 60:
        resulth1+=1
        resultm1-=60
    #if minutes are equal to 60    
    if resultm1==60:
        resultm1 = "00"
        resulth1+=1
    #in case there is one number in minutes
    if len(str(resultm1)) == 1:
        resultm1="0"+str(resultm1)
    #if hours are equal to 24 or 0
    if resulth1 == 24:
        resulth1 = "00"
    if resulth1 == 0:
        resulth1 = "00"


    print(f"In order to wake up at {waking_hour}:{waking_minute} and have a productive day, you must sleep at one of these times: {resulth1}:{resultm1}", end="" )

#The second bedtime choice
    resulth2 = waking_hour - 8
    if waking_hour - 8 < 0:
        resulth2 = 24 + (waking_hour - 8)

    resultm2 = waking_minute + 15
    if resultm2> 60:
        resulth2+=1
        resultm2 -= 60
    #if minutes are equal to 60
    if resultm2==60:
        resultm2 = "00"
        resulth2+=1
    #in case there is one number in minutes
    if len(str(resultm2)) == 1:
        resultm2="0"+str(resultm2)
    #if hours are equal to 24 or 0
    if resulth2 == 24:
        resulth2 = "00"
    if resulth2 == 0:
        resulth2 = "00"

    print(f", {resulth2}:{resultm2}", end ="")

#The third bedtime choice
    resulth3 = waking_hour - 7
    if waking_hour - 7 < 0:
        resulth3 = 24 + (waking_hour - 7)

    resultm3 = waking_minute + 45
    if resultm3> 60:
        resulth3+=1
        resultm3 -= 60
    #if minutes are equal to 60
    if resultm3==60:
        resultm3 = "00"
        resulth3+=1
    #in case there is one number in minutes
    if len(str(resultm3)) == 1:
        resultm3="0"+str(resultm3)
    #if hours are equal to 24 or 0
    if resulth3 == 24:
        resulth3 = "00"
    if resulth3 == 0:
        resulth3 = "00"

    print(f", {resulth3}:{resultm3}", end =" ")
    

#The fourth bedtime choice
    resulth4 = waking_hour - 5
    if waking_hour - 5 < 0:
        resulth4 = 24 + (waking_hour - 5)

    resultm4 = waking_minute + 15
    if resultm4 > 60:
        resulth4+=1
        resultm4 -= 60
    #if minutes are equal to 60
    if resultm4==60:
        resultm4 = "00"
        resulth4+=1
    #in case there is one number in minutes
    if len(str(resultm4)) == 1:
        resultm4="0"+str(resultm4)
    #if hours are equal to 24 or 0
    if resulth4 == 24:
        resulth4 = "00"
    if resulth4 == 0:
        resulth4 = "00"
    print(f"or {resulth4}:{resultm4}")
    
count()
