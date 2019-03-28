# @Time: 2019/2/28-17:23
# @Author: wangyun


import sys

file = "C:/Users/wangyun/Desktop/demo.diff.txt"

output = sys.stdout

with open(file, 'r', encoding='UTF-8', errors='ignore') as f:
    fileNew = "C:/Users/wangyun/Desktop/demo.new.txt"
    outputfile = open(fileNew, 'w')
    for line in f:
        if ('diff' in line):
            print(line, end=' ')
            outputfile.write(line)
    outputfile.close()
sys.stdout = output
