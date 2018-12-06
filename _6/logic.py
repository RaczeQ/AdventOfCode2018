def load_coordinates(data):
    points = []
    for line in data:
        cooridinates = line.split(',')
        points.append((int(cooridinates[0]), int(cooridinates[1])))
    return points

def get_coordinate_ranges(cooridinates):
    x_list = [c[0] for c in cooridinates]
    y_list = [c[1] for c in cooridinates]
    return min(x_list) - 1, max(x_list) + 1, min(y_list) - 1, max(y_list) + 1

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calculate_membership(point, coordinates):
    distances = []
    min_distance = None
    same_distance = False
    for coor in coordinates:
        dist = distance(point, coor)
        distances.append(dist)
        if dist == min_distance:
            same_distance = True
        elif min_distance is None or dist < min_distance:
            min_distance = dist
            same_distance = False
    if not same_distance:
        return distances.index(min_distance)

def one(data):
    points_coordinates = load_coordinates(data)
    points = {i:[0, False] for i in range(len(points_coordinates))}
    x_min, x_max, y_min, y_max = get_coordinate_ranges(points_coordinates)
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            coordinate = (x,y)
            membership = calculate_membership(coordinate, points_coordinates)
            if membership is None:
                continue
            points[membership][0] += 1
            if x in [x_min, x_max] or y in [y_min, y_max]:
                points[membership][1] = True
    largest_area = 0
    for _, point in points.items():
        if not point[1] and point[0] > largest_area:
            largest_area = point[0]
    print(largest_area)
    return largest_area
    
def two(data):
    points_coordinates = load_coordinates(data)
    x_min, x_max, y_min, y_max = get_coordinate_ranges(points_coordinates)
    max_distance = 10000
    safe_coordinates = 0
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            coordinate = (x,y)
            distance_sum = sum([distance(coordinate, point) for point in points_coordinates])
            safe_coordinates += int(distance_sum < max_distance)
    print(safe_coordinates)
    return safe_coordinates

