class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        td = []
        for i , j in zip(s ,t):
            if i in sd:
                if sd[i] != j:
                    return False
            elif j in td:
                return False
            sd[i] = j 
            td.append(j)
        return True
                