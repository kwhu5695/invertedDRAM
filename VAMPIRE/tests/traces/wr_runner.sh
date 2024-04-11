#!/bin/bash

# Loop through each file from 1 to 128
for ((N=1; N<=128; N++)); do
    # Construct the input filename
    filename="${N}-wr.trace"

    # Construct the output filename
    output_filename="${N}-wr.csv"

    # Run the command on the file
    ../../vampire -f "modified_files_wr/${filename}" -c ../../configs/default.cfg -d WR -p ASCII -csv "wr_csvs/$output_filename"
done
