f = {}
g = {}

for n in range(1,50_000):
    if n < 28:
        g[n] = 3*n-4
    if n >= 28:
        g[n] = g[n-5] - 15

for n in range(50_000,1,-1):
    if n < 31054:
        f[n] = f[n+4] + 3020
    if n >= 31054:
        f[n] = 3 * (g[n-2] - 15)

print(f[15])
