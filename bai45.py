def minJumps(nums):
    n = len(nums)
    if n == 1:
        return 0

    jumps = 0
    current_position = 0
    max_reach = 0

    for i in range(n - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == current_position:
            jumps += 1
            current_position = max_reach

        # Debug output
        print(f"i = {i}, jumps = {jumps}, current_position = {current_position}, max_reach = {max_reach}")

    return jumps

# Example usage:
nums1 = [2, 3, 1, 1, 4]
result1 = minJumps(nums1)
print(f"Result 1: {result1}")

nums2 = [2, 3, 0, 1, 4]
result2 = minJumps(nums2)
print(f"Result 2: {result2}")
