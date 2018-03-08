'''
Owner - Rawal Shree
Email - rawalshreepal000@gmail.com
Github - https://github.com/rawalshree
'''


import subprocess

global cmd
cmd = [["sudo", "apt-get", "update"], ["sudo", "apt-get", "dist-update"], ["sudo", "apt-get", "install", "dnsmasq", "hostapd", "-y"],
        ["sudo", "apt-get", "install", "bridge-utils", "-y"], ["sudo", "apt-get", "install", "isc-dhcp-server", "-y"],
        ["sudo", "apt-get", "install", "iptables-persistent", "-y"], ["sudo", "systemctl", "stop", "dnsmasq"], ["sudo", "systemctl", "stop", "hostapd"],
        ["sudo", "mv", "/etc/dhcpcd.conf", "/etc/dhcpcd.conf.bak"], ["sudo", "mv", "dhcpcd.conf", "/etc/dhcpcd.conf"],
        ["sudo", "mv", "/etc/dhcp/dhcpd.conf", "/etc/dhcp/dhcpd.conf.bak"], ["sudo", "mv", "dhcpd.conf", "/etc/dhcp/dhcpd.conf"],
        ["sudo", "mv", "/etc/default/isc-dhcp-server", "/etc/default/isc-dhcp-server.bak"], ["sudo", "mv", "isc-dhcp-server", "/etc/default/isc-dhcp-server"],
        ["sudo", "mv", "/etc/network/interfaces", "/etc/network/interfaces.bak"], ["sudo", "mv", "interfaces", "/etc/network/interfaces"],
        ["sudo", "service", "dhcpcd", "restart"], ["sudo", "ifdown", "wlan0"], ["sudo", "ifup", "wlan0"], ["sudo", "mv", "dnsmasq.conf", "/etc/dnsmasq.conf"],
        ["sudo", "mv", "hostapd.conf", "/etc/hostapd/hostapd.conf"], ["sudo", "mv", "/etc/default/hostapd", "/etc/default/hostapd.bak"],
        ["sudo", "mv", "hostapd", "/etc/default/hostapd"], ["sudo", "service", "hostapd", "start"], ["sudo", "service", "dnsmasq", "start"],
        ["sudo", "mv", "/etc/sysctl.conf", "/etc/sysctl.conf.bak"], ["sudo", "mv", "sysctl.conf", "/etc/sysctl.conf"],
        ["sudo", "sh", "-c", "\"echo", "1", ">", "/proc/sys/net/ipv4/ip_forward\""], ["sudo", "iptables", "-t", "nat", "-A", "POSTROUTING", "-o", "wlan1", "-j", "MASQUERADE"],
        ["sudo", "iptables", "-A", "FORWARD", "-i", "wlan1", "-o", "wlan0", "-m", "state", "--state", "RELATED,ESTABLISHED", "-j", "ACCEPT"],
        ["sudo", "iptables", "-A", "FORWARD", "-i", "wlan0", "-o", "wlan1", "-j", "ACCEPT"], ["sudo", "sh", "-c", "\"iptables-save", ">", "/etc/iptables/rules.v4\""],
        ["sudo", "/usr/sbin/hostapd", "/etc/hostapd/hostapd.conf"]]

def piApple():
    global cmd
    for x in cmd:
        try:
            print("Executing" + cmd[x])
            subprocess.call(x)
        except:
            print("ERROR IN EXECUTING" + cmd[x])
    

try:
    piApple()
    print("Setup done Successfully")
except:
    print("Operations Not performed Successfully")