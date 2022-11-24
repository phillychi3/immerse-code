class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10==0):
            return False
        llist = []
        for i in str(x):
            llist.append(i)
        if list(reversed(llist)) == llist:
            return True
        else:
            return False
            
        
