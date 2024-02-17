list = [2, 53, 832, -342, 452, -53.5, 64]

lam_sort = lambda list: sorted(list)
lam_lenght = lambda list: len(list)
lam_sort_reverse = lambda list: sorted(list,reverse=True)
def sor(list,func):
    return func(list)

print(sor(list,lam_sort))
print(sor(list, lam_lenght))
print(sor(list, lam_sort_reverse))

print(sor(list, lambda list: sorted(list)))