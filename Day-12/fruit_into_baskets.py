
def total_fruit(fruits):
    left = 0
    count = {}
    longest = 0

    for right in range(len(fruits)):
        fruit = fruits[right]

        if fruit in count:
            count[fruit] = count[fruit] + 1
        else:
            count[fruit] = 1

        while len(count) > 2:
            fruit_left = fruits[left]
            count[fruit_left] = count[fruit_left] - 1

            if count[fruit_left] == 0:
                del count[fruit_left]

            left = left + 1

        length = right - left + 1

        if length > longest:
            longest = length

    return longest


fruits = [1, 2, 1, 2, 3]
print(total_fruit(fruits))
