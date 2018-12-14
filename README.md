# Gluster Storage - Zabbix
![Zabbix Glusterfs](https://i.imgur.com/K7OP7uM.png)


This project was created to monitor Gluster Storage with Zabbix.
In this repository there are two files.
One python script that calls [gstatus](https://github.com/gluster/gstatus), discovering gluster volumes and print data we want, according to the arguments given.
You have to install gstatus [gstatus](https://github.com/gluster/gstatus)

You should save the script in /usr/local/bin/ and do it executable. Use visudo and give privileges to zabbix user.
```
visudo
```
Paste the following line!
```
zabbix ALL=(ALL) NOPASSWD: gstatus_discovery.py
```
You have to add glusterfs.conf file in /etc/zabbix/zabbix_agent.conf.d/

* You should save the script in /usr/local/bin directory and do it executable from zabbix user using sudo.
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
*Zabbix Template was made for Zabbix 3.4.*

*Zabbix 4.0 Supported (Tested)*
