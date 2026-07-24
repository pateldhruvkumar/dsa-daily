def maxi_sum_subarray(arr, size):
    current = 0

    for i in range (size):
        current += arr[i]

    window_loop = len(arr) - size
    
    maxx = current
    for i in range(1, window_loop + 1):
        current = current - arr[i - 1] + arr[i + size - 1]
        if current > maxx:
            maxx = current
    
    return maxx

arr = [3,8,2,5,7,6,12]
size = 4

print("Maximum sum of a subarray: ", maxi_sum_subarray(arr, size))