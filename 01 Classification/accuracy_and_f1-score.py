def accuracy(truth, predicted):
    correct = 0
    for i in range(len(truth)):
        if truth[i] == predicted[i]:
            correct += 1
    return round(correct / len(truth), 5)


def f1(truth, predicted):
    TP = 0
    FP = 0
    FN = 0
    for i in range(len(truth)):
        if truth[i] == 1 and predicted[i] == 1:
            TP += 1
        elif truth[i] == 0 and predicted[i] == 1:
            FP += 1
        elif truth[i] == 1 and predicted[i] == 0:
            FN += 1
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = round(2 * precision * recall / (precision + recall), 5)
    return f1, round(precision, 5), round(recall, 5)


truth = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
predicted_a = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
predicted_b = [0, 0, 0, 0, 1, 0, 1, 0, 1, 1]


print("Accuracy:", accuracy(truth, predicted_b))
print("F1, precicion, recall:", f1(truth, predicted_b))


def accuracy(TP, TN, n):
    return round((TP + TN) / n, 5)


def f1(TP, FP, FN):
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = round(2 * precision * recall / (precision + recall), 5)
    return f1, round(precision, 5), round(recall, 5)


TP_a = 85
TN_a = 0
FP_a = 201
FN_a = 0
n = TP_a + TN_a + FP_a + FN_a

# print("Accuracy:", accuracy(TP_a, TN_a, n))
# print("F1, precicion, recall:", f1(TP_a, FP_a, FN_a))
