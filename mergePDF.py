from ast import For
import PyPDF2
import os
import sys
from re import sub
from Header import getHeader, sign

class PyPDFWrapper:
    def debug(self):
        for file in self.pdffiles:
            print(file)
    def __init__(self):
        self.pdffiles = []
        self.pdfWriter = PyPDF2.PdfFileWriter()
    def add(self, pdffile, scale):
        self.pdffiles.append({"filename":pdffile,"scale":scale})
        return self
    def prepare(self):
        for filename in self.pdffiles:
            try:
                obj = PyPDF2.PdfFileReader(filename['filename'])

                for pageNum in range(obj.numPages):
                    pageObj = obj.getPage(pageNum)
                    if(filename['scale']):
                        pageObj.scale_to(2143,3030.2)
                        pageObj.mergePage(sign())
                    self.pdfWriter.addPage(pageObj)
            except:
                print("Error: "+filename+" wasn't readable!")

        return self
    def toDisk(self,filename):
        self.prepare()
        pdfOutputFile = open(filename, 'wb')
        try:
            self.pdfWriter.write(pdfOutputFile)
        except:
            print('Error when writing')
        pdfOutputFile.close()



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

    def go(self, pdfWrapper):
        dirExists = os.path.exists(self.dest)
        if not dirExists:
            print("Error: Destination Directory "+self.dest+" is not available.")
            return
        for name in os.listdir(self.src):
            for substr in self.filter:
                if substr in name:
                    srcfile = self.src+name
                    pdfWrapper.add(srcfile, True)

srcPath=""
dstPath=""
filter=""
if not ((len(sys.argv)==5) or (len(sys.argv)==6)):
    print("usage: "+sys.argv[0]+" -s=<src_dir> -d=<dst_dir -f=pdf -o=outPutFilename.pdf [-pdf=<path2pdfFileInQuotes>[,<path2pdfFileInQuotes>]]")
    exit(0)
pdfWrapper = PyPDFWrapper()
pdfWrapper.add(getHeader(), False)

for arg in sys.argv:
  if("-s" in arg):
    srcPath=arg.split("=")[1]
  if("-d" in arg):
    dstPath=arg.split("=")[1]
  if("-f" in arg):
    filter=arg.split("=")[1]
  if("-o" in arg):
    outPutFilename=arg.split("=")[1]
  if("-pdfPrefix" in arg):
    try:
        for pdfFile in arg.split("=")[1].split(','):
            pdfWrapper.add(pdfFile, True)
    except:
        print("Error: pdfPrefix not working. Maybe wrong path?")

dirExists = os.path.exists(srcPath) and os.path.exists(dstPath)
if(not dirExists):
    print("Error: Quell oder Zielverzeichnis existieren nicht!")
    exit(-1)



dir = Dir(srcPath, dstPath)
for ext in filter.split(','):
    dir.add(ext)

dir.go(pdfWrapper)

pdfWrapper.toDisk(dstPath+outPutFilename)
