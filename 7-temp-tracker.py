"""You decide to test if your oddly-mathematical heating company is fulfilling its 
All-Time Max, Min, Mean and Mode Temperature Guarantee.

Write a class TempTracker with these methods:

    1. insert() - records a new temperature
    2. get_max() - returns the highest temp we've seen so far
    3. get_min() - returns the lowest temp we've seen so far
    4. get_mean() - returns the mean of all temps we've seen so far
    5. get_mode() - returns a mode of all temps we've seen so far

Optimize for space and time. Favor speeding up the getter functions (get_max(), 
get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

get_mean() should return a float, but the rest of the getter functions can return 
integers. Temperatures will all be inserted as integers. We'll record our 
temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110.

If there is more than one mode, return any of the modes.
"""

# Use ahead-of-time (eager) approach so we're storing certain variables before 
# they're called, so getter functions return pre-computed values in O(1) time,
# even though there's a higher cost on insertion.
class TempTracker(object):
    """Track temperatures and quickly return min, max, mean, and mode.

    >>> tracker = TempTracker([])
    >>> tracker.insert(30)
    >>> tracker.insert(20)
    >>> tracker.insert(60)
    >>> tracker.insert(20)
    >>> tracker.insert(75)
    >>> tracker.insert(20)
    >>> tracker.insert(55)    
    >>> tracker.get_max()
    75
    >>> tracker.get_min()
    20
    >>> tracker.get_mean()
    40.0
    >>> tracker.get_mode()
    20

    >>> tracker = TempTracker([5, 5, 5, 10, 20])
    >>> tracker.insert(25)
    >>> tracker.get_min()
    5
    >>> tracker.insert(10)
    >>> tracker.get_mode()
    5
    """

    def __init__(self, tracker=None):
        # Note: use None, not [], for the default value when instantiating the 
        # default object. Don't use a mutable default argument because the empty
        # list is made onec and shared by all calls, so we chek for a value and
        # assign a new emtpy list each time a tracker is instantiated.
        tracker = tracker or []
        assert isinstance(tracker, list)

        self.tracker = tracker
        
        self.counter = {}
        self.max_counts = 0

        # if the object is instantiated with a default list, initialize the
        # variables based on those values
        if tracker:
            self.maximum = max(tracker)
            self.minimum = min(tracker)
            self.total = sum(tracker)
            for temp in self.tracker:
                self.counter[temp] = self.counter.get(temp, 0) + 1
                if self.counter[temp] > self.max_counts:
                    self.mode = temp
                    self.max_counts = self.counter[temp]

        else:
            self.maximum = None
            self.minimum = None
            self.total = 0

    def insert(self, temp):
        """Record new temperature; update max, min, mean, mode."""

        # initialize or update maximum temp
        if (self.maximum is None) or (temp > self.maximum):
            self.maximum = temp
        
        # initialize or update minimum temp
        if (self.minimum is None) or (temp < self.minimum):
            self.minimum = temp

        # update total sum for calculating mean
        self.total += temp

        # use a dict to keep track of the frequency of each temp
        self.counter[temp] = self.counter.get(temp, 0) + 1
        if self.counter[temp] > self.max_counts:
            self.mode = temp
            self.max_counts = self.counter[temp]

        # assert correct data type passed into method; add to lst
        assert isinstance(temp, int)
        self.tracker.append(temp)

        # return self.tracker

    def get_max(self):
        """Return the maximum recorded temperature."""
        
        return self.maximum

    def get_min(self):
        """Return the minimum recorded temperature."""
        
        return self.minimum

    def get_mean(self):
        """Return the mean temperature as a float."""

        return self.total / float(len(self.tracker))

    def get_mode(self):
        """Return the mode temperature, which could be any mode."""
        
        return self.mode

# Runtime: O(1)
# Space: O(1)


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"