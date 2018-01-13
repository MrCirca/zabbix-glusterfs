#!/usr/bin/python3
import json
import subprocess
import sys

gluster_volume_names = []
gstatus_output = subprocess.check_output('gstatus -a -o json ', shell=True).decode()
date, time, json_part = gstatus_output.split(maxsplit=2)
gluster_info = json.loads(json_part)
volume_list = gluster_info["volume_summary"]

nargs = len(sys.argv)

if nargs == 1:
    for volume in volume_list:
        gluster_volume_names.append({"{#VOLUME_NAME}": volume["volume_name"]})
    print(json.dumps({'data': gluster_volume_names}))

elif nargs == 2:
    print(gluster_info[sys.argv[1]])
elif nargs == 3:
    for volume in volume_list:
        if volume.get('volume_name') and sys.argv[2] == volume["volume_name"]:
            print(volume[sys.argv[1]])
            break
    else:
        if sys.argv[1] == "state":
            print('down')
        else:
            print()
        
else:
    print('Wrong arguments')

