import urllib.request
import requests
import time

currentVersion = "0.0.1"
request_url = urllib.request.urlopen('https://raw.githubusercontent.com/tanva2009/xAJ7oj6xrURYLSpViCfCi8VM6JSHzpOWzFUYRBZ09euucTMDZA/main/Version.html') 
encoding = 'utf-8'
NewVersion = request_url.read().decode(encoding)
if (NewVersion == currentVersion):
    print("App is up to date!")
else:
    newVersion = requests.get("https://raw.githubusercontent.com/tanva2009/xAJ7oj6xrURYLSpViCfCi8VM6JSHzpOWzFUYRBZ09euucTMDZA/main/main.py")
    open("TAutoUpdate.py", "wb").write(newVersion.content)
    print("New version downloaded, restarting in 5 seconds!")
    time.sleep(5)
    quit()
