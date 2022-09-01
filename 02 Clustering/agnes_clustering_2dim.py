import sys
from tkinter.tix import COLUMN


class Solver:
    def __init__(self):
        self.number_of_different_clusters = 10
        self.clusters = {}
        self.distance_matrix = []
        self.points = []
        # f = open("../data.txt", "r")
        with open('../data.txt') as f:
            for line in f:
                self.points.append([float(x) for x in line.split()])
        # print(self.points)
        # f.close()

    def manhattan_distance(self, p1, p2):
        # print("p1", p1)
        # print("p2", p2)
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def create_distance_matrix(self):
        for i in range(len(self.points)):
            self.distance_matrix.append([])
            for j in range(len(self.points)):
                self.distance_matrix[i].append(
                    self.manhattan_distance(self.points[i], self.points[j]))
        # print(self.distance_matrix)

    def setup_clusters(self):
        # print(len(self.clusters))
        self.clusters[0] = []
        for i in self.points:
            self.clusters[0].append(i)

    def update_distance_matrix(self):
        # print("ja")
        leng = len(self.clusters)
        current_clusters = self.clusters[leng-1]
        # print("current_clusters", current_clusters)
        matrix = []

        for i in range(len(current_clusters)):
            matrix.append([])
            if len(current_clusters[i]) == 2 and isinstance(current_clusters[i][0], float):
                # print("jadda")
                for j in range(len(current_clusters)):
                    if len(current_clusters[j]) == 2 and isinstance(current_clusters[j][0], float):
                        matrix[i].append(self.manhattan_distance(
                            current_clusters[i], current_clusters[j]))
                    else:
                        shor = sys.maxsize - 1
                        for k in range(len(current_clusters[j])):
                            if self.manhattan_distance(current_clusters[i], current_clusters[j][k]) < shor:
                                shor = self.manhattan_distance(
                                    current_clusters[i], current_clusters[j][k])
                        matrix[i].append(shor)
        return matrix

    def min_distance(self):
        min_dis = sys.maxsize - 1
        row = None
        column = None
        for i in range(len(self.distance_matrix)):
            for j in range(len(self.distance_matrix)):
                if j < i:
                    continue
                if i != j:
                    if self.distance_matrix[i][j] < min_dis:
                        min_dis = self.distance_matrix[i][j]
                        row = i
                        column = j
        # print(min_dis, cluster_1, cluster_2)
        return min_dis, row, column

    def merge_clusters(self, cluster1, cluster2):
        index = len(self.clusters)
        self.clusters[index] = []
        merged = []
        for i in range(len(self.clusters[index-1])):
            if i == cluster1 or i == cluster2:
                merged.append(self.clusters[index-1][i])
            self.clusters[index].append(self.clusters[index-1][i])

        self.clusters[index].append(merged)
        return

    def main(self):
        self.create_distance_matrix()
        self.setup_clusters()
        print(len(self.distance_matrix))
        # print(self.clusters)
        # while len(self.clusters) < self.number_of_different_clusters:
        # print(self.clusters[0][44])
        # print(self.clusters[0][68])
        # print(self.manhattan_distance(
        #     self.clusters[0][44], self.clusters[0][68]))

        for i in range(self.number_of_different_clusters):
            min_dis, row, column = self.min_distance()
            self.merge_clusters(row, column)
            # print(self.clusters[0])
            # print(self.clusters[1])
            self.distance_matrix = self.update_distance_matrix()
            print(self.distance_matrix)
            # print(self.clusters[2])
            break
            # print(min_dis, row, column)
            # print(self.clusters[0])
            continue

        # for i in range(self.number_of_different_clusters):
        #     self.clusters.append([])
        # for i in range(len(self.points)):
        #     self.clusters[i % self.number_of_different_clusters].append(self.points[i])
        # print(self.clusters)


solver = Solver()
solver.main()
