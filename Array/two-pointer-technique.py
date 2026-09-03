# Two Pointer means using two indexes/pointers to process an array.

# Given a sorted array arr (sorted in ascending order) and a target, find if there exists any pair of elements (arr[i], arr[j]) such that their sum is equal to the target.


def two_sum(arr, target):

    left = 0
    right = len(arr) - 1

    while left < right:

        total = arr[left] + arr[right]

        if total == target:
            return True

        elif total < target:          # Check if sum is smaller then left = left + 1
            left += 1

        else:                         # Check if sum is greater then right = right - 1
            right -= 1

    return False


arr = [10, 20, 35, 50]
target = 70

print(two_sum(arr, target))



# Find two numbers whose sum is 6
# def two_sum_sorted(arr, target):

#     left = 0
#     right = len(arr) - 1

#     while left < right:

#         total = arr[left] + arr[right]

#         if total == target:
#             return [left, right]

#         elif total < target:
#             left += 1

#         else:
#             right -= 1

#     return [-1, -1]


# arr = [1, 2, 3, 4, 6]

# print(two_sum_sorted(arr, 6))

# 1 + 6 = 7
# Too large → move right.
# 1 + 4 = 5
# Too small → move left.
# 2 + 4 = 6