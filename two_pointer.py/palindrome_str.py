s="level"
i=0
j=len(s)-1

while i<j:
    if s[i]!=s[j]:
        print("not palindrome")
        
    i+=1
    j-=1
print("palindrome")