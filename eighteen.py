less = int(input())
high = int(input())
 
for numb in range(less,high + 1):
   sum = 0
   temp = numb
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if numb == sum:
       print(numb)
