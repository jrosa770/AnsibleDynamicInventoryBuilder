# SSH Dicovery Script

## Requires two files:

### tacacs.py - TACACS Authentication Container

### ip_range.py - IP Subnet to scan

## tacacs.py Format:

```py
username = 'user.name'
password = 'your.password'
```

`chmod to user only RW (chmod 600 tacacs.py)`



## ip_range.py Format:

```py
net = ‘<subnet/mask>’
Example:
net = '10.100.20.0/29'
```

## Possible pip installs:

scapy

netaddr

netmiko

## For Redhat and forks install pip via:

```sh
# Install PIP if needed

sudo yum -y install python-pip

# PIP package installs:

sudo pip install --upgrade pip

sudo pip install netaddr

sudo pip install config

sudo  pip install --pre scapy
```
