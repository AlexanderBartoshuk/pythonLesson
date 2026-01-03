def Win(n, m):
    return 0 if m <= 537 else any([Lose(n-1, m-4),  Lose(n-1, m//5)])
def Lose(n, m):
    return 1 if m <= 537 else 0 if not n else\
           any([Win(n-1, m-4),  Win(n-1, m//5)])
print('19)', max(m for m in range(537, 100000) if not Win(1, m) and Lose(2, m)))

def Win(n, m):
    return 0 if m <= 537 else any([Lose(n - 1, m - 4), Lose(n - 1, m // 5)])

def Lose(n, m):
    return 1 if m <= 537 else 0 if not n else \
        all([Win(n - 1, m - 4), Win(n - 1, m // 5)])

print('20)', *[m for m in range(537, 100000) if not Win(1, m) and Win(3, m)][:2])
print('21)', min(m for m in range(538, 100000) if not Lose(2, m) and Lose(4, m)))