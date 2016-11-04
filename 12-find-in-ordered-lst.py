"""Suppose we had a list of n integers in sorted order. How quickly could we 
check if a given integer is in the list?
"""

def binary_search(search_lst, value):
    """Return number of tries to find a value in a list using binary search.

    >>> binary_search([x for x in range(101)], 2)
    7

    >>> binary_search([1, 2, 3, 4, 5, 6, 7], 10)
    False

    """

    # reassign the input so we're not overwriting the function parameter
    lst = search_lst

    # initialize counter 
    counter = 0
    
    while lst:
        # find the index of the midpoint in the list
        i = len(lst) / 2

        # increment counter
        counter += 1

        if value == lst[i]:
            return counter

        # determine whether our value is in the first half of the list
        elif value < lst[i]:
            lst = lst[:i]        
        
        # or the second half of the list
        else:
            lst = lst[i + 1:]

    return False

# Runtime: O(log n)
# Space: O(n)


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"