#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

print()

print("Confused to scan which port ? go back and check the file called allPorts.txt to get list of all famous ports !")

print()

host = input("Enter IP or Web address to scan ! : ")
port = int(input("Please enter the port you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)
