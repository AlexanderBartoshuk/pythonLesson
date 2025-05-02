# Список нужных штатов
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

# Словарь станций с покрытиями
stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}

# Итоговые станции
final_stations = []

# Пока есть необходимые штаты
while states_needed:
    best_station = None
    states_covered = set()
    
    # Проходим по каждой радиостанции
    for station, coverage in stations.items():
        covered = states_needed & coverage  # Пересечение множеств
        
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            
    # Обновляем оставшиеся штаты
    states_needed -= states_covered
    
    # Добавляем лучшую станцию в финальный список
    final_stations.append(best_station)

# Результат вывода
print(final_stations)

