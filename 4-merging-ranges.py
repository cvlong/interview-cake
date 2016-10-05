"""Your company built an in-house calendar tool called HiCal. You want to add a
feature to see the times in a day when everyone is available.

To do this, you'll need to know when any team is having a meeting. In HiCal, a
meeting is stored as tuples of integers (start_time, end_time). These integers
represent the number of 30-minute blocks past 9:00am.

For example:

  (2, 3) # meeting from 10:00 - 10:30 am
  (6, 9) # meeting from 12:00 - 1:30 pm

Write a function condense_meeting_times() that takes a list of meeting time ranges
and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from
multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the
numbers representing our time ranges. Here we've simplified our times down to the
number of 30-minute slots past 9:00 am. But we want the function to work even for
very large numbers, like Unix timestamps. In any case, the spirit of the challenge
is to merge meetings where start_time and end_time don't have an upper bound.
"""

def condense_meeting_times(mtgs):
    """Return a list of condensed meeting ranges.

    >>> condense_meeting_times([(1, 3), (2, 4)])
    [(1, 4)]

    >>> condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]
    """

    # sort lst so any meetings that can be merged will always be adjacent
    mtgs.sort()

    # initialize merged lst with the earliest meeting
    merged = [mtgs[0]]

    # if the end time of the first meeting overlaps the start time of the second
    # meeting, then merge the two meetings into one time range, which begins at
    # the first meeting's start, and ends at the later of the two end times
    for current_start, current_end in mtgs[1:]:

        # compare to the last meeting we've looked at in the merged lst
        merged_start, merged_end = merged[-1]

        # if the current and last meetings overlap, use the latest end time
        if current_start <= merged_end:
            merged[-1] = (merged_start, max(merged_end, current_end))

        # if the current meeting doesn't overlap, add it to the merged lst
        else:
            merged.append((current_start, current_end))

    return merged

# Runtime: O(n log n)
# O(n log n) worst case for sorting, then O(n) to walk through the list. Could
# solve in O(n) on presorted list.
# Space: O(n), since in the worst case if no meetings overlap, we're recreating
# an identical list to the input list.


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"