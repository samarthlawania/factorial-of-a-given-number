a = int(input("Enter the number"))
i = 0
f = 1
if a < 0 :
    print("Sorry,the factorial of given number is not defined")
elif a == 0 :
    print("The factorial of 0 is 1")
else :
    for i in range (1,a+1):
        f = f * i
    print(f)


