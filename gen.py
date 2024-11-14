#!/usr/bin/pypy3

import random as rd
import argparse as agp

parser = agp.ArgumentParser(description="Generate a random test case.")

parser.add_argument('N', type=int, help='Number of initial points.')
parser.add_argument('Q', type=int, help='Number of queries.')
parser.add_argument('X', type=int, nargs='?', default=10**9, help='Range of coord x.')
parser.add_argument('Y', type=int, nargs='?', default=10**9, help='Range of coord y.')
parser.add_argument('W', type=int, nargs='?', default=998244352, help='Range of initial weight.')
parser.add_argument('-OP', nargs='*', default=[0, 1, 2, 3], help='Type of operations.')

args = parser.parse_args()

N = args.N
Q = args.Q
X = args.X
Y = args.Y
W = args.W
OP = list(map(int, args.OP))

assert set(OP).issubset({0, 1, 2, 3})

n = rd.randint(1, N)
q = rd.randint(1, Q)

print(n, q)

size = n

for _ in range(n):
    print(rd.randint(0, X), rd.randint(0, Y), rd.randint(0, W))

for _ in range(q):

    op = rd.choice(OP)

    print(op, end=' ')

    if op == 0:
        print(rd.randint(0, X), rd.randint(0, Y), rd.randint(0, W))
        size += 1

    elif op == 1:
        print(rd.randrange(0, size), rd.randint(0, W))

    else:
        l = rd.randint(0, X)
        r = rd.randint(0, X)
        while l == r:
            l = rd.randint(0, X)
            r = rd.randint(0, X)

        d = rd.randint(0, Y)
        u = rd.randint(0, Y)
        while d == u:
            d = rd.randint(0, Y)
            u = rd.randint(0, Y)

        if l > r:
            l, r = r, l
        if d > u:
            d, u = u, d
        
        if op == 2:
            print(l, d, r, u)
        else:
            print(l, d, r, u, rd.randint(0, W), rd.randint(0, W))