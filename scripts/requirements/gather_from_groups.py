import csv
import os
import re

# define column indexes
Rqt = 0
Priority = 1
Function = 2
Requirement = 3

# get number of rows in file
def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# sort function for directory listing
def file_key(file):
    return int(file[:-4])

groups_dir = os.path.join('Requirements/groups/')
test_user_data_dir = os.path.join('SemanticRelatednessModel/data/user/test/')

N = 10
max_rows = 100
max_groups = max_rows / N

onlyfiles = [f for f in os.listdir(groups_dir) if os.path.isfile(os.path.join(groups_dir, f))]

groups = []
group_data = []

# read csv

# gather all groups with > N rows
count = 0
for file in sorted(onlyfiles, key=file_key):
    # if enough lines
    if file_len(groups_dir + file) > N:
        print str(count) + " " + file
        count = count + 1
        # get first 10 rows
        with open(groups_dir + file) as group_file:
            head = []
            reader = csv.reader(group_file, delimiter=',', quotechar='"')
            
            for index,row in enumerate(reader):
                # skip first row
                if (index != 0):
                    # get first N rows
                    if (index < N+1):
                        head.append(row)
                    else:
                        break;

        # append data
        group_data.append(head)

        # track group
        groups.append(file[:-4])

# build a.tok
# repeat each row X times, where X = (max_groups - 1) * N
a_file = open(test_user_data_dir + 'a.toks', 'w')
for index,group in enumerate(group_data[0:max_groups]):
    for row in group:
        for i in range(0, (max_groups-1)*N):
            a_file.write(str(index) + " " + row[Requirement] + "\n")

# build b.tok
# output all groups (except one) max_groups times
count = 0
b_file = open(test_user_data_dir + 'b.toks', 'w')
for i in range(max_groups):
    # print(i)
    for j in range(N):
        for index,group in enumerate(group_data[0:max_groups]):
            if index != i:
                # print index
                for row in group:
                    # print row
                    count = count + 1
                    b_file.write(str(index) + " " + row[Requirement] + "\n")
# print(count)