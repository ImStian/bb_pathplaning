import heapq
import numpy as np
from image_conversion import generate_pixelmap
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt



def astar(start, end, binary_map):
    def heuristic(node):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

    def get_neighbors(node):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor = (node[0] + i, node[1] + j)
                if 0 <= neighbor[0] < len(binary_map) and 0 <= neighbor[1] < len(binary_map[0]) and binary_map[neighbor[0]][neighbor[1]] == 0:
                    neighbors.append(neighbor)
        return neighbors

    heap = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if current_node == end:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current_node):
            new_cost = cost_so_far[current_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(heap, (priority, neighbor))
                came_from[neighbor] = current_node

    return None  # If no path is found

def generate_image_with_path(binary_map, waypoints, output_image_path):
    plt.imshow(binary_map, cmap='gray')

    for point in waypoints:
        plt.scatter(point[1], point[0], color='red')

    plt.savefig(output_image_path)
    plt.show()

# Example usage:
test = 1

if test == 0:
    start_point = (0, 0)
    end_point = (40, 40)
    binary_map = generate_pixelmap("desolate_grid_smile.png")
elif test == 1:
    start_point = (100, 100)
    end_point = (2200, 2200)
    binary_map = generate_pixelmap("grid_image.png")



path = astar(start_point, end_point, binary_map)

if path:
    generate_image_with_path(binary_map, path, 'path_image.png')
    print("Path found:", path)
else:
    print("No path found.")
