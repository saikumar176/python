upper,lower=map(int,input().split())

for i in range(upper+1,lower):
  for j in range(2,i):
    if i%j==0:
      break
  else:
    print(i,end=" ")    
