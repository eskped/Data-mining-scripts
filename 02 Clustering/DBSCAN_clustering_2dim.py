import matplotlib.pyplot as plt


class Solver:
    def __init__(self):
        self.points = [(19, 20), (18, 19), (17, 18),
                       (28, 35), (27, 34), (28, 33), (2, 2), (40, 40), (1, 1), (0, 0)]
        self.core_points = []
        self.noise_points = []
        self.border_points = []
        self.clusters = {}
        self.eps = 3
        self.MinPts = 3
        self.eps_range = [1, 5]

    def find_core_points(self):
        for point in self.points:
            if self.is_core_point(point):
                self.core_points.append(point)

    def is_core_point(self, point):
        count = 0
        for other_point in self.points:
            if self.is_neighbour(point, other_point):
                count += 1
        if count >= self.MinPts:
            return True
        else:
            return False

    def is_neighbour(self, point1, point2):
        if self.manhattan_distance(point1, point2) <= self.eps:
            return True
        else:
            return False

    def manhattan_distance(self, point1, point2):
        return (abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

    def find_noise_points(self):
        for point in self.points:

            if point not in self.core_points:
                noise = True
                for core_point in self.core_points:
                    if self.is_neighbour(point, core_point):
                        noise = False
                        break
                if noise:
                    self.noise_points.append(point)

    def find_border_points(self):
        for point in self.points:
            if point not in self.noise_points and point not in self.core_points:
                self.border_points.append(point)

    def find_centroid(self, points):
        x = 0
        y = 0
        for point in points:
            x += point[0]
            y += point[1]
        return (x/len(points), y/len(points))

    def get_SSE(self, clusters):
        sse = 0
        for cluster in clusters:
            centroid = self.find_centroid(clusters[cluster])
            for point in clusters[cluster]:
                sse += (self.manhattan_distance(point, centroid))**2
        return round(sse, 5)

    def get_3rd_point_distance(self):
        dis = []
        for point in self.points:
            distances = []
            for other_point in self.points:
                if point != other_point:
                    distances.append(
                        (self.manhattan_distance(point, other_point)))
            distances.sort()
            dis.append(distances[2])

        dis.sort()
        return dis

    def dbscan(self):
        self.find_core_points()
        self.find_noise_points()
        self.find_border_points()
        self.points = self.core_points + self.border_points
        self.assigned = set()
        # print("Core", self.core_points)
        # print("Noise", self.noise_points)
        # print("Border", self.border_points)
        index = 0
        for core in self.core_points:
            increase_index = False
            if core not in self.assigned:
                self.clusters[index] = [core]
                self.assigned.add(core)
                increase_index = True

            for point in self.points:
                if (self.is_neighbour(core, point)) and point not in self.assigned:
                    points = self.clusters[index]
                    points.append(point)
                    self.clusters[index] = points
                    self.assigned.add(point)

            if increase_index:
                index += 1
        return self.clusters

    def main(self):
        values = self.get_3rd_point_distance()
        plt.plot(values)
        plt.show()
        return self.dbscan(), self.noise_points, self.get_SSE(self.clusters), self.get_3rd_point_distance()


solver = Solver()
clusters, noise, sse, third = solver.main()
print("Clusters: ", clusters)
print("Noise points: ", noise)
print("SSE: ", sse)
print("Distances to third point", third)
