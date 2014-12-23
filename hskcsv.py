import csv

with open('L6.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('hskdict_L6.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        hskdict = dict((rows[0],rows[1]) for rows in reader)


