import csv
import os
import re

def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

groups_dir = os.path.join('Requirements/groups/')
group = 0

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(groups_dir) if isfile(join(groups_dir, f))]

def file_key(file):
    return int(file[:-4])

for file in sorted(onlyfiles, key=file_key):
    print(str(file) + ' ' + str(file_len(groups_dir + file)-1))