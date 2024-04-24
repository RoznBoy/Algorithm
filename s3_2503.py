from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())

baseball=list(permutations([1,2,3,4,5,6,7,8,9],3))
for _ in range(N):
    q, s, b  = map(int, input().split())