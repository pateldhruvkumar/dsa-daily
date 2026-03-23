def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

mylist = [4,5,6,9,10,1]

result = linearSearch(mylist, 9)

print("Result: ", result)