"""Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am
local time. The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the
best profit I could have made from 1 purchase and 1 sale of 1 Apple stock
yesterday.

No "shorting" - you must buy before you sell. You may not buy and sell in the
same time step (at least 1 minute must pass).
"""

# Brute force: try every combination of prices and keep track of the max diff
# between prices.
def get_max_profit(prices):
    """Return the daily maximum profit.

    >>> get_max_profit([10, 7, 5, 8, 11, 9])
    6
    """

    max_profit = 0

    # iterate through each possible buy_price
    for idx, buy_price in enumerate(prices):

        # since we have to buy before selling, use the inner loop to iterate
        # through each price that comes after the buy_price in the outer loop
        for sell_price in prices[idx + 1:]:
            
            # check the diff b/w each buy and sell prices
            profit = sell_price - buy_price

            # update max_profit if we can do better
            if profit > max_profit:
                max_profit = profit

    return max_profit

# Runtime: O(n^2)
# O(n) to loop thorough buy_prices; O(n-1) to loop through sell_prices.
# Outer loop goes through all times and prices, while the inner loop goes
# through one fewer price each time. The total number of steps is n + (n-1) +
# (n-2) ... + 2 + 1, or O(n^2/2), which is still O(n^2).


# Greedy algorithm: iterates through the problem space taking the optimal
# solution "so far," until it reaches the end. This approach is only optimal if
# the problem has "optimal substructure," which means stitching together
# optimal solutions to subproblems yields an optimal solution.
def get_max_profit2(prices):
    """Return the daily maximum profit.

    >>> get_max_profit2([10, 7, 5, 8, 11, 9])
    6
    """

    # keep track of variables and update as we iterate through the problem
    min_price = prices[0]
    max_profit = 0

    # iterate over the list once
    for current_price in prices:

        # make sure we're buying at the lowest price we've seen so far
        if current_price < min_price:
            min_price = current_price
        # or: min_price = min(min_price, current_price)
        
        # calculate profit for buying at min_price and selling at current_price
        profit = current_price - min_price

        # update max_profit if we can do better
        if profit > max_profit:
            max_profit = profit
        # or: max_profit = max(max_profit, potential_profit)

    return max_profit

# Runtime: O(n)


# Handle edge cases:
# If stock value stays the same? max_profit will return 0. That's ok.
# If stock value goes down all day? max_profit will return 0. That's not correct
# and the algorithm should return a negative profit (this is more accurate and
# less opinionated than throwing an error).
def get_max_profit3(prices):
    """Return the daily maximum profit.

    >>> get_max_profit3([10, 10, 10, 10, 10])
    0

    >>> get_max_profit3([10, 9, 8, 7, 6, 5])
    -1

    >>> get_max_profit3([10])
    Traceback (most recent call last):
        ...
    IndexError: Getting a profit requires at least 2 prices
    """

    # make sure we have at least 2 prices
    if len(prices) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # initialize min_price to the first price of the day
    min_price = prices[0]
    
    # initialize max_profit to the first profit we could get if we buy at the first
    # price and sell at the second price
    # this also works to find the smallest negative.
    max_profit = prices[1] - prices[0]

    # iterate over the list once starting with the second element
    # calculate profit first, before updating min_price
    for current_price in prices[1:]:

        # calculate profit for buying at min_price and selling at current_price
        profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, profit)

        # update min_price so it's the lowest price we've seen so far
        min_price = min(min_price, current_price)
        
    return max_profit

# Runtime: O(n)
# Space complexity: O(1)


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
