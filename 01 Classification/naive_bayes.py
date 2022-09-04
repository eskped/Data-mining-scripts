from sklearn import naive_bayes
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from collections import Counter


data = [(["Action", "Xbox", "High", ], ("No")),
        (["Action", "Switch", "Low", ], ("No")),
        (["Action", "PS4", "High", ], ("No")),
        (["Adventure", "Switch", "High", ], ("Yes")),
        (["Adventure", "Switch", "High", ], ("Yes")),
        (["Adventure", "Switch", "High", ], ("No")),
        (["Adventure", "Switch", "Low", ], ("No")),
        (["Adventure", "PS4", "High", ], ("Yes")),
        (["Adventure", "PS4", "High", ], ("Yes")),
        (["Adventure", "PS4", "High", ], ("No"))
        ]

features_names = ["Genre", "Platform", "Sales"]


def setup():
    features = []
    feature_count = {}
    labels = []

    for d in data:
        labels.append(d[1])
        for f in d[0]:
            features.append(f)
            if f in feature_count:
                feature_count[f] += 1
            else:
                feature_count[f] = 1
    return features, feature_count, labels


def check_laplacian(predict, features, labels):
    commbos = set()
    for f in predict:
        for d in data:
            if f in d[0]:
                commbos.add(f+d[1])

    if len(commbos) < (len(features) * len(labels)):
        return True
    return False


def main(predict):
    features, feature_count, labels = setup()

    laplacian = check_laplacian(predict, features, labels)
    different_features_count = []

    for d in data:
        for i in range(len(d[0])):
            if len(different_features_count) >= 3:
                different_features_count[i].append(d[0][i])
            else:
                different_features_count.append([d[0][i]])
    for i in range(len(different_features_count)):
        different_features_count[i] = len(
            set(different_features_count[i]))

    counts = {}
    for l in labels:
        counts[l] = {}

    # fill yes and no
    for d in data:
        if d[1] in counts[d[1]]:
            counts[d[1]][d[1]] += 1
        else:
            counts[d[1]][d[1]] = 1

    for f in predict:
        for label in counts:
            if f not in counts:
                counts[label][f] = 0

    for p in predict:
        for d in data:
            if p in d[0]:
                counts[d[1]][p] += 1

    prediction = {}
    for l in set(labels):
        prediction[l] = counts[l][l]/len(data)

    for count in counts:
        teller = 0
        for f in counts[count]:
            if f in labels:
                continue
            if laplacian:
                prediction[count] *= round((counts[count][f]+1) /
                                           (counts[count][count] + different_features_count[teller]), 1)
            teller += 1

    return prediction


predict = ["Action", "PS4", "High"]
if __name__ == "__main__":
    print(main(predict))
