#!/usr/bin/python3
import sys


def move(n):
    result = []
    backtrack(n, [], result)
    return result


def backtrack(n, path, result):
    if len(path) == n:
        result.append(path[:])
        return

    for col in range(n):
        if is_safe(col, path):
            path.append(col)
            backtrack(n, path, result)
            path.pop()


def is_safe(col, path):
    row = len(path)
    for r, c in enumerate(path):
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = sys.argv[1]

try:
    n = int(n)
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
moves = move(n)
for movement in moves:
    print(movement)
