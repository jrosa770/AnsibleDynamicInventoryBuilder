# Ansible Dynamic Inventory Builder

## Migrated from AnsibleCisco_IOS-NXOS_Builds on 03/26/2020

### Versions Migrated

- 1.2 (Dev)
- 1.3 (Dev and RC)

## Development

> Version 1.3

- Added Dynamic group split and add into inventory by OS
  - ios
  - nxos
  - iosxr
  - aci

 **Version 1.2 and above, CSV Headers (with cell reference numbers used in templates)**

| Header               | Definition                             | 
|----------------------|----------------------------------------| 
| Hostname (0)         | Alias or FQDN                          | 
| HostIP (1)           | IPv4/6 Address                         |
| OS (2)               | Operating System (ios/ nxos/iosxr/aci) | 


#### Example CSV

```csv
Hostname,HostIP,OS
P-BNAAE-FSW-701,10.160.2.71,nxos
TAM3-MDFA1-ASW4.domain.com,10.164.254.198,ios
lab-host-11,10.1.1.1,ios
lab-host-12,10.1.1.2,ios
lab-host-21,10.2.1.1,nxos
lab-host-22,10.2.1.2,nxos
```

#### Excel View

| Hostname                     | HostIP         | OS   | 
|------------------------------|----------------|------| 
| P-BNAAE-FSW-701              | 10.160.2.71    | nxos | 
| TAM3-MDFA1-ASW4.domain.com | 10.164.254.198 | ios  | 
| lab-host-11                  | 10.1.1.1       | ios  | 
| lab-host-12                  | 10.1.1.2       | ios  | 
| lab-host-21                  | 10.2.1.1       | nxos | 
| lab-host-22                  | 10.2.1.2       | nxos | 

#### Dynamic Inventory Output

```ini
[all:vars]
ansible_python_interpreter=/usr/bin/python3
ansible_connection = local

[cisco:children]
dynamic_inventory
ios
nxos
iosxr
aci

[ios:children]
TAM3-MDFA1-ASW4.domain.com_DYN
lab-host-11_DYN
lab-host-12_DYN
#IOS_GRP

[nxos:children]
P-BNAAE-FSW-701_DYN
lab-host-21_DYN
lab-host-22_DYN
#NXOS_GRP

[iosxr:children]
#IOSXR_GRP

[aci:children]
aci_prod
aci_dev
#ACI_GRP

[aci_dev]
lab-apic ansible_host=10.165.2.214

[aci_prod]
dev-apic ansible_host=10.90.20.11

[infoblox:children]
infoblox_prod
infoblox_dev

[infoblox_prod]

[infoblox_dev]

[panos:children]
panos_prod
panos_dev

[panos_prod]

[panos_dev]

[world_net:children]
usa_net

[usa_net:children]
ga_net
tn_net

[ga_net]

[tn_net]

[dynamic_inventory:children]
P-BNAAE-FSW-701_DYN
TAM3-MDFA1-ASW4.domain.com_DYN
lab-host-11_DYN
lab-host-12_DYN
lab-host-21_DYN
lab-host-22_DYN
#DYNAMIC_GRPS

# == P-BNAAE-FSW-701 == #
# Added with test-1.3-03_josrosa-03-26-2020_0854
[P-BNAAE-FSW-701_DYN:vars]
ansible_network_os=nxos

[P-BNAAE-FSW-701_DYN]
P-BNAAE-FSW-701 ansible_host=10.160.2.71

# == TAM3-MDFA1-ASW4.domain.com == #
# Added with test-1.3-03_josrosa-03-26-2020_0854
[TAM3-MDFA1-ASW4.domain.com_DYN:vars]
ansible_network_os=ios

[TAM3-MDFA1-ASW4.domain.com_DYN]
TAM3-MDFA1-ASW4.domain.com ansible_host=10.164.254.198

# == lab-host-11 == #
# Added with test-1.3-03_josrosa-03-26-2020_0854
[lab-host-11_DYN:vars]
ansible_network_os=ios

[lab-host-11_DYN]
lab-host-11 ansible_host=10.1.1.1

# == lab-host-12 == #
# Added with test-1.3-03_josrosa-03-26-2020_0854
[lab-host-12_DYN:vars]
ansible_network_os=ios

[lab-host-12_DYN]
lab-host-12 ansible_host=10.1.1.2

# == lab-host-21 == #
# Added with test-1.3-03_josrosa-03-26-2020_0854
[lab-host-21_DYN:vars]
ansible_network_os=nxos

[lab-host-21_DYN]
lab-host-21 ansible_host=10.2.1.1

# == lab-host-22 == #
# Added with test-1.3-03_josrosa-03-26-2020_0854
[lab-host-22_DYN:vars]
ansible_network_os=nxos

[lab-host-22_DYN]
lab-host-22 ansible_host=10.2.1.2
#DYNAMIC_DEVICES
#EOF
```

> Test Release Download

[AnsibleDynInvBuild-1.3.tar.gz](https://gitlab.healthcareit.net/netansibledeops/ansibledynamicinventorybuilder/-/blob/master/RC/TestDownloads/AnsibleDynInvBuild-1.3.tar.gz)

---

> Version 1.2

- Dynamic Inventory Builder (IOS and NXOS) - `cisco-inventory-builder.yml`
  - CSV Capable

 **1.2 CSV Headers (with cell reference numbers used in templates)**

| Header               | Definition                             | 
|----------------------|----------------------------------------| 
| Hostname (0)         | Alias or FQDN                          | 
| HostIP (1)           | IPv4/6 Address                         |
| OS (2)               | Operating System (ios/ nxos/iosxr/aci) | 


#### Example CSV

```csv
Hostname,HostIP,OS
lab-host-11,10.1.1.1,ios
lab-host-12,10.1.1.2,ios
lab-host-21,10.2.1.1,nxos
lab-host-22,10.2.1.2,nxos
```

#### Dynamic Inventory Output

```ini
[all:vars]
ansible_python_interpreter=/usr/bin/python3
ansible_connection = local

[cisco:children]
dynamic_inventory

[dynamic_inventory:children]
lab-host-11_DYN
lab-host-12_DYN
lab-host-21_DYN
lab-host-22_DYN
#DYNAMIC_GRPS

# == lab-host-11 == #
# Added with 03192020-DEVTEST_josrosa-03-19-2020_1736
[lab-host-11_DYN:vars]
ansible_network_os=ios

[lab-host-11_DYN]
lab-host-11 ansible_host=10.1.1.1

# == lab-host-12 == #
# Added with 03192020-DEVTEST_josrosa-03-19-2020_1736
[lab-host-12_DYN:vars]
ansible_network_os=ios

[lab-host-12_DYN]
lab-host-12 ansible_host=10.1.1.2

# == lab-host-21 == #
# Added with 03192020-DEVTEST_josrosa-03-19-2020_1736
[lab-host-21_DYN:vars]
ansible_network_os=nxos

[lab-host-21_DYN]
lab-host-21 ansible_host=10.2.1.1

# == lab-host-22 == #
# Added with 03192020-DEVTEST_josrosa-03-19-2020_1736
[lab-host-22_DYN:vars]
ansible_network_os=nxos

[lab-host-22_DYN]
lab-host-22 ansible_host=10.2.1.2
#DYNAMIC_DEVICES
#EOF
```

