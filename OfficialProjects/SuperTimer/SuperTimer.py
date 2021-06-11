import time, subprocess, sys, os, urllib.request
try:
    import datetime
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'datetime'])
    import datetime
try:
    from playsound import playsound
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'playsound'])
    from playsound import playsound

if not os.path.isfile('alarm.mp3'):
    urllib.request.urlretrieve("https://github.com/BarsTiger/KOTIKOTapps_download_repo/blob/master/OfficialProjects/SuperTimer/alarm.mp3?raw=true", 'alarm.mp3')

print("You can change alarm sound: just reneame your sound to alarm.mp3 and copy it to SuperTimer folder (to get original just delete your file)")
superSecond = float(input("Print how many real seconds will be in superSecond: "))
timeInSuperSeconds = int(input("Timer in superSeconds: "))

os.system('cls' if os.name == 'nt' else 'clear')

formattedTimeInSuperSeconds = str(datetime.timedelta(seconds=timeInSuperSeconds))

width = str(len(str(formattedTimeInSuperSeconds)))
while timeInSuperSeconds > 0:
    formattedTimeInSuperSeconds = str(datetime.timedelta(seconds=timeInSuperSeconds))
    print('Time remaining: {{:{:}}}'.format(width).format(formattedTimeInSuperSeconds), end='\r')
    timeInSuperSeconds -= 1
    time.sleep(superSecond)

print("Press Ctrl + C to stop alarm")
while True:
    playsound("alarm.mp3")
