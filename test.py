
import pastebin
import json
import webbrowser

# CHECK http://pastebin.com/api FOR DOCUMENTATION ON THE API

with open("credentials.json", "r") as creds:
    user_info = json.loads(creds.read())

pastebin.API_DEV_KEY = user_info["dev_key"]

result = pastebin.create_paste(
    "print 'This is a test paste for pastebin.create_paste'",
    paste_privacy = API_PASTE_UNLISTED,
    name = "API Test Paste",
    format = "python",
    expire_date = "10M")

print result
webbrowser.open(result)