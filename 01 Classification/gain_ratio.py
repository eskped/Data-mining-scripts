import math
from information_gain import information_gain

# data = [(("google.com", 0), "Benign"),
#         (("google.com", 4), "Benign"),
#         (("google.com", 20), "Benign"),
#         (("google.com", 30), "Attack"),
#         (("reddit.com", 3), "Benign"),
#         (("reddit.com", 32), "Attack"),
#         (("reddit.com", 29), "Attack"),
#         (("howtohack.com", 3), "Benign"),
#         (("howtohack.com", 10), "Attack"),
#         (("howtohack.com", 47), "Attack"), ]


data = [(("google.com", 20), "Benign"),
        (("google.com", 30), "Attack"),
        (("reddit.com", 32), "Attack"),
        (("reddit.com", 29), "Attack"),
        (("howtohack.com", 10), "Attack"),
        (("howtohack.com", 47), "Attack"), ]

attributes = ["Website", "Login"]
numeric_attributes = ["Login"]


def intrinsic_value(data, attribute):
    iv = 0
    values = {}
    for i in data:
        if i[0][attributes.index(attribute)] in values:
            values[i[0][attributes.index(attribute)]].add(i)
        else:
            values[i[0][attributes.index(attribute)]] = {i}
    for i in values:
        iv -= len(values[i])/len(data) * math.log(len(values[i])/len(data), 2)
    return iv


def main():
    sort_data = sorted(data, key=lambda x: x[0][attributes.index("Login")])
    gains = {}
    for attribute in attributes:
        if attribute in numeric_attributes:
            split = None
            max_gain = 0
            previous = 0
            for i in range(0, max([i[0][attributes.index(attribute)] for i in data])+1):
                if information_gain(data, attribute, i) > max_gain:
                    max_gain = information_gain(data, attribute, i)
                    split = (previous + i)/2
                    previous = i
            gains[attribute] = (max_gain, split)
            print("Information gain for", attribute,
                  "is", max_gain, "with split value", split)
        else:
            print("Information gain for", attribute, "is",
                  information_gain(data, attribute, None))
            gains[attribute] = (information_gain(data, attribute, None), None)
    for i in gains:
        print("Gain ratio for", i, "is", gains[i][0]/intrinsic_value(data, i))
    # print(intrinsic_value(data, "Login"))
    # print(intrinsic_value(data, "Website"))


if __name__ == "__main__":
    main()
