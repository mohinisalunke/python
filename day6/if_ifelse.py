
# if statement:

number = 10
if number:
    print("Got a true expression value",)
    print(number)


#elseif
    
number = 0
if number:
    print("Got a true expression value")
    print(number)
else:
    print("Got a false expression value",number)
O\p == Got a false expression value

 #elif:
    
number = 10
if number == 100:
    print("the number is eqaul to 100",)
    print(number)
elif number == 150:
    print("the number is equal to 150",)
    print(number)
elif number == 200:
    print("the number is equal to 200",)
    print(number)
else:
    print("Got a different value.")
O\p == got a different value.

# single line statement :

obj = (1,2,3)

if len(obj) == 4:
    print(True)
else:
    print(False)

print(True) if len(obj) == 4 else print(False)

##################################################

number = int(input('Enter a number from user:'))

if number % 2:
    print("Number %d is an odd number" %(number))
else:
    print("Number %d is an even number" %(number))
    
###################################################

numbers = list(range(11))

if len(numbers)>10:
    print("numbers has more than 10 items")
    if numbers[0] % 2 == 0:
        print("Number has first item even")
    else:
        print("Number has first item odd")
elif number[1]%2 == 1 :
    print("Number has second item in even.")
elif len(numbers) < 10:
    print("numbers has less than 10 times.")
else:
    print("all above conditions are false!!")
print("this is outside block.")

#####################################################

obj = (1,2,3)

if len(obj) == 3
    print(True)
else:
    print(False)
    
# single line statement
print(True) if len(obj) == 4 else print(False)

#############################################################
