import csv
import os
import re

# define column indexes
Rqt = 0
Priority = 1
Function = 2
Requirement = 3

groups_dir = os.path.join('Requirements/groups/')
group = 0

with open('Requirements/requirements.csv', 'rb') as csvfile:
    # read csv
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # open group file
    group_file = open(groups_dir + str(group) + '.csv', 'w')

    # create csv writer
    writer = csv.writer(group_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    counter = 0
    group_name = ""

    for index,row in enumerate(reader):
        # skip first row
        if (index != 0):

            # increment group when Rqt is null
            if (row[Rqt] == ''):
                if (row[Requirement] != group_name):
                    # assign group name
                    group_name = row[Requirement]

                    # close group file if open
                    group_file.close()

                    # increment group
                    group = group + 1

                    # open next group file
                    group_file = open(groups_dir + str(group) + '.csv', 'w')
                    
                    # create csv writer
                    writer = csv.writer(group_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    writer.writerow([group_name])
            else:
                # write to group file
                writer.writerow(row)

    # close files
    group_file.close()
