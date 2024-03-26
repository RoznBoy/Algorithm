import sys
input = sys.stdin.readline

n, m = map(int,input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))
print(queen, knight, pawn)