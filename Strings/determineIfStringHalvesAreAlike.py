class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=0
        b=0
        l={'a','e','i','o','u','A','E','I','O','U'}
        for i in range(len(s)//2):
            if s[i] in l:
                a+=1 
        for i in range(len(s)//2,len(s)):
            if s[i] in l:
                b+=1
        if a==b:
            return True
        else:
            return False