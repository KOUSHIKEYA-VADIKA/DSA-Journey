num=int(input())
reverse=0
original=0
if(num<0):
    original=num
    sign=-1
    num=num*sign
while(num>0):
    lastdigit=num%10
    reverse=(reverse*10)+lastdigit
    num//=10

if(original<0):
    reverse=reverse*sign
print(reverse)