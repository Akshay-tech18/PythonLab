def naturalnumbers(num):
    if num==1:
        return num
    else:
        return num + naturalnumbers(num-1)
    
num = int(input("Enter the natural numbers : "))

if num<1:
    print("Entered number is not a natural number. Please try again")
else:
    sum = naturalnumbers(num)
    print(f"sum of {num} is = {sum}")