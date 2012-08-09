#!/bin/bash

# This function is executed when the audio file conversion is
# finished
function on_completion()
{
    echo -ne "[==============================] (100%)\t"
    echo -ne "($file_num/$num_total_files)\t[ $output_file ]\r\n"
    exit 0
}

# This function traps the SIGTERM signal that the script gets
# from ConvertVideoToAudio.sh
trap on_completion SIGTERM

# Get the arguments passed to the script
output_file=$1
filesize_bytes=$2
file_num=$3
num_total_files=$4

# While the audio file doesn't yet exist, wait for it to be created
while [[ ! -e "$output_file" ]]
do
        sleep 1
done

# Loop infinitely until the script receives a SIGTERM signal from
# ConvertVideoToAudio.sh
while :
do
    # Get the current size of the file
    current_file_bytes=`ls -l "$output_file" | awk '{print $5}'`

    # Get the ratio of the output file to its projected size as a
    # percent
    percent=`echo "scale=2; ($current_file_bytes / $filesize_bytes) \
             * 100" | bc | sed -e 's/\..*//g'`

    # Don't print 100% until the audio file is actually finished
    if [[ "$percent" -ge 100 ]]
    then
        percent='99'
    fi

    # Print the first part of the output
    echo -ne "["

    # Calculate the number of bars to print (=)
    num_bars=`echo "scale=2; 30 * ($percent / 100)" | bc | \
              sed -e 's/\..*//g'`
    if [[ -z $num_bars ]]
    then
        num_bars="0"
    fi

    # Calculate the number of dashes to print (-)
    num_dashes=`echo "30 - $num_bars" | bc | sed -e 's/\..*//g'`

    # Print out $num_bars bars
    until [[ "$num_bars" -eq 0 ]]
    do
        echo -ne "="
        let "num_bars = $num_bars - 1"
    done

    # Print out $num_dashes dashes
    until [[ "$num_dashes" -eq 0 ]]
    do
        echo -ne "-"
        let "num_dashes = $num_dashes - 1"
    done

    # Print the audio file completion information
    echo -ne "] (${percent}%)\t($file_num/$num_total_files)\t[ "
    echo -ne "$output_file ]\r"

    # Sleep for 1 second
    sleep 1
done
