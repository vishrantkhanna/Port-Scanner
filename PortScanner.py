#!/usr/bin/python3

import socket

ip = input("IP Address: ")

port_list = {
    1: "TCP Port Service Multiplexer (TCPMUX)",
    5: "Remote Job Entry (RJE)",
    7: "ECHO",
    18: "Message Send Protocol (MSP)",
    20: "FTP -- Data",
    21: "FTP -- Control",
    22: "SSH Remote Login Protocol",
    23: "Telnet",
    25: "Simple Mail Transfer Protocol (SMTP)",
    29: "MSG ICP",
    37: "Time",
    42: "Host Name Server (Nameserv)",
    43: "WhoIs",
    49: "Login Host Protocol (Login)",
    53: "Domain Name System (DNS)",
    69: "Trivial File Transfer Protocol (TFTP)",
    70: "Gopher Services",
    79: "Finger",
    80: "HTTP",
    103: "X.400 Standard",
    108: "SNA Gateway Access Server",
    109: "POP2",
    110: "POP3",
    115: "Simple File Transfer Protocol (SFTP)",
    118: "SQL Services",
    119: "Newsgroup (NNTP)",
    137: "NetBIOS Name Service",
    139: "NetBIOS Datagram Service",
    143: "Interim Mail Access Protocol (IMAP)",
    150: "NetBIOS Session Service",
    156: "SQL Server",
    161: "SNMP",
    179: "Border Gateway Protocol (BGP)",
    190: "Gateway Access Control Protocol (GACP)",
    194: "Internet Relay Chat (IRC)",
    197: "Directory Location Service (DLS)",
    389: "Lightweight Directory Access Protocol (LDAP)",
    396: "Novell Netware over IP",
    443: "HTTPS",
    444: "Simple Network Paging Protocol (SNPP)",
    445: "Microsoft-DS",
    458: "Apple QuickTime",
    546: "DHCP Client",
    547: "DHCP Server",
    563: "SNEWS",
    569: "MSN",
    1080: "Socks",
}

print("\n")

print("List of commonly used ports: ")
for port, name in port_list.items():
    print(port, name)

print("\n")


def scanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)

    if s.connect_ex((ip, port)):
        print(port, "is closed.")
    else:
        print(port, "is open.")

    s.close()


for port in port_list:
    scanner(ip, port)
