"""You have a list of integers, and for each index you want to find the product
of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of
integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
"""

# Brute force: multiply the int at every index by the int at every nested_index,
# unless index == nested_index.
def get_products_of_all_ints_except_at_index(lst):
    """Return list of integer products except the integer at that index.

    >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
    [84, 12, 28, 21]
    """

    product = 1
    results = []

    for idx in range(len(lst)):
        for nested_idx in range(len(lst)):
            if idx != nested_idx:
                product *= lst[nested_idx]
        
        results.append(product)
        
        # reset product for the next idx
        product = 1

    return results

# Runtime: O(n^2), also resetting product each time we iterate through the lst


# Also brute force; a bit cleaner.
def get_products_of_all_ints_except_at_index2(lst):
    """Return list of integer products except the integer at that index.

    >>> get_products_of_all_ints_except_at_index2([1, 7, 3, 4])
    [84, 12, 28, 21]
    """

    # instantiate output list to hold products
    results = [1] * len(lst)

    # loop over list
    for idx in xrange(len(lst)):

        # get the product of all ints before each index 
        for nested_idx in lst[:idx]:
            results[idx] *= nested_idx

        # get the product of all ints after each index
        for nested_idx in lst[idx + 1:]:
            results[idx] *= nested_idx

    return results

# Runtime: O(n^2) still

# Greedy approach: break problem down into subproblems.
# Find the product of all ints before each index and work backwards to get the
# product of all ints after each index.
def get_products_of_all_ints_except_at_index3(lst):
    """Return list of integer products except the integer at that index.

    >>> get_products_of_all_ints_except_at_index3([1, 7, 3, 4])
    [84, 12, 28, 21]
    """

    # instantiate lists to hold products
    products_before_idx = [None] * len(lst)
    products_after_idx = [None] * len(lst)

    # for each int, find the product of all ints before it
    # store product each time and multiply that by the next int
    # then store that new product and keep going
    product = 1
    for i in range(len(lst)):
        products_before_idx[i] = product
        product *= lst[i]

    # same process going backwards to find product of all ints after int at idx
    product = 1
    for i in range(len(lst)-1, -1, -1):
        products_after_idx[i] = product
        product *= lst[i]

    # multiply the products at the same indices in each lst
    result = [None] * len(lst)
    for i in range(len(result)):
        result[i] = products_before_idx[i] * products_after_idx[i]

    return result

# Runtime: O(n)
# O(n) for products_before, O(n) for products_after, O(n) for result
# Space complexity: O(n) for three lists the size of the input lst


# Optimize by only making one new lst to store products and be the final output.
def get_products_of_all_ints_except_at_index4(lst):
    """Return list of integer products except the integer at that index.

    >>> get_products_of_all_ints_except_at_index4([1, 7, 3, 4])
    [84, 12, 28, 21]
    """

    # instantiate output list to hold products
    products = [None] * len(lst)

    # for each int, find the product of all ints before it
    product = 1
    for i in range(len(lst)):
        products[i] = product
        product *= lst[i]

    # for each int, find the product of all ints after it
    product = 1
    for i in range(len(lst)-1, -1, -1):
        # since each idx in products already has the product of all ints before it,
        # multiply current value by the product of all ints after it to store the
        # total product of all other ints
        products[i] *= product
        # then increment product to incude the current value
        product *= lst[i]

    return products

# Runtime: O(n)
# Space complexity: O(n)


# Handle edge cases:
# Input list contains zeroes? That's fine.
# Input list only has one integer? No products to return. Make sure len(lst) > 2.


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"