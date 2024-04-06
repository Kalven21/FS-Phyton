varname =2
variable = ""
varstring= "kevin"
varnum = 2
varname =True
print(varstring)
print(variable + str(varname))

age = 20
if age<20:
    print("youre young")
elif age>20:
    print("no worrys jeje")
else:
    print("okay, dont fear")

#insted of being aclled array is named list
colors = ["red","green","blue"]
print(colors)
colors.append("yellow")
print(colors)
colors.remove("blue")
print(colors)
print(colors[2])

for x in colors:
    print(x)
    
#dictionarys
me ={
    "first_name": "Kevin",
    "last_name": "Zamora",
    "age": 20,
}
print(me)
#get a value
print(me["first_name"])
me["age"]=21
me["favorite_color"]="red"
print(me)

#funtions
def say_hello():
    print("say hello")
def say_goodbye(name,age):
    print("goodbye "+ name + " " + str(age))
    
#call functions
say_hello()
say_goodbye("Kevin",21)

#create a calculator

#functions
def print_menu():
    print("1)sum")
    print("2)substraction")
    print("3)multiplication")
    print("4)division")
    
#instructions
print_menu()
opt = int(input("Choose an option: "))
num1 = float(input("please provide me the first number: "))
num2 = float(input("please provide me the second number: "))

if opt == 1:
    total = num1 + num2
    print("the sum of the numbers is: " + str(total))
elif opt == 2:
    total = num1 - num2
    print("the substraction of the numbers is: " + str(total))
elif opt == 3:
    total = num1 * num2
    print("the multiplitation of the numbers is: " + str(total))
elif opt == 4:
    if num2 == 0:
        print("you cannot divide by zero")
    else:
        total = num1 / num2
        print("the division of the numbers is: " + str(total))
    