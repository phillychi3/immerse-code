# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        last = n
        while(first < last):
            between = first+(last-first)/2
            if isBadVersion(between):
                last = between
            else:
                first = between+1
                
        bad_version = isBadVersion(between)

        if bad_version == True:
            return int(between)
        else:
            return int(between) + 1