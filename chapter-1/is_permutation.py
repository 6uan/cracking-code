
#  checks to see if str1 and str2 are permutations of eachother

def is_permuation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    # stores frequency of each char in str1
    freq = {}

    for char in str1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for char in str2:
        if char not in freq:
            return False
        freq[char] -= 1
        # if frequency of single letter exceeds that of str1
        if freq[char] < 0:
            return False
    return True


def is_permuation_sorted(str1, str2):
    if len(str1) != len(str2):
        return False
    
    return(sorted(str1) == sorted(str2))

str1 = "race"
str2 = "cear"
print(is_permuation(str1, str2))
print(is_permuation_sorted(str1, str2))
