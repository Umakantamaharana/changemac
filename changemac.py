import random
import re
import subprocess
import os

def opt():
    print("\n1. Enter a MAC to change.")
    print("2. Apply  a random mac.")
    print("3. Exit.")

def getrandommac():
    chars = "0123456789abcdef"
    randommacaddress = "00"
    for i in range(5):
        randommacaddress += ":" + random.choice(chars) + random.choice(chars)
    print(randommacaddress)
    return randommacaddress

def changemac(*newmac):
    count = 0
    interfaces = os.listdir('/sys/class/net')
    print("Network interfaces available")
    for i in interfaces:
        print(count," -> ",i,"\n")
        count += 1
    interface = int(input("Choose an interface to change mac : "))
    print("Changing MAC address (",interfaces[interface],") ...")
    print("Current MAC : ",currentmac())

    if not newmac:
        newmac = getrandommac()

    try:
        subprocess.call(["sudo", "ifconfig", interfaces[interface], "down"])
        subprocess.check_output(["sudo", "ifconfig", interfaces[interface], "hw", "ether", newmac[0]])
        subprocess.call(["sudo", "ifconfig", interfaces[interface], "up"])
        print("Changing mac to : " ,newmac[0])
        print("MAC changed successfully.")
    except:
        print("[!] Enter a valid MAC address.")

def currentmac():
    output = subprocess.check_output(["ifconfig"])
    return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output)).group(0)

while True:
    opt()
    inp = input("\nWhat you want to do : ")
    if inp == "1":
        newmac = input("Type a MAC address : ")
        try:
            c = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(newmac)).group(0)
        except:
            print("\n[!] Enter a valid MAC address.\n")
            continue
        changemac(newmac)
    elif inp == "2":
        newmac = getrandommac()
        print(newmac)
        changemac(newmac)
    elif inp == "3":
        break
    else:
        print("\n[!] Choose valid option ..")
        continue