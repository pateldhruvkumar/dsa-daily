def length_of_shortest_subarray(nums, target):
    left, right = 0, len(nums) - 1
    count = 0
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            count = right - left + 1
            return count
        elif current_sum < target:
            left += 1
        else:
            right -= 1

nums = [1,4,4]
target = 7
print(length_of_shortest_subarray(nums, target))