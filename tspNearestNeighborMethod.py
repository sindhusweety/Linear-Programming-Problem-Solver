'''
 Implementing Nearest Neighbor Heuristic to solve Traveling Salesman problems
'''

def tspNearestNeighborHeuristic(cities, distance):

    visited = []
    minimum_distance_traveled = []
    neighbor = 'A'

    neighbor_index = cities.index(neighbor)
    unvisited_neighbour_distance = [__i for __i in distance[neighbor_index] if __i > 0]
    minimum_distance = min(unvisited_neighbour_distance)
    visited_neighbor_distance = list()
    visited_neighbor_distance.append(0)

    while neighbor not in visited:
        visited.append(neighbor)
        minimum_distance_traveled.append(minimum_distance)
        neighbor = cities[distance[neighbor_index].index(min(unvisited_neighbour_distance))]
        neighbor_index = cities.index(neighbor)
        before_visited_neighbor_index = cities.index(neighbor)
        visited_neighbor_distance.append(distance[neighbor_index][before_visited_neighbor_index])
        unvisited_neighbour_distance = [__i for __i in distance[neighbor_index] if __i not in visited_neighbor_distance]
        minimum_distance = min(unvisited_neighbour_distance)
        no_cities = 1
        if neighbor not in visited:
            no_cities = 2
            visited.append(neighbor)

        while neighbor in visited and no_cities < len(cities):
            visited_neighbor_index = cities.index(neighbor)
            visited_neighbor_distance.append(distance[neighbor_index][visited_neighbor_index])
            unvisited_neighbour_distance = [__i for __i in distance[neighbor_index] if __i not in visited_neighbor_distance]
            neighbor = cities[distance[neighbor_index].index(min(unvisited_neighbour_distance))]
            minimum_distance = min(unvisited_neighbour_distance)
            no_cities += 1
    neighbor_index = cities.index(visited[-1])
    minimum_distance_traveled.append(distance[neighbor_index][0])
    print('Shortest route : ', " -> ".join(visited))
    for _i in range(len(visited)):
        print("City "+visited[_i]+"'s Nearest Neighbor's Distance is ",minimum_distance_traveled[_i] )
    print("total traveled distance: ", sum(minimum_distance_traveled))


cities = ['A', 'B', 'C', 'D', 'E']
distance = [[0, 132, 217, 164, 58],
            [132, 0, 290, 201, 79],
            [217, 290, 0, 113, 303],
            [164, 201, 113, 0, 196],
            [58, 79, 303, 196, 0]]
tspNearestNeighborHeuristic(cities, distance)