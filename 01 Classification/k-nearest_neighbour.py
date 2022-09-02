data = [
    ((35, 35, 3), "Yes"),
    ((22, 50, 2,), "No"),
    ((63, 200, 1,), "No"),
    ((59, 170, 1), "No"),
    ((25, 40, 4), "Yes"),
]


attributes = ["Age", "Income", "Games Played"]
numeric_attributes = ["Age", "Income", "Games Played"]


def manhattan_distance(a, b):
    distance = 0
    for i in range(0, len(a)):
        distance += round(abs(a[i] - b[i]), 5)
    return distance


def euclidean_distance(a, b):
    distance = 0
    for i in range(0, len(a)):
        distance += (a[i] - b[i])**2
    return round(distance**0.5, 5)


def chebychev_distance(a, b):
    distance = []
    for i in range(0, len(a)):
        distance.append(abs(a[i] - b[i]))
    return round(max(distance))


def find_nearest_neighbours(data, instance, k):
    distances = []
    for i in data:
        distances.append((euclidean_distance(i[0], instance), i))
    distances.sort(key=lambda x: x[0])
    return distances[0:k]


k = 5
instance = (37, 50, 2)


def main():
    noe = find_nearest_neighbours(data, instance, k)
    prediction = []
    for i in noe:
        prediction.append(i[1][1])
        print("Number:", noe.index(i)+1, "Distance:", i[0], "Data: ", i[1])
    print("Prediction:", max(set(prediction), key=prediction.count))


if __name__ == "__main__":
    main()
