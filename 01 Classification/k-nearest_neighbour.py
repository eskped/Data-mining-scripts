data = [
    ((35, 35, 3), "Yes"),
    ((22, 50, 2,), "No"),
    ((63, 200, 1,), "No"),
    ((59, 170, 1), "No"),
    ((25, 40, 4), "Yes"),
]

# remember may need to standardize the data before using this algorithm
training_data = [
    ((1, 0.4), 0),
    ((1.3, -0.4), 0),
    ((1.1, 0.8), 0),
    ((1.0, -2.0), 0),
    ((-0.1, 0.0), 0),
    ((0.0, 0.3), 1),
    ((-0.6, 0.9), 1),
    ((-1.4, -1.4), 1),
    ((-1.3, -0.2), 1),
    ((-1.0, 1.5), 1),
]


attributes = ["Variance", "Image"]
numeric_attributes = ["Variance", "Image"]


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
        distances.append((round(manhattan_distance(i[0], instance), 5), i))
    distances.sort(key=lambda x: x[0])
    return distances[0:k]


k = 4
instance = (37, 50, 2)


def main():

    # instances = []
    # for i in training_data:
    #     instances.append(i[0])

    # for instance1 in instances:
    prediction = []
    noe = find_nearest_neighbours(training_data, instance, k)
    for i in noe[1:]:
        prediction.append(i[1][1])
        print("K:", noe.index(i)+1, "Distance:", i[0], "Data: ", i[1])
    print("Prediction:", max(set(prediction), key=prediction.count))


if __name__ == "__main__":
    main()
