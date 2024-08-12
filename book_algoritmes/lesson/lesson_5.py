# поиск в ширину 
from collections import deque


graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuji","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ['thom',"jony"]
graph["anuji"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jony"] = []

"""
search_queue = deque()
search_queue += graph["you"]
"""
def person_is_seller(name):
    return name[-1] == "m"
"""
def method(search_queue):
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(f"{person} является продавцом фруктов")
            return True
        else:
            search_queue += graph[person]
    return False
"""


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")