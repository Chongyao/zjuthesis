#!/bin/bash
for file in $(ls *.png)
do
    echo $file
    convert -trim -transparent white $file $file
done