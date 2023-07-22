#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fib_seq = list()
        print(fib_seq)
    elif length == 1:
        fib_seq = list([0])
        print(fib_seq)
    elif length > 1:
        fib_seq = list([0, 1])
        for int in range(length - 2): 
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        print(fib_seq)