# Difference Array is used when we need to perform many range updates.

def range_update(n, l, r, value):

    diff = [0] * (n + 1)        # Create difference array

    diff[l] += value      # diff[1] += 6    
    diff[r + 1] -= value   # diff[4] -= 6               diff = [0, 6, 0, 0, -6, 0]  

    arr = [0] * n

    arr[0] = diff[0]

    for i in range(1, n):
        arr[i] = arr[i - 1] + diff[i]

    return arr


print(range_update(5, 1, 3, 6))



#Time Complexity: O(n)

# Multiple update

# def difference_array(n, updates):

#     diff = [0] * (n + 1)

#     for l, r, value in updates:

#         diff[l] += value
#         diff[r + 1] -= value

#     arr = [0] * n

#     arr[0] = diff[0]

#     for i in range(1, n):
#         arr[i] = arr[i - 1] + diff[i]

#     return arr


# updates = [
#     (1, 3, 5),
#     (2, 4, 2)
# ]

# print(difference_array(5, updates))