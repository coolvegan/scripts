#!/opt/homebrew/bin/python3
import os
import sys
from re import sub

class Dir:
    src = ""
    dest = ""
    filter = []
    def add(self,substr):
        self.filter.append(substr)
        return self

    def __init__(self, src, dest) -> None:
        self.src = src
        self.dest = dest
    def rec(self):
        for root, dirs, files in os.walk(self.src , topdown=True, followlinks=False):
            for name in files:
                for substr in self.filter:
                    if substr in name:
                        print(name)

    def go(self):
        dirExists = os.path.exists(self.dest)
        if not dirExists:
            print("Error: Destination Directory "+self.dest+" is not available.")
            return
        for name in os.listdir(self.src):
            for substr in self.filter:
                if substr in name:
                    srcfile = self.src+'/'+name
                    print("moving " +srcfile + " to "+self.dest)
                    os.system('mv "'+srcfile+'" '+ self.dest)

srcPath=""
dstPath=""
filter=""
if(len(sys.argv)==1):
    print("usage: "+sys.argv[0]+" -s=<src_dir> -d=<dst_dir -f=mkv,mp4,avi")
    exit(0)
for arg in sys.argv:
  if("-s" in arg):
    srcPath=arg.split("=")[1]
  if("-d" in arg):
    dstPath=arg.split("=")[1]
  if("-f" in arg):
    filter=arg.split("=")[1]
dirExists = os.path.exists(srcPath) and os.path.exists(dstPath)
if(not dirExists):
    print("Error: Quell oder Zielverzeichnis existieren nicht!")
    exit(-1)

dir = Dir(srcPath, dstPath)
for ext in filter.split(','):
    dir.add(ext)
dir.go()
