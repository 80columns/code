#!/bin/bash

# http://projecteuler.net/problem=22
#
# Using names.txt (http://projecteuler.net/project/names.txt), a 46K
# text file containing over five-thousand first names, begin by
# sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
# list. So, COLIN would obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?

# Echo the answer by performing Bash arithmetic and command
# substitution. First cat the input file, then replace all commas with
# newlines so that each name is on one line. Then, sort the file
# alphabetically. Pass the result of sort to cat to place line numbers
# at the beginning of each line. Remove the spaces from the beginning
# of each line, and replace the tab + " with a multiplication sign and
# left parenthesis. Append a right parenthesis to the end of each
# line. Next, replace each character with its numeric value with a
# space on both sides of the number. Then remove the extra spaces
# directly next to the left and right parentheses. Replace each
# occurrence of two spaces with a plus sign with a single space on
# both sides. Add an extra right parenthesis and plus sign at the end
# of each line. Add an extra left parenthesis at the beginning of each
# line. Finally, remove all newlines and remove the extra plus sign
# with spaces from the end of the resulting output. The output is then
# passed to Bash's arithmetic calculator and evaluated.
echo $(( $(cat names.txt | tr ',' '\n' | sort | cat -n | \
           sed -e 's/^ *//g' -e 's/\t\"/ * (/g' -e 's/\"/)/g' \
               -e 's/A/ 1 /g' -e 's/B/ 2 /g' -e 's/C/ 3 /g' \
               -e 's/D/ 4 /g' -e 's/E/ 5 /g' -e 's/F/ 6 /g' \
               -e 's/G/ 7 /g' -e 's/H/ 8 /g' -e 's/I/ 9 /g' \
               -e 's/J/ 10 /g' -e 's/K/ 11 /g' -e 's/L/ 12 /g' \
               -e 's/M/ 13 /g' -e 's/N/ 14 /g' -e 's/O/ 15 /g' \
               -e 's/P/ 16 /g' -e 's/Q/ 17 /g' -e 's/R/ 18 /g' \
               -e 's/S/ 19 /g' -e 's/T/ 20 /g' -e 's/U/ 21 /g' \
               -e 's/V/ 22 /g' -e 's/W/ 23 /g' -e 's/X/ 24 /g' \
               -e 's/Y/ 25 /g' -e 's/Z/ 26 /g' -e 's/( /(/g' \
               -e 's/ )/)/g' -e 's/  / + /g' -e 's/$/) + /g' \
               -e 's/^/(/g' | \
           tr -d '\n' | sed -e 's/ + $//g') ))
