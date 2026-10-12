
def min_subarray_len(target, nums):
    left = 0
    total = 0
    min_len = len(nums) + 1

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            length = right - left + 1

            if length < min_len:
                min_len = length

            total -= nums[left]
            left += 1

    if min_len == len(nums) + 1:
        return 0
    else:
        return min_len


nums = [2, 3, 1, 2, 4, 3]
target = 7

print(min_subarray_len(target, nums))
