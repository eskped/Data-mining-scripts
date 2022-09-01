import math
data = [(("google.com", 0), "Benign"),
        (("google.com", 4), "Benign"),
        (("google.com", 20), "Benign"),
        (("google.com", 30), "Attack"),
        (("reddit.com", 3), "Benign"),
        (("reddit.com", 32), "Attack"),
        (("reddit.com", 29), "Attack"),
        (("howtohack.com", 3), "Benign"),
        (("howtohack.com", 10), "Attack"),
        (("howtohack.com", 47), "Attack"), ]

attributes = ["Website", "Login"]
numeric_attributes = ["Login"]


def entropy(data):
    entropy = 0
    labels = {}
    for i in data:
        if i[1] in labels:
            labels[i[1]] += 1
        else:
            labels[i[1]] = 1
    # print(labels)
    for i in labels:
        entropy += labels[i]/len(data) * math.log(labels[i]/len(data), 2)
    return -entropy


def information_gain(data, attribute, split):
    gain = entropy(data)
    values = {}
    if split == None:
        for i in data:
            if i[0][attributes.index(attribute)] in values:
                values[i[0][attributes.index(attribute)]].add(i)
            else:
                values[i[0][attributes.index(attribute)]] = {i}
        for i in values:
            gain -= len(values[i])/len(data) * entropy(values[i])
    else:
        for i in data:
            if i[0][attributes.index(attribute)] <= split:
                if "left" in values:
                    values["left"].add(i)
                else:
                    values["left"] = {i}
            else:
                if "right" in values:
                    values["right"].add(i)
                else:
                    values["right"] = {i}
        for i in values:
            gain -= len(values[i])/len(data) * entropy(values[i])
    return gain


def are_same_class(data):
    return len(set([i[1] for i in data])) == 1


def are_same_attributes(data):
    return len(set([i[0] for i in data])) == 1


def main():
    print("inital entropy: ", entropy(data))
    sort_data = sorted(data, key=lambda x: x[0][attributes.index("Login")])
    for attribute in attributes:
        if attribute in numeric_attributes:
            split = None
            max_gain = 0
            for i in range(0, max([i[0][attributes.index(attribute)] for i in data])+1):
                if information_gain(data, attribute, i) > max_gain:
                    max_gain = information_gain(data, attribute, i)
                    split = (sort_data[i-1][0][attributes.index(
                        attribute)] + sort_data[i][0][attributes.index(attribute)])/2
            print("Information gain for", attribute,
                  "is", max_gain, "with split value", split)
        else:
            print("Information gain for", attribute, "is",
                  information_gain(data, attribute, None))


if __name__ == "__main__":
    main()
