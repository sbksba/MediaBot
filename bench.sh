#!/bin/bash
#bench.sh

dir=$(pwd)
echo "## BENCH ##"
echo ""
echo "Create the configuration file"
echo $dir"/test/Vrac"   > $dir/config/config_test.txt
echo $dir"/test/Films" >> $dir/config/config_test.txt
echo $dir"/test/Serie" >> $dir/config/config_test.txt
echo "Create directories and files test"
cd test
./multi.sh
cd ..
echo "Run the test"
./launch.sh
