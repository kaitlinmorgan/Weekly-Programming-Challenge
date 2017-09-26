#Kaitlin Morgan
#RAM Hacks Programming Challenge #1
#9/26/17

#Simple solution - function for FizzBuzz spin off
def FizzBuzz():
    #Will loop through numbers 1-50 (51 is exclusive)
    for i in range(1,51):
        #Checks if number is divisible by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("RAMHacks")
        #Checks if number is divisible by 3
        elif i % 3 == 0:
            print("RAM")
        #Checks if number is divisible by 5
        elif i % 5 == 0:
            print("Hacks")
        #Prints non-divisble numbers with no modification
        else:
            print(i)

#Alternate solutions
def FizzBuzz2():
    numList = []
    #Adds numbers and modifications to list
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            numList.append("RAMHacks")
        elif i % 3 == 0:
            numList.append("RAM")
        elif i % 5 == 0:
            numList.append("Hacks")
        else:
            numList.append(i)
    #Prints the elements in the list
    for k in range(len(numList)):
        print(numList[k])
