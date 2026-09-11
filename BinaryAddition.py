num1 = '11'
num2 = '11110101'
#------------------------------------------------------
X = max(len(num1), len(num2))
num1=num1.zfill(X)
num2=num2.zfill(X)

s = ''
c = 0
for i in range(-1, -max(len(num1),len(num2))-1, -1):
    s1=(int(num1[i])+int(num2[i])+c)%2
    c=(int(num1[i])+int(num2[i])+c)//2
    s+=str(s1)

if c:
    s+='1'
s = s[::-1]

print(s)