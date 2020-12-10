#! /usr/bin/env python

import subprocess
from scapy.all import *
import datetime
import netaddr
from netmiko import ConnectHandler
import tacacs
import ip_range


now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
ping_file = "ping_results_"+timestamp+".txt"
out_file = "hostnames_"+timestamp+".txt"

# Functions
def etc_hosts_format():
# Single Line IP Format Hostname (/etc/hosts)   
        file1 = open(out_file,"a")
        file1.write(str(host) + '\t')
        file1.write(hostname)
        file1.write("\n")

def bind_a_format():

# Single Line Hostname IP Format (DNS A Record) 
        file1 = open(out_file,"a")
        file1.write(hostname + '\t')
        file1.write('\t' + "A" + '\t')
        file1.write(str(host))
        file1.write("\n")

def generic_format():
# Multiline Format (Generic)
        file1 = open(out_file,"a")
        file1.write(hostname)
        file1.write("\n")
        file1.write(str(host))
        file1.write("\n")

def ansible_inventory_format():
# Ansible Inventory Multiline Format
        file1 = open(out_file,"a")
        file1.write('[' + hostname + '_ssh_discovery]')
        file1.write("\n")
        file1.write(hostname + '\t')
        file1.write('ansible_host=' + str(host))
        file1.write("\n")

def log_ping():
        file2 = open(ping_file,"a")
        file2.write(str(ping0))
        file2.write("\n")
        file2.close()

# Define IP range to ping
network = ip_range.net

# make list of addresses out of network, set live host counter
addresses = netaddr.IPNetwork(network)
liveCounter = 0

# Send ICMP ping request, wait for answer
for host in addresses:
        if (host == addresses.network or host == addresses.broadcast):
                continue
        ping0 = "ping to", str(host), "OK"
        res = subprocess.call(['ping', '-c', '2', str(host)])
        if res == 0:
            print ping0
            device = ConnectHandler(device_type='cisco_ios', ip=host, username=tacacs.username, password=tacacs.password)        
            result = device.send_command("show run | in hostname")
            result = result.split()
            hostname = result[1]
            print(hostname)
            device.disconnect()
            etc_hosts_format()
#            bind_a_format()
#            generic_format()
#            ansible_inventory_format()
            log_ping()
        elif res == 2:
            print "no response from", host
        else:
            print "ping to", host, "failed!"
