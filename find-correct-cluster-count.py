import math
import random


class Solver:
    def __init__(self) -> None:
        self.points = [18, 25, 28, 35]
        self.number_of_different_start_clusters = 5
        self.number_of_iterations_per_cluster = 5
        self.k = int(round(math.sqrt(len(self.points)), 0))

    def find_random_centroids(self, points, k):
        centroids = random.sample(points, k)
        return centroids

    def manhattan_distance(self, p1, p2):
        return abs(p1 - p2)

    def find_closest(self, p, points):
        return min(points, key=lambda point: self.manhattan_distance(point, p))

    def SSE(self, mean):
        sse = 0
        for centroid in mean.keys():
            for point in mean[centroid]:
                sse += (self.manhattan_distance(point, centroid))**2
        return sse

    def get_new_centroids(self, mean):
        new_keys = []
        old_keys = list(mean.keys())
        for centroid in old_keys:
            sum = 0
            if len(mean[centroid]) == 0:
                new_keys.append(centroid)
            else:
                for point in mean[centroid]:
                    sum += point
                new_keys.append
                (round(sum / len(mean[centroid]), 5))
        new_mean = {}
        for i in new_keys:
            new_mean[i] = []

        return new_mean

    def k_means(self, points, k, different_start_clusters, number_of_iterations):
        best_try = [99999, {}]
        for j in range(different_start_clusters):
            centroids = self.find_random_centroids(points, k)
            mean = {}
            for centroid in centroids:
                mean[centroid] = []
            for i in range(number_of_iterations):
                points_copy = points.copy()
                mean = self.get_new_centroids(mean)
                for point in points_copy:
                    distance = 999999
                    for centroid in mean.keys():
                        print(self.manhattan_distance(point, centroid))
                        if self.manhattan_distance(point, centroid) < distance:
                            distance = self.manhattan_distance(point, centroid)
                            closest_centroid = centroid
                    print(point)
                    mean[closest_centroid].append(point)
            if self.SSE(mean) < best_try[0]:
                best_try = [self.SSE(mean), mean]

        return best_try[0], best_try[1]

    def main(self):
        for i in range(1, self.k):
            print(self.k_means(self.points, i, self.number_of_different_start_clusters,
                  self.number_of_iterations_per_cluster))
        return


solver = Solver()
solver.main()
