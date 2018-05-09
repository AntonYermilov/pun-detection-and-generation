#!/bin/bash

for (( i = 1; i <= 40; i++ ))
do
    ./classifier.py $i &
done
