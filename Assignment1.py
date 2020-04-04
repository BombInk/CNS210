#!/usr/bin/env python
# Function for nth Fibonacci number

import argparse

def Fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)




def main():
    # Create argparse
    parser = argparse.ArgumentParser(description="Computes to the nth term of the Fibonacci sequence")
    # Add an argument
    parser.add_argument("num", type=int, help='Enter a number to compute the nth term')
    parser.add_argument("-o", "--output", action="store_true")
    # Assign the argument to a variable
    args = parser.parse_args()
    # Call the fib function and assign the return value to a variable
    result = Fib((args.num))
    if args.output:
        f = open("Fibonacci.txt", "a")
        f.write(str(result) + '\n')

if __name__ == "__main__":
    main()