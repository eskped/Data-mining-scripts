import random

all_points = [(2, 2), (4, 6), (4, 8), (6, 6), (6, 8), (8, 0)]
number_of_clusters = 3
number_of_different_start_clusters = 5
number_of_iterations_per_cluster = 5


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_closest(p, points):
    return min(points, key=lambda point: manhattan_distance(point, p))


def find_random_centroids(points, k):
    centroids = random.sample(points, k)
    return centroids


def get_new_centroids(mean):

    new_keys = []
    old_keys = list(mean.keys())
    for centroid in old_keys:
        sum = [0, 0]
        if len(mean[centroid]) == 0:
            new_keys.append(centroid)
        else:
            for point in mean[centroid]:
                sum[0] += point[0]
                sum[1] += point[1]
            new_keys.append(
                (round(sum[0] / len(mean[centroid]), 5), round(sum[1] / len(mean[centroid]), 5)))
    new_mean = {}
    for i in new_keys:
        new_mean[i] = []

    return new_mean


def SSE(mean):
    sse = 0
    for centroid in mean.keys():
        for point in mean[centroid]:
            sse += (manhattan_distance(point, centroid))**2
    return sse


def k_means(points, k, different_start_clusters, number_of_iterations):
    best_try = [99999, {}]
    for j in range(different_start_clusters):
        centroids = find_random_centroids(points, k)
        mean = {}
        for centroid in centroids:
            mean[centroid] = []
        for i in range(number_of_iterations):
            points_copy = points.copy()
            mean = get_new_centroids(mean)
            for point in points_copy:
                distance = 999999
                for centroid in mean.keys():
                    if manhattan_distance(point, centroid) < distance:
                        distance = manhattan_distance(point, centroid)
                        closest_centroid = centroid
                mean[closest_centroid].append(point)
        if SSE(mean) < best_try[0]:
            best_try = [SSE(mean), mean]

    return best_try[0], best_try[1]


def main():
    sse, mean = k_means(all_points, number_of_clusters, number_of_different_start_clusters,
                        number_of_iterations_per_cluster)

    print(sse)
    print(mean)


main()
