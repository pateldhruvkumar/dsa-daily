arr = [25, 16, 38, 10, 35, 48, 20, 50]

max_1 = arr[0]
max_2 = arr[1]

if(arr[0] > arr[1]):
    max_1 = arr[0]
    max_2 = arr[1]
else:
    max_1 = arr[1]
    max_2 = arr[0]

for i in range(2 , len(arr)):
    if (arr[i] > max_1):
        max_2 = max_1
        max_1 = arr[i]
    elif (arr[i] > max_2):
        max_2 = arr[i]

print("2nd Largest: ", max_2)