def two_sum_problem(arr, target):
    left = 0
    right = len(arr) - 1
    
    while (left < right):
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left = left + 1
        else:
            right = right - 1

arr = [1,2,3,5,7,10,11,15]
target = 15

print("The number were found on this index: ", two_sum_problem(arr, target))