print("Enter numerator:")
num=input()
print("Enter denominator:")
den=input()
try:
   res=int(num)/int(den)
except:
   print("Division by zero not allowed") 
else:
   print(res)
