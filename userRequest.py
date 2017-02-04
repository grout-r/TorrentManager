import sys

def askKeyword():

    print("What is your keyword ?")
    sys.stdout.write("$>")
    sys.stdout.flush()
    return sys.stdin.readline()

def askRes():
    print("""What resolution do you want ? Enter your choice :
    [0] Any
    [1] 720p
    [2] 1080p""")
    sys.stdout.write("$>")
    sys.stdout.flush()
    an = sys.stdin.readline()
    if (an == "0\n"):
        return ""
    if (an == "1\n"):
        return "720"
    if (an == "2\n"):
        return "1080"
    print("Invalid choice")
    return askRes()

def askRequest():
    req = {}
    req["keyword"] = askKeyword()
    req["resolution"] = askRes()
    return req


def choose():
    print("Choose your(s) torrent(s) : ")
    sys.stdout.write("$>")
    sys.stdout.flush()
    an = sys.stdin.readline()
    tor = int(an)
    return tor