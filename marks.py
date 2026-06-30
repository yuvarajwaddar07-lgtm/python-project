print("1")
print("2")
print("3")
print("4")
option = int(input("Enter your register number"))

name1=("Yuvaraj")
name2=("shubham")
name3=("Karthik")
name4=("Pramod")

marks1= 431
marks2=486
marks3=490
marks4=452

if(option in[1, 2, 3, 4]):
    num1=str("Enter your name")
    if(option == 1):
        print("Candate name:",name1)
        print("Obtained Marks:",marks1)
    elif(option == 2):
         print("Candate name:",name2)
         print("Obtained Marks:",marks2)
    elif(option == 3):
         print("Candate name:",name3)
         print("Obtained Marks:",marks3)
    elif(option == 4):            
        print("Candate name:",name4)
        print("Obtained Marks:",marks4)
else:
    print("Not Found!!")