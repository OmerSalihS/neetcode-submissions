class Solution:
    def isPalindrome(self, s: str) -> bool:
        mylist=list(s)
        news=''
        count=-1
        total=0
        for i in mylist:
            if i.isalnum():
                news+=i.lower()
        return news==news[::-1]

        
        
        