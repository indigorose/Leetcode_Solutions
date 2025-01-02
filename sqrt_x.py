'''
69. sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

Looping through the range of numbers to search for the n value is considered a brute force solution.

An alternative is considering the use of binary search.

It is proposed to cut the range in half and theorise which end of the range to consider.

For example if x = 7, we can theorise that the result or square root is between 2 and 3, as their respective squares are
4 and 9. however as we cannot return decimal places, the result is 2 as we round down.

If we look at the range of 0-7 and divide 7 by half, we have 3.5, the midpoint of the range. As with the previous brute
force strategy, 3.5 squared is larger than 7. Therefore, we must reduce the search further to look for the result
between 0 and 3. For argument's sake, use whole integers.

The aim of this to find where the midpoint value is closest to x and return.

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r-l) // 2)
            # If the midpoint squared is greater than x, we search on the left side
            if m**2 > x:
                r = m - 1
            # Else we search on the right side.
            elif m**2 < x:
                l = m + 1
                res = m # This may be the result
            else:
                return m
        #   return the result either way if the while loop fails.
        return res



