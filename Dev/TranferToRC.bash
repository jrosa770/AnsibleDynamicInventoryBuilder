#!/usr/bin/env bash
echo -e "\e[0m========================================================================================"
echo -e "\e[32mCreate new Version of the Playbook into RC"
echo -e "\e[0m========================================================================================"

echo -n "Source Dev Playbook Version (Example: 1.1): "
read Dev

echo -n "New RC Playbook Version (Example: 1.2): "
read RC

cp -R $Dev ../RC/$RC

ls -la ../RC/$RC
