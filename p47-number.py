try:
    x=int(input("What is x? "))
   
except ValueError:
    print("x is not integer")
else:

   print(f"x is: {x}")