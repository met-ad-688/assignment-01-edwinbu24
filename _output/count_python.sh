#!/bin/bash

DATA_DIR=".."

count=$(grep -i "python"  "$DATA_DIR"/question_tags.csv "$DATA_DIR"/questions.csv | wc -l)
echo "Number of lines containing 'python' in CSV files: $count"

