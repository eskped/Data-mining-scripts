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


def main(k, instance, data):

    prediction = []
    noe = find_nearest_neighbours(data, instance, k)
    print("instance", instance)
    if instance in data and instance in noe:
        noe.remove(instance)
    for i in noe:
        prediction.append(i[1][1])
        print("Closest neighbour number:", noe.index(i)+1,
              "Distance to that neighbour:", i[0], "Point: ", i[1])
    print("Prediction:", max(set(prediction), key=prediction.count))


data = [
    ((35, 35, 3), "Yes"),
    ((22, 50, 2,), "No"),
    ((63, 200, 1,), "No"),
    ((59, 170, 1), "No"),
    ((25, 40, 4), "Yes"),
]

# remember may need to standardize the data before using this algorithm

# if there are non-numerical values in the data, you need to convert them to numerical values
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

data1 = [
    ((1, 1, 0, 0, 0.8), " No"),
    ((1, 0, 1, 0, 0.3), "No"),
    ((1, 0, 0, 1, 0.6), "No"),
    ((0, 0, 1, 0, 0.9), "Yes"),
    ((0, 0, 0, 1, 1.0), "Yes"),
    ((0, 0, 1, 0, 1.2), "No"),
    ((0, 0, 1, 0, 0.4), "No"),
    ((0, 0, 0, 1, 1.2), "Yes"),
    ((0, 0, 0, 1, 1.3), "Yes"),
    ((0, 0, 0, 1, 1.4), "No"),
]

k = 3
instance = (0, 0)
if __name__ == "__main__":
    main(k, instance, training_data)
