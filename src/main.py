import os
import requests
import json

def diskInit():
    os.system("lsblk")
    print("Enter partition identifier (Example sda1) DO NOT USE /dev/ just the identifier")
    Partition = input("Enter partition identifier: ")
    input(f"You seleected '{Partition}' press enter to continue. if this is incorrect press ctrl+c and rerun the installer!")
if __name__ == '__main__':
    diskInit()