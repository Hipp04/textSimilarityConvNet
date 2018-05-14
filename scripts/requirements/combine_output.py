import csv

user_dir = 'SemanticRelatednessModel/data/user'

# open files and process rows
with open(user_dir + '/test/a.toks', 'rb') as a_file, \
    open(user_dir + '/test/b.toks', 'rb') as b_file, \
    open(user_dir + '/test/id.txt', 'rb') as id_file, \
    open(user_dir + '/output.txt', 'r') as r_file, \
    open(user_dir + '/combined.csv', 'w') as o_file:
        # create csv writer
        writer = csv.writer(o_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # header row
        writer.writerow(['ID', 'Similarity', 'A', 'B'])

        # loop rows writing to output
        for a, b, r, ID in zip(a_file, b_file, r_file, id_file):
            if (a != b):
                writer.writerow([ID.rstrip(), round(float(r), 10), a.rstrip(), b.rstrip()])
