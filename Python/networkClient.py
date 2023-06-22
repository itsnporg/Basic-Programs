#A simple program to view all device connected to network



#!/usr/bin/env python
import scapy.all as scapy
import argparse


def get_agruments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Enter target to scan IP/Range")
    options = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_brodcast = brodcast / arp_request
    answered_list = scapy.srp(arp_request_brodcast, timeout=1, verbose=False)[0]

    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "Mac Address": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list


def print_result(result_list):
    print("IP\t\t\t Mac Address\n--------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["Mac Address"])


options = get_agruments()
scan_result = scan(options.target)
print_result(scan_result)
