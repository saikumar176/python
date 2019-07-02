n = int(input("Enter the value of n: "))
sums = 0
if n <= 0: 
   print("Enter a whole positive number!") 
else: 
   while n > 0:
        sums = sums + n
        n = n - 1;
print("Sum of first", "natural numbers is: ", sums)
