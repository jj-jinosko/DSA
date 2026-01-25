userTime = "07:05:45PM"

# def timeConversion(userTime):
    
# no built-ins
def timeConversion(userTime):
    twelveHours = int(userTime[:2])
    if twelveHours >= 12:
        militaryHours = twelveHours - 12
    else: 
        militaryHours = twelveHours + 12
    result = str(militaryHours) + userTime[2:-2]
    print(result)

timeConversion(userTime)


