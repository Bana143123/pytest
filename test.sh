#!/bin/bash
echo "Hello world!"
cd pytest_tut
pwd
ls
if [ -d "HL" ];
then
    echo "Directory already exists"
else
    echo "Directory created"
    mkdir HL
fi
cd HL
touch narendra.txt
#nano narendra.txt
cat narendra.txt
