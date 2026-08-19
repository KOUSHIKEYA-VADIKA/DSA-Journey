num=int(input())
reverse=0
while(num>0):
    lastdigit=num%10
    reverse=(reverse*10)+lastdigit
    num//=10
print(reverse)