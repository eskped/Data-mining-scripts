from random import randrange


def cross_validation_split(data, cv):
    # Create a copy of the data
    data_copy = list(data)
    # Create a list to hold the folds
    folds = []
    # Calculate the size of each fold
    fold_size = int(len(data) / cv)
    # Loop through the folds
    for i in range(cv):
        # Create an empty fold
        fold = []
        # Loop through the fold size
        while len(fold) < fold_size:
            # Get a random index
            # index = randrange(len(data_copy))
            # Add the row to the fold
            fold.append(data_copy.pop(0))
        if len(data_copy) != 0 and i == cv - 1:
            fold.append(data_copy.pop())
        # Add the fold to the list of folds
        folds.append(fold)
    # Return the list of folds
    return folds


def manhattan_distance(a, b):
    distance = []
    for i in range(0, len(a)):
        distance.append(abs(a[i] - b[i]))
    return round(max(distance))


def k_nearest_neighbours(data, instance, k):
    distances = []
    # print("data", data)
    for i in data:
        # print(i)
        distances.append((round(manhattan_distance(i[0], instance), 10), i))
    distances.sort(key=lambda x: x[0])
    return distances[0:k]


def get_accuracy(data, predictions):
    correct = 0
    for i in range(len(predictions)):
        if data[i][1] == predictions[i][1][1]:
            correct += 1
    return round(correct / float(len(predictions)), 3)


def main(cv, data1, k_max):

    folds = cross_validation_split(data1, cv)
    scores = []

    for i in range(cv):
        print(i)
        test_set = folds[i]
        print("test_set", test_set)
        train_set = [x for x in data1 if x not in test_set]
        for k in range(1, k_max+1):

            if k % 2 == 0:
                continue
            print(k)
            predictions = []
            for instance in test_set:
                # print("ins", instance)
                # print("t",  train_set)
                neighbour = k_nearest_neighbours(train_set, instance[0], k)
                # print("N", neighbour)
                predictions.append(neighbour[0])
            print("test_set", test_set)
            print("predictions", predictions)
            # print("pre", predictions[0][1][1])
            accuracy = get_accuracy(test_set, predictions)
            scores.append(accuracy)
    print(scores)

    return


data1 = [
    ((1, 1, 0, 0, 0.8), "No"),
    ((1, 0, 1, 0, 0.3), "No"),
    ((1, 0, 0, 1, 0.6), "No"),
    ((0, 0, 1, 0, 0.9), "Yes"),
    ((0, 0, 1, 0, 1.0), "Yes"),
    ((0, 0, 1, 0, 1.1), "No"),
    ((0, 0, 1, 0, 0.4), "No"),
    ((0, 0, 0, 1, 1.2), "Yes"),
    ((0, 0, 0, 1, 1.3), "Yes"),
    ((0, 0, 0, 1, 1.4), "No"),


]

cv = 3
k_max = 5

if __name__ == "__main__":
    main(cv, data1, k_max)
