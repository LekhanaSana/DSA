def longest_subarray_sum_k(nums, k):
    total = 0
    first_index = {0: -1}
    longest = 0

    for i in range(len(nums)):
        total = total + nums[i]
        needed = total - k

        if needed in first_index:
            length = i - first_index[needed]

            if length > longest:
                longest = length

        if total not in first_index:
            first_index[total] = i

    return longest


nums = [10, 5, 2, 7, 1, 9]
k = 15

print(longest_subarray_sum_k(nums, k))

