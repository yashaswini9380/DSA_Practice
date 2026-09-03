# using sorting
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))