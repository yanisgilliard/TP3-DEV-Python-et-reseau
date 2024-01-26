import psutil


def get_ip():
    ips = psutil.net_if_addrs()
    adress = {}
    for i in ips:
        adress[i] = ips[i][0].address
    return adress


if __name__ == "__main__":
    for i in get_ip():
        print(i, ":", get_ip()[i])
