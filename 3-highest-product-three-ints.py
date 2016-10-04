"""Given a list_of_ints, find the highest_product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""

# Sort the list to get the highest numbers.
def get_highest_product(nums):
    """Return the highest product from three ints in a list.

    >>> get_highest_product([6, 3, 5, 1, 7, 2, 4])
    210
    """

    product = 1

    # find the max values in the list, pop them and multiply together   
    for i in range(3):
        product *= nums.pop(nums.index(max(nums)))

    return product


# Sort the list and evaluate the highest & lowest products of two ints (this
# accounts for two negative ints having a higher positive product).
def get_highest_product2(nums):
    """Return the highest product from three ints in a list.

    >>> get_highest_product2([6, 3, 5, 1, 7, 2, 4])
    210

    >>> get_highest_product2([1, 10, -5, 1, -100])
    5000
    """

    # sort in place so we can access nums by index
    nums.sort()

    # compare the products of the two lowest nums and two highest nums
    # to account for two negative ints with the highest product
    if nums[0] * nums[1] > nums[-2] * nums[-1]:
        return nums[0] * nums[1] * nums[-1]
    else:
        return nums[-3] * nums[-2] * nums[-1]

# Runtime: O(n log n)


# Keep track of highest/lowest ints and highest/lowest products of two ints
# to check against highest_three up to date as we walk through the list.
def get_highest_product3(nums):
    """Return the highest product from three ints in a list.

    >>> get_highest_product3([6, 3, 5, 1, 7, 2, 4])
    210

    >>> get_highest_product3([1, 10, -5, 1, -100])
    5000
    """

    if len(nums) < 3:
        raise Exception('Need at least three ints to calculate')

    highest = max(nums[0], nums[1])
    lowest = min(nums[0], nums[1])

    highest_pair = nums[0] * nums[1]
    lowest_pair = nums[0] * nums[1]

    highest_three = nums[0] * nums[1] * nums[2]

    # start at the third element, since we prepopulated our tracking variables
    # with elements at the first two indeces already
    for num in nums[2:]:

        # check whether there's a new max product of three ints
        highest_three = max(highest_three,
                            num * highest_pair,
                            num * lowest_pair)

        # check whether there's a new max product of two ints
        highest_pair = max(highest_pair, num * highest, num * lowest)
        
        # check whether there's a new min product of two ints
        lowest_pair = min(lowest_pair, num * lowest, num * highest)

        # reset highest and lowest values
        highest = max(num, highest)
        lowest = min(num, lowest)


    return highest_three

# Runtime: O(n)
# Space: O(1), but creating a lot of additional lists to track high/low values


# Handle edge cases:
# Highest product of 4 items? Highest product of k items?
# If our highest product is really big, it could overflow
# def get_highest_product4(nums, k):
    """Return the highest product from 'k' ints in a list.

    >>> get_highest_product4([6, 3, 5, 1, 7, 2, 4], 4)
    210

    >>> get_highest_product4([1, 10, -5, 1, -100, 8, 12, 0], 5)
    480000
    """


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"