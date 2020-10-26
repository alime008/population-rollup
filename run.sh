#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python 3.7. Remember that in order to execute the following command, you need to uncomment the line

SCRIPT_PATH="./src/population.py" 
INPUT_PATH="./input/censustract-00-10.csv" 
OUTPUT_PATH="./output/report.csv"
PYTHON=python3

# call script via the interrupter     
$PYTHON $SCRIPT_PATH $INPUT_PATH $OUTPUT_PATH