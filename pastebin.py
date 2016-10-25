
import urllib
import urllib2
import json

API_DEV_KEY = "00000000"
API_USER_KEY = "00000000"
API_PASTE_PUBLIC = 0
API_PASTE_UNLISTED = 1
API_PASTE_PRIVATE = 2

class paste(object):
    pass

def create_paste(text, dev_key = API_DEV_KEY, paste_privacy = None,
                 user_key = None, name = None, format = None,
                 expire_date = None):

    req = urllib2.Request("http://pastebin.com/api/api_post.php")
    data = {"api_option": "paste",
            "api_dev_key": dev_key,
            "api_paste_code": text}

    if paste_privacy:
        data["api_paste_private"] = paste_privacy
    if user_key:
        data["api_user_key"] = user_key
    if name:
        data["api_paste_name"] = name
    if format:
        data["api_paste_format"] = format
    if expire_date:
        data["api_paste_expire_date"] = expire_date

    req.add_data(urllib.urlencode(data))
    response = urllib2.urlopen(req)

    return response.read()

def get_user_key(username, password, dev_key = API_DEV_KEY):
    # WARNING: THIS IS WILL SEND PASSWORDS UNENCRYPTED

    req = urllib2.Request("http://pastebin.com/api/api_login.php")
    data = {"api_dev_key": dev_key,
            "api_user_name": username,
            "api_user_password": password}

    req.add_data(urllib.urlencode(data))
    response = urllib2.urlopen(req)

    return reponse.read()

def get_user_posts(user_key, dev_key = API_DEV_KEY, results_limit = None):
    
    req = urllib2.Request("http://pastebin.com/api/api_post.php")
    data = {"api_option": "list",
            "api_dev_key": dev_key,
            "api_user_key": user_key}

    if results_limit:
        data["api_results_limit"] = results_limit

    req.add_data(urllib.urlencode(data))
    response = urllib2.urlopen(req)

    return response.read()

