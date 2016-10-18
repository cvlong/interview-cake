"""Imagine you landed a new job as a cashier...

Your quirky boss found out that you're a programmer and has a weird request about
something they've been wondering for a long time.

Write a function that, given:

  1. an amount of money
  2. a list of coin denominations

computes the number of ways to make amount of money with coins of the available
denominations.

Example: for amount=4(4c) and denominations=[1,2,3] (1c, 2c, and 3c), your program
would output 4 - the number of ways to make 4c with those denominations:

  1. 1c, 1c, 1c, 1c
  2. 1c, 1c, 2c
  3. 1c, 3c
  4. 2c, 2c
"""

# Recursive, top-down approach.
# Starts with final value for amt and recursively breaks the rest of the problems
# into subproblems with smaller values for amt.
# For each choice about how to many times to include a coin of each denomination,
# must solve the subproblem of how many ways we can get the remaining amount
# from the other coins.
def make_change(amt_left, denominations, index = 0):
    """Return the number of ways to make amt with coins of specific denominations.

    >>> make_change(4, [1,2,3])
    4
    """

    # base case: we hit the right amount
    if amt_left == 0: return 1

    # base case: we overshot the amount by using too many coins
    if amt_left < 0: return 0

    # base case: we've used all possible denominations
    if index == len(denominations): return 0

    # print "checking ways to make %i with %s" % (amt_left, denominations[index:])

    # choose current coin
    coin = denominations[index]

    # initialize the counter
    counter = 0

    # count the possibilities for each combination using the current coin
    while amt_left >= 0:
        counter += make_change(amt_left, denominations, index + 1)
        amt_left -= coin

    return counter


# But this method often duplicates work. Avoid duplicate work and bring down
# time cost using memoization: wrap the function in a class that stores an 
# instance variable self.memo that maps inputs to outputs.


# Recursive, top-down approach using memoization.
class Change:

    def __init__(self):
        self.memo = {}

    def make_change2(self, amt_left, denominations, index = 0):
        """Return the number of ways to make amt with coins of specific denominations.

        >>> make_change2(4, [1,2,3])
        4
        """

        # check self.memo to see if we've already made this calculation
        if (amt_left, index) in self.memo:

            print "grabbing memo[%i %i]" % amt_left, index

            return memo[(amt_left, index)]

        # base case: we hit the right amount
        if amt_left == 0: return 1

        # base case: we overshot the amount by using too many coins
        if amt_left < 0: return 0

        # base case: we've used all possible denominations
        if index == len(denominations): return 0

        # print "checking ways to make %i with %s" % (amt_left, denominations[index:])

        # choose current coin
        coin = denominations[index]

        # initialize the counter
        counter = 0

        # count the possibilities for each combination using the current coin
        while amt_left >= 0:
            counter += make_change(amt_left, denominations, index + 1)
            amt_left -= coin


        # if not in self.memo, save the results of any calculation to self.memo
        self.memo[(amt_left, index)] = counter
        
        return counter

# Runtime: O(n*m)
# Space: O(n*m) for self.memo; O(m) for the call stack
# In each case, n is the size of amt_left and m is the num of items in denominations
# Becase the function is recursive, it will build up a large call stack as a new
# frame gets pushed onto the call stack each time the function calls itself; if
# the stack has limited amount of space before you encounter a stack overflow error.


# Bottom-up, iterative approach.
# Compute the smaller values of amt first and use those to iteratively compute the
# answer for higher values.


def make_change3(amt, denominations):
    """Return the number of ways to make amt with coins of specific denominations.

    >>> make_change3(4, [1,2,3])
    4

    We use a bottom-up algorithm to build up a table ways_of_making_n_cents such
    that ways_of_making_n_cents[k] is how many ways we can get to k cents using our 
    denominations. We start with the base case that there's one way to create the 
    amount zero, and progressively add each of our denominations.

    The number of new ways we can make a higher_amount when we account for a new 
    coin is simply ways_of_making_n_cents[higher_amount - coin], where we know that 
    value already includes combinations involving coin (because we went bottom-up, 
    we know smaller values have already been calculated).
    """

    # initialize ways for making change for amount 'n' at each index
    ways_of_making_n_cents = [0] * (amt + 1)
    ways_of_making_n_cents[0] = 1

    # iterate over each denomination available
    for coin in denominations:

        # find ways to make each amt with current coin
        # don't look below value of coin; calculate up to max amt
        for value in range(coin, amt + 1):

            # this is the amt we need to make for each current coin
            remainder = value - coin

            # keep track of each value between coin and amt (inner loop)
            # for each coin in denominations (outer loop)
            ways_of_making_n_cents[value] += ways_of_making_n_cents[remainder]

    return ways_of_making_n_cents[amt]

# Runtime: O(n*m)
# Space: O(n), where n is the size of amt.


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"