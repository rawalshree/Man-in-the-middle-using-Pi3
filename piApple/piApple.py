import subprocess

def piApple():
    try:
        subprocess.call(["sudo", "apt-get", "update"])
    except:
        print("cannot execute sudo apt-get update")
    try:
        subprocess.call(["sudo", "apt-get", "dist-update"])
    except:
        print("cannot execute dist-update")
    try:
        subprocess.call(["sudo", "apt-get", "install", "dnsmasq", "hostapd", "-y"])
    except:
        print("cannot install dnsmasq and hostapd")
    try:
        subprocess.call(["sudo", "apt-get", "install", "bridge-utils", "-y"])
    except:
        print("cannot install bridge-utils")
    try:
        subprocess.call(["sudo", "apt-get", "install", "isc-dhcp-server", "-y"])
    except:
        print("cannot install isc-dhcp-server")
    try:
        subprocess.call(["sudo", "apt-get", "install", "iptables-persistent", "-y"])
    except:
        print("cannot install iptables-persitent")
    try:
        subprocess.call(["sudo", "systemctl", "stop", "dnsmasq"])
    except:
        print("Error in systemctl stop dnsmasq")
    try:
        subprocess.call(["sudo", "systemctl", "stop", "hostapd"])
    except:
        print("Error in systemctl stop hostapd")
    try:
        subprocess.call(["sudo", "mv", "/etc/dhcpcd.conf", "/etc/dhcpcd.conf.bak"])
    except:
        print(" Error in backup dhcpcd.conf file")
    try:
        subprocess.call(["sudo", "mv", "dhcpcd.conf", "/etc/dhcpcd.conf"])
    except:
        print(" Error in moving dhcpcd.conf file")
    try:
        subprocess.call(["sudo", "mv", "/etc/dhcp/dhcpd.conf", "/etc/dhcp/dhcpd.conf.bak"])
    except:
        print(" Error in backup dhcpd.conf file")
    try:
        subprocess.call(["sudo", "mv", "dhcpd.conf", "/etc/dhcp/dhcpd.conf"])
    except:
        print(" Error in moving dhcpcd.conf file")
    try:
        subprocess.call(["sudo", "mv", "/etc/default/isc-dhcp-server", "/etc/default/isc-dhcp-server.bak"])
    except:
        print(" Error in backup isc-dhcp-server file")
    try:
        subprocess.call(["sudo", "mv", "isc-dhcp-server", "/etc/default/isc-dhcp-server"])
    except:
        print(" Error in moving isc-dhcp-server file")
    try:
        subprocess.call(["sudo", "mv", "/etc/network/interfaces", "/etc/network/interfaces.bak"])
    except:
        print(" Error in backup interfaces file")
    try:
        subprocess.call(["sudo", "mv", "interfaces", "/etc/network/interfaces"])
    except:
        print(" Error in moving dhcpcd.conf file")
    try:
        subprocess.call(["sudo", "service", "dhcpcd", "restart"])
    except:
        print(" Error in service dhcpcd restart")
    try:
        subprocess.call(["sudo", "ifdown", "wlan0"])
    except:
        print(" Error in ifdown wlan0")
    try:
        subprocess.call(["sudo", "ifup", "wlan0"])
    except:
        print(" Error in ifup wlan0")
    try:
        subprocess.call(["sudo", "mv", "dnsmasq.conf", "/etc/dnsmasq.conf"])
    except:
        print(" Error in moving dnsmasq.conf file")
    try:
        subprocess.call(["sudo", "mv", "hostapd.conf", "/etc/hostapd/hostapd.conf"])
    except:
        print(" Error in moving hostapd.conf file")
    try:
        subprocess.call(["sudo", "mv", "/etc/default/hostapd", "/etc/default/hostapd.bak"])
    except:
        print(" Error in backup hostapd.conf file")
    try:
        subprocess.call(["sudo", "mv", "hostapd", "/etc/default/hostapd"])
    except:
        print(" Error in moving hostapd.conf file")
    try:
        subprocess.call(["sudo", "service", "hostapd", "start"])
    except:
        print(" Error in service hostapd start")
    try:
        subprocess.call(["sudo", "service", "dnsmasq", "start"])
    except:
        print(" Error in service dnsmasq start")
    try:
        subprocess.call(["sudo", "mv", "/etc/sysctl.conf", "/etc/sysctl.conf.bak"])
    except:
        print(" Error in backup sysctl.cong file")
    try:
        subprocess.call(["sudo", "mv", "sysctl.conf", "/etc/sysctl.conf"])
    except:
        print(" Error in moving sysctl.conf file")
    try:
        subprocess.call(["sudo", "sh", "-c", "\"echo", "1", ">", "/proc/sys/net/ipv4/ip_forward\""])
    except:
        print(" Error in /proc/sys/net/ipv4/ip_forward")
    try:
        subprocess.call(["sudo", "iptables", "-t", "nat", "-A", "POSTROUTING", "-o", "wlan1", "-j", "MASQUERADE"])
    except:
        print(" Error in adding IP RULE # 1")
    try:
        subprocess.call(["sudo", "iptables", "-A", "FORWARD", "-i", "wlan1", "-o", "wlan0", "-m", "state", "--state", "RELATED,ESTABLISHED", "-j", "ACCEPT"])
    except:
        print(" Error in adding IP RULE # 2")
    try:
        subprocess.call(["sudo", "iptables", "-A", "FORWARD", "-i", "wlan0", "-o", "wlan1", "-j", "ACCEPT"])
    except:
        print(" Error in adding IP RULE # 3")
    try:
        subprocess.call(["sudo", "sh", "-c", "\"iptables-save", ">", "/etc/iptables/rules.v4\""])
    except:
        print("Error in saving iptables rules")
    try:
        subprocess.call(["sudo", "/usr/sbin/hostapd", "/etc/hostapd/hostapd.conf"])
    except:
        print(" Error in starting hostapd.conf for access point")
 

try:
    piApple()
    print("Setup done Successfully")
except:
    print("Operations Not performed Successfully")