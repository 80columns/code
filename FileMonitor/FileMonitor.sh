#!/bin/bash

function Help {
    # Display the help message
    echo "FileMonitor v1.0"
    echo "Usage:"
    echo "-h or --help to view this message"
    echo "-a or --add [file(s)] to add files to the database"
    echo "-c or --check [file(s)] to check files present in" \
         "the database"
}

# Add a file or folder to the database
function AddFile {
    # If this function instance is being called by AddFile,
    # reset the IFS variable
    if [[ $IFS == '\n' ]]
    then
        IFS=$' \t\n'
    fi

    # Get the full path of the file
    FilePath=`realpath $1`

    # If the argument is a regular file, process it
    if [[ -f $FilePath ]]
    then
        FileHash=`sha256sum $FilePath | awk '{print $1}'`

        # If the file path is in the database, check whether its
        # database hash is consistent with the current hash
        grep -F "$FilePath" fm.db 1>/dev/null
        if [[ "$?" -eq 0 ]]
        then
            # Check whether the database hash is consistent with
            # the file's current hash
            grep -P "$FileHash\t$FilePath" fm.db 1>/dev/null
            if [[ "$?" -eq 0 ]]
            then
                # The hashes match
                echo "$FilePath and its current hash are already" \
                     "present in the database"
            else
                # The hashes do not match, and the old hash is
                # overwritten with the new one
                echo "Warning! The hash for $FilePath has changed,"
                     "updating the database with new hash"

                # Remove the old file/hash pair in the database
                # and insert the new one
                sed -i \
                    "/$(echo $FilePath | sed -e 's/\//\\\//g')/d" \
                    fm.db
                FileString="$FileHash\t$FilePath"
                echo -e $FileString >> fm.db
            fi

        # If the file path is not in the database, insert the path
        # and the hash
        else
            FileString="$FileHash\t$FilePath"
            echo -e $FileString >> fm.db
        fi

    # If the argument is a directory, call AddFile on its children
    elif [[ -d $FilePath ]]
    then
        IFS=$'\n'
        for f in `ls "$FilePath/"`
        do
            AddFile "$FilePath/$f"

            # http://tldp.org/LDP/abs/html/localvar.html
            # This is documented in the Bash manual:
            # "Local can only be used within a function; it makes the
            # variable name have a visible scope restricted to that
            # function *and its children*." [emphasis added]
            # The ABS Guide author considers this behavior to be a
            # bug.
            #
            #  The fact that local variable names are visible to a
            # function's children means that when AddFile is called
            # recursively, the child instance's $FilePath and the
            # parent instance's $FilePath refer to *the same
            # variable* in memory. So even if we just pased a single
            # file recursively to AddFile, it will run as its first
            # statement:
            #
            #  FilePath=`realpath $f`
            #
            #  Which, evidently, changes the value of FilePath *here*
            # as well. As one may imagine, this leads to errors such
            # as "/directory/a/b is not a valid file", where a and
            # b are both files inside directory, and a is added to
            # the database first. After a is added to the database,
            # $FilePath is set to /directory/a, and then the function
            # call AddFile /directory/a/b is made, which results in
            # an error.
            #  The one and only solution [that I've found so far] is
            # the fact that parameters remain unchanged in a
            # recursive function call. As a result, both the caller
            # and the callee have their own set of $1, $2, and so
            # on. Thus the original path of the file to process is
            # still in $1, so we reset $FilePath here to its original
            # value.
            FilePath=`realpath $1`
        done
        IFS=$' \t\n'

    # If the argument is neither a regular file or a directory, print
    # an error
    else
        echo "Error: $FilePath does not represent a valid file"
    fi

    # Reset the IFS variable in case this function was called
    # by AddFile
    IFS=$'\n'
}

# Check whether a file or folder is present in the database
function CheckFile {
    # If this function instance is being called by AddFile,
    # reset the IFS variable
    if [[ $IFS == '\n' ]]
    then
        IFS=$' \t\n'
    fi

    # Get the full path of the file
    FilePath=`realpath $1`

    # If the argument is a regular file, process it
    if [[ -f $FilePath ]]
    then
        FileHash=`sha256sum $FilePath | awk '{print $1}'`

        # If the file path is in the database, check whether its
        # database hash is consistent with the current hash
        grep -F "$FilePath" fm.db 1>/dev/null
        if [[ "$?" -eq 0 ]]
        then
            # Check whether the database hash is consistent with
            # the file's current hash
            grep -P "$FileHash\t$FilePath" fm.db 1>/dev/null
            if [[ "$?" -eq 0 ]]
            then
                # The hashes match - don't print anything here,
                # otherwise running the script would take much
                # longer
                :
            else
                # The hashes do not match
                echo "Warning! The hash for $FilePath has changed" \
                     "since it was added to the database"
            fi

        # If the file path is not in the database, let the user know
        else
            echo "Warning! $FilePath is not present in the database"
        fi

    # If the argument is a directory, call CheckFile on its children
    elif [[ -d $FilePath ]]
    then
        IFS=$'\n'
        for f in `ls "$FilePath/"`
        do
            CheckFile "$FilePath/$f"
            FilePath=`realpath $1`
        done
        IFS=$' \t\n'

    # If the argument is neither a regular file or a directory, print
    # an error
    else
        echo "Error: $FilePath does not represent a valid file"
    fi

    # Reset the IFS variable in case this function was called
    # by AddFile
    IFS=$'\n'
}

# Check here for the parameter (-a or --add, -c or --check,
# -h or --help)
if [[ $1 = "-a" || $1 = "--add" ]]
then
    # Make sure that the database exists, and if it doesn't,
    # create it
    if [[ ! -f fm.db ]]
    then
        touch fm.db
    fi

    # Pass the rest of the command line arguments to the AddFile
    # function
    j=0
    for i in "$@"
    do
        if [[ $j -ne 0 ]]
        then
            AddFile "$i"
            if [[ $IFS == '\n' ]]
            then
                IFS=$' \t\n'
            fi
        else
            j=$(($j + 1))
        fi
    done

    # Exit with a success status
    exit 0

elif [[ $1 = "-c" || $1 = "--check" ]]
then
    # Make sure that the database exists, and if it doesn't,
    # tell the user that there is no database to check files
    # against
    if [[ ! -f fm.db ]]
    then
        echo "Error: No database exists to check files against." \
             "Please initialize the database first by adding files" \
             "to it with the -a or --add flag"
    fi

    # Pass the rest of the command line arguments to the CheckFile
    # function
    j=0
    for i in "$@"
    do
        if [[ $j -ne 0 ]]
        then
            CheckFile "$i"
            if [[ $IFS == '\n' ]]
            then
                IFS=$' \t\n'
            fi
        else
            j=$(($j + 1))
        fi
    done

    # Exit with a success status
    exit 0

elif [[ $1 = "-h" || $1 = "--help" ]]
then
    # Display the help message
    Help

    # Exit with a success status
    exit 0

else
    # Print an error message if there are no recognizable arguments
    echo -e "Error: Please specify an operation to perform\n"

    # Display the help for the user
    Help

    # Exit with a non-success status
    exit 1
fi
