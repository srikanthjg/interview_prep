import sys
import os


fo = open("test1.txt",'r+')


file_content=fo.readlines()
print file_content.split()

fo.close()
