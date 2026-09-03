# Sliding Window Technique is a method used to solve problems that involve subarray or substring or window.
# Find the maximum sum of 3 consecutive elements.

# Given an array arr[] and an integer k, we need to calculate the maximum sum of a subarray having size exactly k. 

def max_sum(arr, k):
    window_sum = sum(arr[:k])              # arr[:3]
    max_sum = window_sum                   # 8

    for i in range(k, len(arr)):            # range(3,6) i = 3,4,5 
        window_sum = window_sum + arr[i] - arr[i - k]   
        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]

print(max_sum(arr, 3))

# 2 + 1 + 5 = 8      First window
# 1 + 5 + 1 = 7      Move window 
# 5 + 1 + 3 = 9
# 1 + 3 + 2 = 6
# arr[i]       → add the new element
# arr[i-k]     → remove the old element.
# old sum + new element - old element
# Time Complexity: O(n)






# def max_sum(arr, k):

#     window_sum = 0

# First window
#     for i in range(k):           # range(3) 0 1 2  
#         window_sum += arr[i]     # arr[0] = 2 then window_sum = 0+2=2, 2+1=3, 3+5=8 

#     max_sum = window_sum         #   8

# Slide the window
#     for i in range(k, len(arr)):      # (3,6)  i= 3,4,5
#         window_sum = window_sum + arr[i] - arr[i - k]   # 8 + arr[3] - arr [3-3]  ==> 8 + 1 - 2 = 7

#         if window_sum > max_sum:
#             max_sum = window_sum

#     return max_sum


# arr = [2, 1, 5, 1, 3, 2]

# print(max_sum(arr, 3))
