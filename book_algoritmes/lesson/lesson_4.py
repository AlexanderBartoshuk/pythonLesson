book = dict()

book["apple"] = 0,67
#print(book)
#print(book["apple"])

voter = {}
def check_voter(name):
    if voter.get(name):
        print(f"Kick {name} out")
    else:
        voter[name] = True
        print(f"let {name} to vote")

#кэширование 
catche = {}
def get_page(url):
    if catche.get(url):
        return catche[url]
    else:
        data = get_data_from_server(url) # type: ignore
        catche[url] = data
        return data


 
