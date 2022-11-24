class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        anlist = []
        word = ""
        self.go(word,n,0,0,anlist)
        return anlist
        
        
    def go(self,word,n,c1,c2,anlist):
        if c1 == n and c2 == n:
            anlist.append(word)
            return
        if c1 < n:
            self.go(word+'(',n,c1+1,c2,anlist)
        if c2 < c1:
            self.go(word+')',n,c1,c2+1,anlist)
        
        