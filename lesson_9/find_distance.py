import math


def find_distance(*points):
    summa = 0
    for index, point in enumerate(points):
        if index == len(points) - 1:
            break
        x1, y1 = point
        x2, y2 = points[index+1]
        final_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        summa += final_dis
    return summa


my_list = ((1, 2), (2, 3), (2, 6))


print(find_distance(*my_list))
