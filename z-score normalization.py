import math

array = [17, 20, 18.5, 27, 26, 24]

mean = sum(array)/len(array)
deviations = [(x - mean) ** 2 for x in array]
variance = math.sqrt(sum(deviations) /len(array))

array1 = []

for x in array:
    array1.append((x-mean)/variance)

print(array1)