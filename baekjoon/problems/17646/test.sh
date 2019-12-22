#!/bin/bash

EXEC_FILENAME=$1
OUTPUT_FILENAME=$2
START=$3
END=$4

rm -f $OUTPUT_FILENAME

for ((i = $START; i <= $END; ++i))
do
    echo $i >> $OUTPUT_FILENAME
    echo $i | { time $EXEC_FILENAME; } >> $OUTPUT_FILENAME 2>&1
    echo -e '\n' >> $OUTPUT_FILENAME
done
