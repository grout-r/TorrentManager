import requests
import json
import sys
import userRequest
import tempfile
import os

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
    header = {"Authorization": token}

def printTorrents(json):
    template = "{0:4} | {1:8} | {2:125} | {3:10} | {4:10} | {5:10} | {6:10} Go | {7:20} | {8:20}"
    i = 0

    print(json["torrents"][0])
    print(color.WARNING + template.format("NUM", "UID", "NAME", "COMPLETED", "SEEDERS", "LEECHERS", "SIZE","ADDED", "TYPE") + color.ENDC)

    for item in json["torrents"]:
        print(template.format(str(i), item['id'], item['name'], item["times_completed"], item['seeders'], item['leechers'], round(float(item["size"]) / 1073741824, 2), item["added"], item["categoryname"]))
        i += 1


def getOnlyRes(json, res):
    retval = json.copy()
    del retval["torrents"]
    retval["torrents"] = []
    for item in json["torrents"]:
        if res in item["name"]:
            retval["torrents"].append(item)
    return retval

def perfomRequest(req):
    r = requests.get(domain + "/torrents/search/" + req["keyword"] + "?limit=50", headers=header).json()
    return r

def addTorrent(json, tlist):
    torrent = json["torrents"][tlist]
    torrentbyte = requests.get(domain + "/torrents/download/" + torrent["id"], headers=header)
    print(torrentbyte.content)
    with open(os.getenv("TEMP")+ torrent["id"] + ".torrent", "wb") as tfile:
        tfile.write(torrentbyte.content)


def main():
    login()
    req = userRequest.askRequest()
    r = perfomRequest(req)
    r = getOnlyRes(r, req["resolution"])
    printTorrents(r)
    tlist = userRequest.choose()
    addTorrent(r, tlist)


main()
