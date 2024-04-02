#! /bin/bash

logfile_path=$1
echo $logfile_path
df -h | awk '{print $1,$(NF-1),$NF }' > $logfile_path