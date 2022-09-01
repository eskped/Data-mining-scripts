# array = [17, 20, 18.5, 27, 26, 24]
array = [100, 50, 750, 1000, 9500, 7000]
xMin = min(array)
xMax = max(array)
array1 = []
for x in array:
    array1.append(round(abs((x-xMin)/(xMax-xMin)), 4))


print("Min-max:", array1)
