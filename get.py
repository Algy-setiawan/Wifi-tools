import csv
import os

contacts = []
os.system("ls -la")
print("Select Project")
folder = input()
with open(''+folder+'/'+folder+'-01.kismet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        contacts.append(row)

labels = contacts.pop(0)

#print(labels)
#print(contacts)

#print("-"*34)
for data in contacts:
    print(f"{data[3]}")