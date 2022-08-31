class Solver:
    def __init__(self):
        self.number_of_different_clusters = 5
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
        # print(self.clusters)

    def merge_clusters(self):
        distances = []
        pass

    def update_distance_matrix(self, cluster_1, cluster_2):
        for cluster in self.clusters[len(self.clusters)]:
            for point in cluster:
                for other_point in cluster:
                    self.distance_matrix[point][other_point] = self.manhattan_distance(
                        point, other_point)

    def main(self):
        self.create_distance_matrix()
        self.setup_clusters()

        # for i in range(self.number_of_different_clusters):
        #     self.clusters.append([])
        # for i in range(len(self.points)):
        #     self.clusters[i % self.number_of_different_clusters].append(self.points[i])
        # print(self.clusters)


solver = Solver()
solver.main()
