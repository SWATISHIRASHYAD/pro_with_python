class sample:
    
    def ispalindrome(self,num):
        new=0
        number=num
        while number!=0:
            rem=number%10
            new=new*10+rem
            number=number//10      #Integer division
        if new==num:
            return True
        else:
            return False
obj1=sample()
ans=obj1.ispalindrome(1231)
if ans:
    print("palindrome")
else:
    print("not palindrome")


