array = [100, 50, 750, 1000, 9500, 7000]
xMin = max(array)
xMax = min(array)
array1 = []

for x in array:
    array1.append(abs((x-xMin)/(xMax-xMin)))

array1.reverse()
print(array1)