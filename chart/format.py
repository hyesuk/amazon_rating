#!/usr/bin/python

for line in open("result.txt"):
    cols = line.split(",")
    label = cols[0]
    z = cols[1]
    x = cols[2]
    y = cols[3].strip()
    print "{ x: %s, y: %s, z: %s, label: \"%s\" }," % (x,y,z,label)
