from os import system
from sys import argv
import socket
import psutil


def get_ip():
    ips = psutil.net_if_addrs()
    adress = {}
    for i in ips:
        adress[i] = ips[i][0].address
    return adress


def ping(host):
    return system("ping -c 1 " + host + " > /dev/null")


def is_up(host):
    if ping(host) == 0:
        return "UP !"
    else:
        return "DOWN !"


def lookup(name):
    return socket.gethostbyname(name)


if __name__ == "__main__":
    CMD = argv[1]
    if CMD == "ip":
        for i in get_ip():
            print(i, ":", get_ip()[i])
    elif CMD == "ping":
        print(is_up(argv[2]))
    elif CMD == "lookup":
        print(lookup(argv[2]))
    else:
        print(f"{CMD} is not a valid command. Déso.")
