import requests
import json
import sys

username = "LeRockeur43"
password = "acdcacdc"
token = ""
domain = "http://api.t411.li"
header = {}

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def login():
    global token
    global header
    r = requests.post(domain + "/auth", data={'username': username, 'password': password})
    token = r.json()["token"]
    header = {"Authorization" : token}

def askRequest():
    req = {}

    print("What is your keyword ?")
    sys.stdout.write("$>")
    sys.stdout.flush()
    req["keyword"] = sys.stdin.readline();
    return req

def printTorrents(json):
    template = "| {0:8} | {1:125} | {2:10} | {3:10} | {4:10} | {5:10} Go | {6:20} |"
    print(json["torrents"][0])
    print(color.WARNING + template.format("UID", "NAME", "COMPLETED", "SEEDERS", "LEECHERS", "SIZE", "ADDED") + color.ENDC)
    for item in json["torrents"]:
        print(template.format(item['id'], item['name'], item["times_completed"], item['seeders'], item['leechers'], round(float(item["size"])/1073741824, 2), item["added"] ) )

def getOnlyRes(json, res):
    retval = json.copy()
    del retval["torrents"]
    retval["torrents"] = []
    for item in json["torrents"]:
        if res in item["name"]:
            retval["torrents"].append(item)
    return retval

def main():
    login()
    req = askRequest()
    r = requests.get(domain + "/torrents/search/" + req["keyword"]+ "?limit=15", headers=header).json()
    print(r)
    r2 = getOnlyRes(r, "720")
    printTorrents(r2)

main()