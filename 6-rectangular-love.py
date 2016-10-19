"""A crack team of love scientists from OkEros (a hot new dating site) have devised 
a way to represent dating profiles as rectangles on a two-dimensional plane.

They need help writing an algorithm to find the intersection of two users' love 
rectangles. They suspect finding that intersection is the key to a matching 
algorithm so powerful it will cause an immediate acquisition by Google or Facebook 
or Obama or something.

Write a function to find the rectangular intersection of two given love rectangles.

Love rectangles are always "straight" and never "diagonal." More rigorously: each 
side is parallel with either the x-axis or the y-axis.

They are defined as dictionaries like this:

    my_rectangle = {

        # coordinates of bottom-left corner
        'left_x': 1,
        'bottom_y': 5,

        # width and height
        'width': 10,
        'height': 4,

    }

Your output rectangle should use this format as well.
"""

def find_intersection(recA, recB):
    """Return the intersecting rectangle of two rectangles.

    >>> recA = {
    ... 'left_x': 0,
    ... 'bottom_y': 0,
    ... 'width': 4,
    ... 'height': 6,
    ... }

    >>> recB = {
    ... 'left_x': 3,
    ... 'bottom_y': 2,
    ... 'width': 5,
    ... 'height': 3,
    ... }

    >>> find_intersection(recA, recB) == {'width': 1, 'left_x': 3, 'bottom_y': 2, 'height': 3}
    True

    >>> recA = {
    ...     'left_x': 1,
    ...     'bottom_y': 1,
    ...     'width': 4,
    ...     'height': 3
    ...     }
    
    >>> recB = {
    ...     'left_x': 3,
    ...     'bottom_y': 3,
    ...     'width': 5,
    ...     'height': 4
    ...     }
    
    >>> find_intersection(recA, recB) == {'width': 2, 'left_x': 3, 'bottom_y': 3, 'height': 1}
    True

    >>> recA = {
    ...     'left_x': 1,
    ...     'bottom_y': 1,
    ...     'width': 4,
    ...     'height': 3
    ...     }
    
    >>> recB = {
    ...     'left_x': 6,
    ...     'bottom_y': 8,
    ...     'width': 5,
    ...     'height': 4
    ...     }
    
    >>> find_intersection(recA, recB) is None
    True
    """

    # initialize empty dict for results rectangle
    overlap = {}
    
    # calculate overlap's left_x as the highest ('rightmost') of the two lefts
    overlap['left_x'] = max(recA['left_x'], recB['left_x'])

    # calculate the lowest ('leftmost') end point minus the overlap's left
    overlap['width'] = min(recA['left_x'] + recA['width'],
                           recB['left_x'] + recB['width']) - overlap['left_x']

    # calculate overlap's bottom_y as the higher ('upmost') of the two bottoms
    overlap['bottom_y'] = max(recA['bottom_y'], recB['bottom_y'])

    # calculate the lowest end point minus the overlap's bottom
    overlap['height'] = min(recA['bottom_y'] + recA['height'],
                            recB['bottom_y'] + recB['height']) - overlap['bottom_y']

    # lastly, make sure the rectagles are overlapping
    if overlap['width'] <= 0 or overlap['height'] <= 0:
        return None


    return overlap

# Runtime: O(1)
# Space: O(1)


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"