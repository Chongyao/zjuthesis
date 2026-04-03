#!/bin/bash
for file in $(ls *.png)
do
    echo $file
    convert  -transparent white $file $file
done
