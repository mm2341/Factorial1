num=int(input("Please enter number: "))

factorial=1

for x in range(1,num+1):
    factorial=factorial*x

print("The factorial of",num, "is",factorial)
