import urllib.request
import requests
import time

currentVersion = "0.0.2"
request_url = urllib.request.urlopen('https://raw.githubusercontent.com/tanva2009/xAJ7oj6xrURYLSpViCfCi8VM6JSHzpOWzFUYRBZ09euucTMDZA/main/Version.html?token=GHSAT0AAAAAACQZZ6JD7OOY6UVEXMQEELECZRH7R7Q') 
if (request_url.read() == currentVersion):
    print("App is up to date!")
else:
    newVersion = requests.get("https://raw.githubusercontent.com/tanva2009/xAJ7oj6xrURYLSpViCfCi8VM6JSHzpOWzFUYRBZ09euucTMDZA/main/main.py?token=GHSAT0AAAAAACQZZ6JCSKPNLQEDKAPDZXPMZRH7SIA")
    open("TAutoUpdate.py", "wb").write(newVersion.content)
    print("New version downloaded, restarting in 5 seconds!")
    time.sleep(5)
    quit()
