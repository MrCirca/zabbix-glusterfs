# Gluster Storage - Zabbix

This project was created to monitor Gluster Storage with Zabbix.
In this repository there are two files.
One python script that calls [gstatus](https://github.com/gluster/gstatus), discovering gluster volumes and print data we want, according to the arguments given.
You have to install gstatus [gstatus](https://github.com/gluster/gstatus)

You should save the script in any directory you want, in order to do it executable from zabbix user using sudo.
You have to create a file in /etc/zabbix/zabbix_server.conf.d/ and add UserParameters:

* You should save the script in any directory you want, do it executable from zabbix user using sudo.
* You have to create a file in /etc/zabbix/zabbix_server.conf.d/ and add UserParameters:
 * UserParameter=gluster_volume_info[\*],sudo /path/gstatus_discovery.py $1 $2
 * UserParameter=gluster_storage_info[\*],sudo /path/gstatus_discovery.py $1
 * UserParameter=gluster_volume_info,sudo /path/gstatus_discovery.py
* The last one shoud be import zabbix_template.xml in zabbix

### Examples executing script
Giving no arguments
```
root@gfs1:/opt# ./gstatus_discovery.py
{"data": [{"{#VOLUME_NAME}": "gv0"}, {"{#VOLUME_NAME}": "gv1"}]}
```

Giving one argument
```
./gstatus_discovery.py nodes_active
2
```
```
./gstatus_discovery.py usable_capacity
37423202304
```

Giving two arguments and last should be volume name
```
./gstatus_discovery.py used_capacity gv0
3235531434
```

