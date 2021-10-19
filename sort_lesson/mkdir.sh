#!/bin/bash
# File will create dirs and files {docx, xlsx} with some size
FILE_SIZE=1
for i in {1..3}
do
    echo $i
    mkdir "test$i"
    for j in {1..300}
    do
        head -c ${FILE_SIZE}M </dev/urandom > test$i/file-docx-$j.docx
        head -c ${FILE_SIZE}M </dev/urandom > test$i/file-xlsx-$j.xlsx
    done
done
# simple for: 4 dirs with 600 files each 2M
# Start in folder test1
# Start in folder test2
# Start in folder test3
# Start in folder test4
# 0.5133495330810547

# MultiThreads: 4 dirs with 600 files each 2M
# Start in folder test1
# Start in folder test2
# Start in folder test4
# Start in folder test3
# 0.21183156967163086