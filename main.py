calculator_running=True

while calculator_running:
    print("===Python calculator===")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")  
    print("5.Exit")
    choice = int(input("Enter your choice:")) 
    if choice==1:
         print("ADDITION")
         first_number=int(input("enter the first number:"))
         second_number=int(input("enter the second number:"))
         result= first_number + second_number
         print(" The Result is:",result)
    elif choice==2:
         print("SUBTRACTION")
         first_number=int(input("enter the first number:"))
         second_number=int(input("enter the second number:"))
         result= first_number - second_number
         print(" The Result is:",result)
    elif choice==3:
         print("MULTIPLICATION")
         first_number=int(input("enter the first number:"))
         second_number=int(input("enter the second number:"))
         result= first_number * second_number
         print(" The Result is:",result)
    elif choice==4:
         print("DIVISION")
         first_number=int(input("enter the first number:"))
         second_number=int(input("enter the second number:"))
         result= first_number / second_number
         print(" The Result is:",result)

    elif choice==5: 
         calculator_running = False
         print("Thank you for using the calculator!")
    else:
         print("Invalid choice")

