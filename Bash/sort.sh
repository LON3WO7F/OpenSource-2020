#!/bin/bash

# test that at least one argument was passed
if [[ $# -le 0 ]]
then
    printf "Not enough arguments!\n"
    exit
fi

count=1

for arg in "$@"
do
    if [[ $arg =~ ^-?[0-9]+([0-9]+)?$ ]]
    then
        n[$count]=${arg}
        let "count += 1"
    else
        echo "$arg is not a valid integer!"
    fi
done

sort -n <(printf "%s\n" "${n[@]}")
# example: ./sort.sh 100 a 1.1 1 1 2 3 -1