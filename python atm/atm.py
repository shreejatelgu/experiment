
print("******welcome custommer to our atm*******\n\n PLEASE INSERT YOUR CARD")
balance = 1000
password=1234
choice=0

pin=int(input("enter your pin:"))
if pin==password: 

    while choice!=5:
        print("******menu******")
        print("1.deposit")
        print("2.withdraw")
        print("3.check balance")
        print("4.change password")    
        print("5.exit")

        choice=int(input("enter your choice  :"))
        if choice==1:
         dep=int(input("enter your amount of deposition :"))
         balance=balance+dep
         print("the depoisition is been done and your  balance:",balance)
        elif choice==2:
         draw =int(input("enter your amount of withdrawal :"))
         balance=balance-draw 
         print("your current balance is :",balance)
        elif choice==3:
         print("your current balance is :",balance)
        elif choice==4:
         new_pin=int(input("enter your new 4-digit pin :"))
         password=new_pin
         print("your pin has been changed")
        elif choice==5:
          print("thank you for banking with us")
else:
  print("invalid pin")

