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


def gini(data):
    gini = 1
    labels = {}
    for i in data:
        if i[1] in labels:
            labels[i[1]] += 1
        else:
            labels[i[1]] = 1
    # print("labels", labels)
    for i in labels:
        gini -= (labels[i]/len(data))**2
    return gini


def gini_index(data, attribute, split):
    gini_index = 0
    values = {}
    if split == None:
        for i in data:
            if i[0][attributes.index(attribute)] in values:
                values[i[0][attributes.index(attribute)]].add(i)
            else:
                values[i[0][attributes.index(attribute)]] = {i}
        for i in values:
            gini_index += len(values[i])/len(data) * gini(values[i])
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
            gini_index += len(values[i])/len(data) * gini(values[i])
    return gini_index


def main():
    sort_data = sorted(data, key=lambda x: x[0][attributes.index("Login")])
    # print("sort_data", sort_data)
    gini = {}
    for attribute in attributes:
        if attribute in numeric_attributes:
            split = None
            min_gini = 1
            for i in range(0, max([i[0][attributes.index(attribute)] for i in data])+1):
                if gini_index(data, attribute, i) < min_gini:
                    min_gini = gini_index(data, attribute, i)
                    split = (sort_data[i-1][0][attributes.index(
                        attribute)] + sort_data[i][0][attributes.index(attribute)])/2
            print("Gini index for", attribute,
                  "is", min_gini, "with split value", split)
        else:
            print("Gini index for", attribute, "is",
                  gini_index(data, attribute, None))


if __name__ == "__main__":
    main()
