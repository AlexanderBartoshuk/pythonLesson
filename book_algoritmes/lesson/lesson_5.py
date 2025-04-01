book = dict() # пустая хэш-таблица

book["apple"] = 0,67
book['авокадо'] = 0,35
book['молоко'] = 0,35

print(book)
print(book["apple"])

voter = {}
def check_voter(name):
    if voter.get(name):
        print(f"Kick {name} out")
    else:
        voter[name] = True
        print(f"let {name} to vote")
check_voter('Alexander')


#кэширование
catche = {}
def get_page(url):
    if catche.get(url):
        return catche[url]
    else:
        data = get_data_from_server(url) # type: ignore
        catche[url] = data
        return data

def main(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])
print(main([2,4,6]))

def число(list):
    a = sorted(list)
    return a[-2]
print(число([0,3,5,7,4,100]))






