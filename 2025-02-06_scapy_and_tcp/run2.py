import scapy.all as scapy
import json as json

"""
Note:
In Linux (like Ubuntu) you need to run this script with 'sudo' and bring in the non-sudo $PATH env var.

$ sudo env PATH=$PATH python run2.py
"""


if __name__ == '__main__':
    print("Scapy demo 1")

    ifaces = scapy.conf.ifaces

    import pprint
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(ifaces)
    # Display info to help user see interfaces of interest
    for i, iface_key in enumerate(ifaces.keys()):
        print("i = ", i, ", iface name = ", ifaces[iface_key].name)

    iface_index = int(input("Please enter the index number for the interface to sniff: "))
    print("You have chosen index: ", iface_index)
    iface_name = ifaces[list(ifaces.keys())[iface_index]].name
    iface_name = ifaces[list(ifaces.keys())[iface_index]].name
    print("Corresponding iface name: ", iface_name)

    capture = scapy.sniff(iface=iface_name, count=5, timeout=5)

    print(capture)