import csv 

filename = "phonebook.csv"

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        #print(row)
        name, phone_number = row
        print(name, phone_number)
        
