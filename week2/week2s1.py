
# myNumber = 25


# > greater
# < less than
# >= greater or equal to
# <= less or equal to

# if the number is greater than 25, we need to print "greater than 25"
# if the number is less than 25, we need to print less than 25
# if(myNumber > 25):
#     print("greater than 25")

# if(myNumber < 25):
#     print("less than 25")

# if(myNumber > 25):
#     print("greater than 25")
# else:
#     print("less than 25")

# if the number is greater than 25, we need to print "greater than 25"
# if the number is 25, we need to print number is 25
# if the number is less than 25, we need to print less than 25


# != not equal
# == equal to

# if(myNumber > 25):
#     print("greater than 25")
# elif(myNumber == 25):
#     print("number is 25")
# else:
#     print("less than 25")


# name = input("Enter your name: ")
# greeting = "Hai "

# print(greeting + name)


# def GreetUser(greeting):
#     name = input("Enter your name: ")
#     print(greeting + " " + name)


# GreetUser("Good morning")

# GreetUser("Good Evening")

# GreetUser("Hello")


# def sayHello (nameOfPerson = "defaultName"):
#     print("Hello " + nameOfPerson)


# sayHello()
# sayHello("Najma")

# <p>This is a paragraph</p>

# def make_tags(tag, tagValue):
#     print("<" + tag + ">" + tagValue + "</" + tag + ">")


# make_tags("p", "this is a paragraph")
# make_tags("h2", "this is header of type h2")
# make_tags("h6", "this is a header of type h6")

# <p>this is a paragraph</p>
# <h2>this is header of type h2</h2>
# <h6>this is a header of type h6</h6>


# def sayHello (nameOfPerson = "Faith"): # nameOfPerson = "Najma"

#     print("Hello " + nameOfPerson)


# sayHello("Navin")


# def CalculateSum(num1, num2):
#     total = num1 * num2
#     return total


# answer = CalculateSum(5, 27)

# print("total is", answer)

# answer2 = CalculateSum(5, 147)


# class activity from week2

password = input("Enter your password: ")

if(len(password) < 5):
    print("not a valid password")
elif(password.isnumeric()): #if password is just numbers, we say not valid
    print("password is not valid!")
elif(password == "secret123"):
    print("Access Granted")
else:
    print("Access denied")