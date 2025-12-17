while True:
    try:
        n=int(input("Enter a positive number"))
        if n<=0 :
            raise ValueError("Number must be positive")
        print(f"Success {n}")
        break
    except ValueError as e:
        print(f"Error: {e}")