import math
import random
import matplotlib.pyplot as plt
import numpy as np


class Solver:
    def __init__(self) -> None:
        self.points = [18, 25, 28, 35]
        self.number_of_different_start_clusters = 5
        self.number_of_iterations_per_cluster = 5
        self.k = self.find_k(self.points)

    def find_k(self, points):
        if len(self.points) < 100:
            return len(self.points)
        else:
            return int(round(math.sqrt(len(self.points)), 0))

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
        # print("old_keys", old_keys)
        for centroid in old_keys:
            sum = 0
            if len(mean[centroid]) == 0:
                new_keys.append(centroid)
            else:
                for point in mean[centroid]:
                    sum += point
                new_keys.append((round(sum / len(mean[centroid]), 5)))
        new_mean = {}
        # print("new_keys", new_keys)
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
            # print(mean)
            for i in range(number_of_iterations):
                points_copy = points.copy()
                # print("old_mean", mean)
                mean = self.get_new_centroids(mean)
                # print("new_mean", mean)
                for point in points_copy:
                    distance = 999999
                    for centroid in mean.keys():
                        # print(self.manhattan_distance(point, centroid))
                        if self.manhattan_distance(point, centroid) < distance:
                            distance = self.manhattan_distance(point, centroid)
                            closest_centroid = centroid
                    # print("closest_centroid: ", closest_centroid)
                    # print("mean", mean)
                    # print("clos", mean[closest_centroid])
                    # print("point", point)
                    mean[closest_centroid].append(point)
                # print("her")
            if self.SSE(mean) < best_try[0]:
                best_try = [self.SSE(mean), mean]
        # print("nå")
        return best_try[0], best_try[1]

    def main(self):
        meanSSE = {}
        for i in range(2, self.k+1):
            meanSSE[i] = (self.k_means(self.points, i, self.number_of_different_start_clusters,
                                       self.number_of_iterations_per_cluster))

        xValues = np.array(list(meanSSE.keys()))
        yValues = []
        for j in meanSSE.values():
            yValues.append(j[0])
        yValues = np.array(yValues)
        print(xValues)
        print(yValues)

        plt.plot(xValues, yValues)
        plt.show()

        return meanSSE


solver = Solver()
print(solver.main())
