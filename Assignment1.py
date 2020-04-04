#!/usr/bin/env python
# Function for nth Fibonacci number

import argparse

def Fib(n, f = None):
    r = 0
    if n == 1:
        r = 0
    elif n == 2:
        r = 1
    else:
        r = (Fib(n - 1, f) + Fib(n - 2))
    if f != None:
        f.write(str(r) + ' ')
    return r




def main():
    print("Enter Main")
    # Create argparse
    parser = argparse.ArgumentParser(description="Computes to the nth term of the Fibonacci sequence")
    # Add an argument
    parser.add_argument("num", type=int, help='Enter a number to compute the nth term')
    parser.add_argument("-o", "--output", action="store_true")
    # Assign the argument to a variable
    args = parser.parse_args()
    print("Args: ", args)
    # Call the fib function and assign the return value to a variable
    result = Fib((args.num))
    print("Calculation finished: ", result)
    if args.output:
        print("Open file to save")
        f = open("Fibonacci.txt", "a")
        print("File is open")
        Fib(args.num, f)

if __name__ == "__main__":
    main()
