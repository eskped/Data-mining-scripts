import random

all_points = [(2, 2), (4, 6), (4, 8), (6, 6), (6, 8), (8, 0)]


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_closest(p, points):
    return min(points, key=lambda point: manhattan_distance(point, p))


def update_centroids(points, mean):
    print("hei")
    print(mean)
    new_keys = []
    old_keys = [mean.keys()]
    for centroid in old_keys:
        sum = [0, 0]
        # print(mean)
        if len(mean[centroid]) == 0:
            continue
        else:
            for point in mean[centroid]:
                sum[0] += point[0]
                sum[1] += point[1]
            new_keys.appen(sum[0] / len(mean[centroid]), sum[1] /
                           len(mean[centroid]))
    for i in range(len(new_keys)):
        # mean[new_key[i]] = mean[old_key[i]]
        # del dictionary[old_key[i]]
        mean[mean[i]] = mean.pop(centroid[i])

    return mean


def k_means(points, k):
    centroids = random.sample(points, k=k)
    mean = {}
    for centroid in centroids:
        mean[centroid] = []
    for i in range(2):
        points_copy = points.copy()
        points_copy = [
            point for point in points_copy if point not in mean.keys()]
        # print(mean)
        print(points_copy)
        for point in points_copy:
            # print("point", point)
            distance = 999999
            for centroid in mean.keys():
                if manhattan_distance(point, centroid) < distance:
                    distance = manhattan_distance(point, centroid)
                    closest_centroid = centroid
            if closest_centroid in mean.keys():
                mean[closest_centroid].append(point)
            else:
                mean[closest_centroid] = [point]
        # print(mean.keys())
        # print(centroids)
        print(mean)
        print(update_centroids(points_copy, mean))

        # if all(closest_points[p] == clusters[p] for p in points):
        #     return clusters
        # for p in points:
        #     clusters[p] = closest_points[p]


def main():
    k_means(all_points, 3)


main()
