import os
import sys
import subprocess
from time import sleep
import time


def piApple():
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "dist-update"])
    subprocess.call(["sudo", "apt-get", "install", "dnsmasq", "hostapd", "-y"])
    subprocess.call(["sudo", "apt-get", "install", "bridge-utils", "-y"])
    subprocess.call(["sudo", "apt-get", "install", "isc-dhcp-server", "-y"])
    subprocess.call(["sudo", "apt-get", "install", "iptables-persistent", "-y"])
    subprocess.call(["sudo", "systemctl", "stop", "dnsmasq"])
    subprocess.call(["sudo", "systemctl", "stop", "hostapd"])
    subprocess.call(["sudo", "mv", "/etc/dhcpcd.conf", "/etc/dhcpcd.conf.bak"])
    subprocess.call(["sudo", "mv", "dhcpcd.conf", "/etc/dhcpcd.conf"])
    subprocess.call(["sudo", "mv", "/etc/dhcp/dhcpd.conf", "/etc/dhcp/dhcpd.conf.bak"])
    subprocess.call(["sudo", "mv", "dhcpd.conf", "/etc/dhcp/dhcpd.conf"])
    subprocess.call(["sudo", "mv", "/etc/default/isc-dhcp-server", "/etc/default/isc-dhcp-server.bak"])
    subprocess.call(["sudo", "mv", "isc-dhcp-server", "/etc/default/isc-dhcp-server"])
    subprocess.call(["sudo", "mv", "/etc/network/interfaces", "/etc/network/interfaces.bak"])
    subprocess.call(["sudo", "mv", "interfaces", "/etc/network/interfaces"])
    subprocess.call(["sudo", "service", "dhcpcd", "restart"])
    subprocess.call(["sudo", "ifdown", "wlan0"])
    subprocess.call(["sudo", "ifup", "wlan0"])
    subprocess.call(["sudo", "mv", "dnsmasq.conf", "/etc/dnsmasq.conf"])
    subprocess.call(["sudo", "mv", "hostapd.conf", "/etc/hostapd/hostapd.conf"])
    subprocess.call(["sudo", "mv", "/etc/default/hostapd", "/etc/default/hostapd.bak"])
    subprocess.call(["sudo", "mv", "hostapd", "/etc/default/hostapd"])
    subprocess.call(["sudo", "service", "hostapd", "start"])
    subprocess.call(["sudo", "service", "dnsmasq", "start"])
    subprocess.call(["sudo", "mv", "/etc/sysctl.conf", "/etc/sysctl.conf.bak"])
    subprocess.call(["sudo", "mv", "sysctl.conf", "/etc/sysctl.conf"])
    subprocess.call(["sudo", "sh", "-c", "\"echo", "1", ">", "/proc/sys/net/ipv4/ip_forward\""])
    subprocess.call(["sudo", "iptables", "-t", "nat", "-A", "POSTROUTING", "-o", "wlan1", "-j", "MASQUERADE"])
    subprocess.call(["sudo", "iptables", "-A", "FORWARD", "-i", "wlan1", "-o", "wlan0", "-m", "state", "--state", "RELATED,ESTABLISHED", "-j", "ACCEPT"])
    subprocess.call(["sudo", "iptables", "-A", "FORWARD", "-i", "wlan0", "-o", "wlan1", "-j", "ACCEPT"])
    subprocess.call(["sudo", "sh", "-c", "\"iptables-save", ">", "/etc/iptables/rules.v4\""])
    subprocess.call(["sudo", "/usr/sbin/hostapd", "/etc/hostapd/hostapd.conf"])
 

try:
    piApple()
except:
    print("Failed to perform certain opertaions")