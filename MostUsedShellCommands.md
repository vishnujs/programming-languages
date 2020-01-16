#### Performance related
- os details : cat /etc/os-release
- RAM details: cat /proc/meminfo
- cpu details: lscpu
- cpu details with vendor name:less /proc/cpuinfo
#### Details on processes on run
- processId using a port: lsof -i:9090
- get the process path: pwx pid

#### List all directories with their size in sorted manner
```
du -sh * | sort -n
```
s:summary
h:human readable
This can also be done using
```
ls| du -h --max-depth=1 | sort -n
```
