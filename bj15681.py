import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, r, q = map(int, input().split())

g = [[] for _ in range(n + 1)]
d = [0 for _ in range(n + 1)]

def f(x, p):
    d[x] = 1

    for i in g[x]:
        if i != p:
            d[x] += f(i, x)

    return d[x]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

f(r, r)

for _ in range(q):
    n = int(input())
    print(d[n])