print 'how many numbers are you adding?'
userInput = int(raw_input())
total = 0
for x in range(userInput):
    print 'enter a number:'
    integer = int(raw_input())
    total = total + integer
print total

myFirstList = []
print 'how many numbers are you adding?' 
userInput = int(raw_input())
for x in range(userInput):
    print 'enter a number:'
    aList = int(raw_input())
    myFirstList.append(aList)
print myFirstList
   
print 'What number do you want to make a factorial of?'
userInput = int(raw_input())
total = 1
for x in range(1,userInput+1,1):
    total = total * x
print total

def factors(n):
    myList = []
    for x in range(1, n+1):
        if n % x == 0:
            myList.append(x)
    return myList
        
print 'What number do you want the factors of?'
print factors(int(raw_input())) 