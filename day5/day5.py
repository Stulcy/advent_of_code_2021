cloud_locations = [[int(point) for point in points.split(',')] for points in [cloud.strip('\n').replace(' -> ', ',')
                                                                              for cloud in open('day5/day5.txt')]]
diagonal_cloud_locations = []
unique_points = set()
dangerous_points = set()


def add_point(curr_x, curr_y):
    if (curr_x, curr_y) in unique_points and (curr_x, curr_y) not in dangerous_points:
        dangerous_points.add((curr_x, curr_y))
    else:
        unique_points.add((curr_x, curr_y))


def add_new_points_without_diagonal(cloud):
    big_x = cloud[0] if cloud[0] > cloud[2] else cloud[2]
    small_x = cloud[0] if cloud[0] < cloud[2] else cloud[2]
    big_y = cloud[1] if cloud[1] > cloud[3] else cloud[3]
    small_y = cloud[1] if cloud[1] < cloud[3] else cloud[3]

    for curr_x in range(small_x, big_x + 1):
        for curr_y in range(small_y, big_y + 1):
            add_point(curr_x, curr_y)


def add_new_points_diagonal(cloud):
    if cloud[0] > cloud[2] and cloud[1] > cloud[3]:
        curr_y = cloud[1]
        for curr_x in range(cloud[0], cloud[2] - 1, - 1):
            add_point(curr_x, curr_y)
            curr_y -= 1

    elif (cloud[0] < cloud[2] and cloud[1] < cloud[3]):
        curr_y = cloud[1]
        for curr_x in range(cloud[0], cloud[2] + 1):
            add_point(curr_x, curr_y)
            curr_y += 1

    elif (cloud[0] < cloud[2] and cloud[1] > cloud[3]):
        curr_y = cloud[1]
        for curr_x in range(cloud[0], cloud[2] + 1):
            add_point(curr_x, curr_y)
            curr_y -= 1

    elif (cloud[0] > cloud[2] and cloud[1] < cloud[3]):
        curr_y = cloud[1]
        for curr_x in range(cloud[0], cloud[2] - 1, - 1):
            add_point(curr_x, curr_y)
            curr_y += 1


for cloud in cloud_locations:
    if cloud[0] == cloud[2] or cloud[1] == cloud[3]:
        add_new_points_without_diagonal(cloud)
    else:
        diagonal_cloud_locations.append(cloud)


print(len(dangerous_points))

for cloud in diagonal_cloud_locations:
    add_new_points_diagonal(cloud)

print(len(dangerous_points))
