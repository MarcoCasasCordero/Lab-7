import datetime
import pathlib
import os
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
name=str(input("Enter Username: "))

import getpass

password = getpass.getpass("Please Enter Your Password: ")
from pathlib import Path
path = Path.cwd()
print(Path)
file = open("csrBackup.txt", "w")
ip = "192.168.11.11"
dictionary = {
    "ip": ip,
    "username": name,
    "password": password,
    "device_type": "cisco_ios"
}

connection = ConnectHandler(**dictionary)
output = connection.send_command("show run")
file.write(output)
file.close()
