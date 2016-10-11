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

# Recursive, top down approach.
# For each choice about how to many time to include a coin of each denomination,
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


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"