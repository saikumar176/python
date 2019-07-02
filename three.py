sets=["a","e","i","o","u"]
set2=["?","!","&","$","#","@"]
z=input()
if z in sets:
  print("Vowel")
elif z in set2:
  print("Invalid")
else:
  print("Consonant")
