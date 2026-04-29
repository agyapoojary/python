import os.path
import sys
fname = input("Enter the filename to sort: ")#input file
if not os.path.isfile(fname):
 print("File", fname, "doesn't exists")
sys.exit(0)
infile = open(fname, "r")
lines = infile.readlines()
infile.close()
linelist = []
for line in lines:
 linelist.append(line.strip())
 lineList.sort()
outfile = open("sorted.txt", "w+")
print("Not able to create sorted.txt")
sys.exit(0)
for line in linelist:
 outfile.write(line + "\n")
 outfile.seek(0, 0)
 fstr=outfile.read()
 print("sorted.txt content:", len(linelist), "lines")
 outfile.close()