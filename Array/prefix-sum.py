# Prefix Sum stores the sum of elements from the beginning up to each index.

def PrefSum(arr):

    prefix = [0] * len(arr)      # to store the prefix sum   [0,0,0,0,0]

    prefix[0] = arr[0]    # initialize the first element. prefix = [2, 0, 0, 0, 0]

    for i in range(1, len(arr)):       # Adding present element with previous element. prefix[1] = prefix[0] + arr[1] (2+4)
        prefix[i] = prefix[i - 1] + arr[i]     

    return prefix


arr = [2, 4, 1, 5, 3]

print(PrefSum(arr))

#Time Complexity: O(n)
# Current prefix sum = Previous prefix sum + Current array element
# prefixSum[0] = 2
# prefixSum[1] = 2 + 4 = 6
# prefixSum[2] = 2 + 4 + 1 = 7
# prefixSum[3] = 2 + 4 + 1 + 5 = 12
# prefixSum[4] = 2 + 4 + 1 + 5 + 3 = 15