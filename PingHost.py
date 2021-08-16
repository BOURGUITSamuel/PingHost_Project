# coding: utf-8

import os
import sys
import colorama
from colorama import Fore

# Verifies your os type
OS_TYPE = os.name

# Sets the count modifier to the os type
count = '-n' if OS_TYPE == 'nt' else '-c'


def create_ip_list():
    """Creates an ip address list"""
    ip_list = []

    with open("ip_file.txt", "r") as file:
        for line in file:
            ip_list.append(line.strip())
    return ip_list


def ping_device(ip_list):
    """Ping ip_list and return results"""
   
    results_file = open("results.txt", "w")

    for ip in ip_list:
        response = os.popen(f"ping {ip} {count} 1").read()
        if "TTL" in response:
            print(Fore.GREEN + f'UP' + Fore.WHITE + '', f'[{ip}]' + '', 'Ping Successful')
            results_file.write(f"UP {ip} Ping Successful" + "\n")
        else:
            print(Fore.RED + f'DOWN' + Fore.WHITE + '', f'[{ip}]' + '', 'Ping UnSuccessful')
            results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
    results_file.close()


def main():
    """ Verify if IP list is empty before starting IP Scan"""

    filesize = os.path.getsize("ip_file.txt")

    if filesize == 0:
        print(Fore.RED + "The program has been interrupted : The IP list is empty!")
        sys.exit()
    else:
        print('Start IP Scan...')
        ping_device(create_ip_list())
        print('IP Scan is finish!')


if __name__ == "__main__":
    main()
