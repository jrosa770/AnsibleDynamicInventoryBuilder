#!/usr/bin/env bash
echo -e "\e[0m========================================================================================"
echo -e "\e[32mCreate new Version"
echo -e "\e[0m========================================================================================"

echo -n "Source Playbook Version (Example: 1.1): "
read Old

echo -n "New Playbook Version (Example: 1.2): "
read New

cp -R $Old $New

ls -la $New/
