#Simple Calculator

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#chose an operation

choice= input("Enter operation(1/2/3/4): ")

#input two numbers

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

#perform chosen operation

if choice=='1':
 print(num1,"+",num2,"=",num1+num2)

elif choice=='2':
    print(num1,"-",num2,"=",num1-num2)

elif choice=='3':

    print(num1,"*",num2,"=",num1*num2)

elif choice=='4':
    print(num1,"/",num2,"=",num1/num2)

else:
        
        print("Invalid input please try again")


