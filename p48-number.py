while True:
    try:
        x=int(input("What is x? "))
    except ValueError:
        print("x is not integer")

    else:
        break
print(f"x is: {x}")