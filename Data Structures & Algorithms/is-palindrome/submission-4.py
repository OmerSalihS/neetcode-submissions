class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring=""
        for x in s:
            if x.isalnum()==True:
                newstring+=x.lower()
        print(newstring,newstring[::-1])
        if newstring==newstring[::-1]:
            return True
        else:
            return False



        
        
        