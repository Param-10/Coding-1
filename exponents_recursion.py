def Calculatepower(base,exponent):
    if exponent == 0:
        return 1
    else:
          return base*Calculatepower(base,exponent-1)

def main():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter a whole number between 2 and 50: "))
    while exponent < 2 or exponent > 50:
        exponent = int(input("Invalid. Please enter a whole number between 2 and 50: "))
    answer=Calculatepower(base,exponent)
    print(f"{base} raised to the power of {exponent} is {answer}")
    
if __name__ == "__main__":
    main()
