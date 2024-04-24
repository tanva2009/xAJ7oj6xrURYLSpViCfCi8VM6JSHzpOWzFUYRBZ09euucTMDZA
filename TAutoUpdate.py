import urllib.request
import requests
import requests # dependency
import platform
import os
import pyttsx3

ts = pyttsx3.init()
ts.say("update main work")
ts.runAndWait()
currentVersion = "0.0.2"
request_url = urllib.request.urlopen('https://raw.githubusercontent.com/tanva2009/xAJ7oj6xrURYLSpViCfCi8VM6JSHzpOWzFUYRBZ09euucTMDZA/main/Version.html') 
NewVersion = request_url.read().decode('utf-8').strip()
if (NewVersion == currentVersion):
    print("App is up to date!")
else:
    newVersion = requests.get("https://raw.githubusercontent.com/tanva2009/xAJ7oj6xrURYLSpViCfCi8VM6JSHzpOWzFUYRBZ09euucTMDZA/main/main.exe")
    open(__file__, "wb").write(newVersion.content)
    os.startfile(__file__)
    try:
        quit()
    except:
        ts.say("error in quit")
        ts.runAndWait()