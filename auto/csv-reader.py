import csv

with open('./data_set/members.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

