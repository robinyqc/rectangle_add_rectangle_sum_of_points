#!/usr/bin/bash

test_case=0

touch "brute_force.cpp"
make brute_force
touch "$1.cpp"
make $1

while [ "$test_case" -lt $2 ]; do
    python gen.py 5000 5000 1000000000 1000000000 998244353 0 1 2 3 > small.in
    ./brute_force < small.in > small.ans
    ./$1 < small.in > small.out
    if ! diff -w small.out small.ans > /dev/null; then
        echo "wa!"
        exit -1
    fi
    echo "OK on test $test_case."
    test_case=$((test_case + 1))
done
