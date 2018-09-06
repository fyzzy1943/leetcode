
def search(needle, haystack):

    haystack.sort()
    print(haystack)
    l = 0
    h = len(haystack)-1
    while l <= h:

        mid = int((l+h)/2)
        if haystack[mid] == needle:
            return mid
        if haystack[mid] < needle:
            l = mid+1
        else:
            h = mid-1

    return -1

t1 = [2, 4, 5, 7, 1, 23, 4, 24, 534, 456, 34, 6 ,3]
# t1.sort()
# print(t1)

# print(len([1]))

print(search(24, t1))