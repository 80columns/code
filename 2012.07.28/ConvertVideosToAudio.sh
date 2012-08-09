#!/bin/bash

# Global variables
VIDEOS="videos"
BITRATE="256000"
NUM_VIDEOS=`ls -l "$VIDEOS/" | grep -v 'total' | wc -l`

# Create the output directory in case it doesn't already exist
mkdir -p audio

# Hide the cursor
tput civis

# Video number counter
video_num="1"
for v in $VIDEOS/*
do
    # The $audio_time variable is split into four sections:
    # ww:xx:yy:zz
    #
    # ww: Hours
    # xx: Minutes
    # yy: Seconds
    # zz: Hundrethds of a second
    audio_time=`ffprobe "$v" 2>&1 | grep 'Duration' | \
                sed -e 's/,.*//g' | sed -e 's/  Duration: //g' | \
                tr "." ":"`

    # This splits $audio_time into an array using ':' as an element
    # separator
    audio_time_array=(${audio_time//:/ })

    # This stores the total audio length in seconds in
    # $audio_time_seconds
    audio_time_seconds=`echo "scale=2;
                        (${audio_time_array[3]} * 0.01) + \
                        ${audio_time_array[2]} + \
                        (${audio_time_array[1]} * 60) + \
                        (${audio_time_array[0]} * 3600)" | bc`

    filesize_bytes=`echo "($BITRATE * $audio_time_seconds) / 8" | \
                    bc | sed -e 's/\..*//g'`

    # Put the output file in the current directory
    output_file=`echo "$v" | sed -e "s/$VIDEOS\///g"`
    output_file=`echo "$output_file" | sed -e 's/\.mp4//g'`
    output_file=`echo "$output_file" | sed -e 's/\.flv//g'`
    output_file="audio/$output_file.mp3"

    # Show the user a progress bar for the conversion
    ./MonitorProgress.sh "$output_file" "$filesize_bytes" \
                         "$video_num" "$NUM_VIDEOS" &

    # Get the PID of the MonitorProgress.sh process
    background_pid=$!

    # Launch the conversion process
    ffmpeg -i "$v" -ab $BITRATE -f mp3 "$output_file" 2>/dev/null

    # End the MonitorProgress.sh process and wait for it to exit
    kill $background_pid
    sleep 1

    # Increment the video number
    video_num=`echo "$video_num + 1" | bc`
done

# Show the cursor
tput cnorm

exit 0
