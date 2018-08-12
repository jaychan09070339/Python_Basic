#!/usr/bin/python
IP="0xc0a80164"
MASK="0xFFFFFF00"
ip=int(IP,16)
mask=int(MASK,16)
print("ip:",ip,"mask:",mask)
print("IP&MASK:",ip&mask)
print("IP|~MASK",ip|~mask)
