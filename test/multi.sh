#!/bin/bash
#multi.sh

mkdir Films Serie Vrac
cd Films
../create.pl -type="movie"
cd ..
cd Serie
../create.pl -type="serie"
cd ..
cd Vrac
../create.pl
cd ..
cp -f films.csv Films
#cp -f films.csv Serie
cp -f films.csv Vrac
