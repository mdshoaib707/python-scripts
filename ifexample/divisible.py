#!/usr/bin/env python

import sys

number = int(sys.argv[1])

for fb in range(number):
    newnumber = fb+1
    div3 = div5 = 0

    div3 = newnumber % 3
    div5 = newnumber % 5

    if div3 == 0 and div5 == 0:
        print("FizzBuzz")
    elif div3 == 0:
        print("Fizz")
    elif div5 == 0:
        print("Buzz")
    else:
        print(newnumber)

