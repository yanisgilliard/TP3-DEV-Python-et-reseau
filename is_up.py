from os import system
from sys import argv

def is_up(host):
    return system("ping -c 1 " + host + "/dev/null") == 0 

if __name__ == "__main__":
    if len(argv) !=2:
        print ("usage : python3 is_up.py <host>")
        exit(1)
    if is_up(argv[1]):
        print("up !")
    else: 
        print("down !")