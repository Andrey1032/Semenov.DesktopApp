import math
from PySide6.QtWidgets import QMessageBox


def solve_tsp(self,distance_matrix):
        """
        Решает задачу коммивояжера методом ближайшего соседа.
        """
        start_city = 0  # Индекс стартового города
        path = nearest_neighbor(distance_matrix, start_city)
        total_distance = calculate_total_distance(path, distance_matrix)
        
        result_message = f"Минимальное расстояние: {total_distance:.2f}\n\nМаршрут: {'->'.join(map(str, [i+1 for i in path]))}"
        QMessageBox.information(self, "Решение задачи коммивояжера", result_message)

def nearest_neighbor(distances, start):
    """
    Алгоритм ближайшего соседа для задачи коммивояжера.
    Возвращает порядок посещения городов.
    """
    num_cities = len(distances)
    visited = [False] * num_cities
    current_city = start
    route = [current_city]
    visited[current_city] = True
    
    while len(route) < num_cities:
        next_city = find_nearest_unvisited(current_city, distances, visited)
        if next_city is None:
            break  # Больше маршрутов нет, останавливаемся
        route.append(next_city)
        visited[next_city] = True
        current_city = next_city
    
    # Завершающий переход назад в стартовый город
    route.append(start)
    return route

def find_nearest_unvisited(city, distances, visited):
    """
    Нахождение ближайшего неизведанного города.
    """
    best_dist = math.inf
    best_city = None
    
    for i in range(len(distances)):
        if not visited[i]:  # Город еще не посещен
            dist = distances[city][i]
            if dist > 0 and dist < best_dist:
                best_dist = dist
                best_city = i
    
    # Если не нашли подходящий город, вернем None
    return best_city

def calculate_total_distance(route, distances):
    """
    Высчитывает полную длину маршрута.
    """
    total_dist = 0
    n = len(route)
    
    for i in range(n - 1):
        city1 = route[i]
        city2 = route[i+1]
        total_dist += distances[city1][city2]
    
    return total_dist