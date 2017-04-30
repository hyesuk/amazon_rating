#!/bin/bash
for i in $(ls *.csv); do
    ./analyze.py $i 10
done