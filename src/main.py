import os
import requests

def partitionInit():
    os.system("lsblk")
    print("Enter partition identifier (Example sda1) DO NOT USE /dev/ just the identifier")
    Partition = input("Enter partition identifier: ")
    input(f"You selected Partition '{Partition}' press enter to continue. if this is incorrect press ctrl+c and rerun the installer!")

def diskInit():
    os.system("lsblk")
    print("Enter disk identifier (Example sda) DO NOT USE /dev/ just the identifier")
    Disk = input("Enter disk identifier: ")
    input(f"You selected Disk '{Disk}' press enter to continue. if this is incorrect press ctrl+c and rerun the installer!")


while True:
    diskorpartition = input("Do you want to use a disk or a partition? (disk/partition): ")
    if diskorpartition == "disk":
        diskInit()
    elif diskorpartition == "partition":
        partitionInit()
    else:
        print("\n\n\n Invalid input! Please enter either 'disk' or 'partition' \n\n\n")