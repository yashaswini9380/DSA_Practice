# Kadane's Algorithm finds the maximum sum of a continuous subarray.

def maxSubarraySum(arr):
    res = arr[0]

    for i in range(len(arr)):
        current_sum  = 0

        for j in range(i, len(arr)):
            current_sum  = current_sum  + arr[j]

            res = max(res, current_sum ) 

    return res


arr = [2, 3, -8, 7, -1, 2, 3]

print(maxSubarraySum(arr))