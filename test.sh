#!/bin/bash

./clean.sh
cd Downloads
../create.pl
cd -
python Main.py
