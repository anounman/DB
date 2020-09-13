#!/usr/bin/env python3
import optparse
import os.path
from os import path
import os
import random
import string
import sys
import requests
import time
letters = string.ascii_lowercase
n = ''.join(random.choice(letters) for i in range(3))
def paths():
    paths = path.exists("/usr/bin/cewl")
    return paths
def parser():
    par = optparse.OptionParser()
    par.add_option("-u", "--url", dest="url", help="Please use -u or --u or use -h for more info")
    (options, argument) = par.parse_args()
    if not options.url:
        print("Please use -u for specify a url or use -h or --help for more info")
        sys.exit()
    return options
def install():
    print("[+]Findng Path...[+]")
    cewl = paths()
    if cewl and dirb:
        print("[+]Successfully Find The Paths[+]")
    else:
        print("[+]Install Requirement[+]")
        os.system("apt-get install cewl -y")
        os.system("clear")
def wordlist(url):
    print("[+]Genarating Wordlist...[+]")
    os.system("cewl "+url+ " -d 2 "+"-w "+n+".txt")
    print("[+]Successfully Genarated Wordlsit[+]")
def dirb(url):
    print("[+]Start Finding Directories[+]")
    path_name = str(n+".txt")
    with open(path_name, 'r+') as file:
        wrds = file.readlines()
        for word in wrds:
            Furl = url+"/"+word
            responce = requests.get(Furl)
            if responce:
                print("[+]Discover URL ---->"+Furl)
    print("[+]Finding Completed[+]")
if __name__ == "__main__":
    try:
        install()
        options = parser()
        wordlist(options.url)
        dirb(options.url)
        x = input("Do You want to remove genarated wordlist(Y/N)>")
        if x == "y" or x =="Y":
            wdlst = str(n+".txt")
            os.remove(wdlst)
        else:
            wdlst = str(n+".txt")
            os.system("mv "+  wdlst + " wordLst.txt")
            SystemExit
    except KeyboardInterrupt:
        print("[-]Detected CTRL+C quiting...[-]")