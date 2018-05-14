import csv
import os
import re

# define normalize function
def normalize(req):
    # req = re.sub('[(),.:]', '', req)
    # req = re.sub('[/]', ' ', req)
    return req

# define column indexes
Rqt = 0
Priority = 1
Function = 2
Requirement = 3

# number of requirements to Cartesian product
max_rows = 100

# test user data dir from root
test_user_data_dir = os.path.join('data/user/test/')

with open('scripts/requirements/requirements.csv', 'rb') as csvfile:
    # read csv
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # open files
    id_file = open(test_user_data_dir + 'id.txt', 'w')
    sim_file = open(test_user_data_dir + 'sim.txt', 'w')
    a_file = open(test_user_data_dir + 'a.toks', 'w')
    b_file = open(test_user_data_dir + 'b.toks', 'w')

    counter = 0
    for index,row in enumerate(reader):
        # skip first row
        if (index != 0):
            if (row[Rqt] != '' and index < max_rows):
                # write x rows to a.toks
                for x in range(max_rows):
                    counter = counter + 1

                    id_file.write(str(counter) + "\n")

                    # write dummy value to sim.txt
                    # (required for some reason)
                    sim_file.write("0\n")

                    a_file.write(normalize(row[Requirement]) + "\n")

    # write to b.toks x times
    for i in range(max_rows):
        # reset read position
        csvfile.seek(0)

        # loop rows
        for index,row in enumerate(reader):
            # skip first row
            if (index != 0):
                if (row[Rqt] != '' and index < max_rows):
                    b_file.write(normalize(row[Requirement]) + "\n")

    # close files
    id_file.close()
    a_file.close()
    b_file.close()
