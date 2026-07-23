def maxi_sum_subarray(arr, size):
    maxx = float('-inf')
    for i in range(len(arr) - size + 1):
        current = 0
        for j in range(i, i + size):
            current = current + arr[j]
        maxx = max(current, maxx)
    return maxx

arr = [3,8,2,5,7,6,12]
size = 4

print("Maximum Sum of Subarray: ", maxi_sum_subarray(arr, size))