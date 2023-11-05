#! /usr/bin/python3


import netifaces
import os

def configure_interface(interface, mode):
    interfaces = netifaces.interfaces()
    if interface in interfaces:
        if mode == 'static':
            os.system(f"sudo ifconfig {interface} down")
            os.system(f"sudo dhclient -r {interface}")
            os.system(f"sudo ifconfig {interface} 172.20.10.11 netmask 255.255.255.240 up")
        elif mode == 'dynamic':
            os.system(f"sudo dhclient {interface}")
        else:
            print("Invalid mode. Choose 'static' or 'dynamic'.")
    else:
        print("Interface not found.")

if __name__ == "__main__":
    interface_name = input("Enter the interface name: ")
    config_mode = input("Enter the mode (static/dynamic): ")
    configure_interface(interface_name, config_mode)

