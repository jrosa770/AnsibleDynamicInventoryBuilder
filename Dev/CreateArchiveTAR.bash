#!/usr/bin/env bash
NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
#	FUNCTIONS 
delete_source () {
if [ "$DeleteSource" == "y" ]; then
echo -e "${Green} Deleting "$Version"/"
rm -drf $Version
echo -e "${NOCOLOR}"
else
echo -e "${RED}Leaving " $Version"/ in place"
echo -e "${NOCOLOR}"
fi
}
## EXIT ROUTINE
exit_message () {
	echo -e "Thank You For Playing." && echo && sleep 2 && echo -e "${ORANGE}Goodbye${NOCOLOR}" ${BLUE}"===" $USER "==="${NOCOLOR} && echo && sleep 2
}

echo -e "${NOCOLOR}======================================================================================="
echo -e "${Green}Create new Test TAR.GZPackage"
echo -e "${NOCOLOR}======================================================================================="

echo -n "Source Playbook Version (Example: 1.1): "
read Version

tar -czvf AnsibleACIBuilds-$Version-plus_archive.tar.gz $Version

echo -e "${Green}AnsibleACIBuilds-"$Version"_plus-archive.tar.gz Completed"
echo -e "${NOCOLOR}"

echo -e "${Green}AnsibleACIBuilds-"$Version"_plus-archive.tar.gz Contents"
echo -e "${NOCOLOR}"

tar -ztvf AnsibleACIBuilds-$Version-plus_archive.tar.gz

echo -n "Delete Source Folder? (y/n): "
read DeleteSource

delete_source

exit_message