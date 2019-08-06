question = input("Ask your question: ")                                 #the code will take your question/statement as the input

import random

a = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) #A random number will then be generated

if (a == 1):                                #different values of variable 'a' will effect the program. The different values of 'a' will give the answer.
    print("It is certain.")
elif (a == 2):
    print("It is decidedly so.")
elif (a == 3):
    print("Without a doubt.")
elif (a == 4):
    print("Yes - definetly.")
elif (a == 5):
    print("You may rely on it.")
elif (a == 6):
    print("As i see it, yes.")
elif (a == 7):
    print("Most likely.")
elif (a == 8):
    print("Outlook good.")
elif (a == 9):
    print("Yes.")
elif (a == 10):
    print("Signs point to yes.")
elif (a == 11):
    print("Reply hazy, try again later")
elif (a == 12):
    print("Ask again later")
elif (a == 13):
    print("Better not tell you now.")
elif (a == 14):
    print("Cannot predict now.")
elif (a == 15):
    print("Concentrate and ask again.")
elif (a == 16):
    print("Don't count on it.")
elif (a == 17):
    print("My reply is no.")
elif (a == 18):
    print("My sources say no.")
elif (a == 19):
    print("Outlook not so good.")
elif (a == 20):
    print("Very doubtful.")

print("Do you want to ask again?")
ans = input("")
while ans == "yes":                                         #A while statement to execute the program again if the user wants to ask a question again
    question = input("Ask Your question: ")
    a = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    if (a == 1):
        print("It is certain.")
    elif (a == 2):
        print("It is decidedly so.")
    elif (a == 3):
        print("Without a doubt.")
    elif (a == 4):
        print("Yes - definetly.")
    elif (a == 5):
        print("You may rely on it.")
    elif (a == 6):
        print("As i see it, yes.")
    elif (a == 7):
        print("Most likely.")
    elif (a == 8):
        print("Outlook good.")
    elif (a == 9):
        print("Yes.")
    elif (a == 10):
        print("Signs point to yes.")
    elif (a == 11):
        print("Reply hazy, try again later")
    elif (a == 12):
        print("Ask again later")
    elif (a == 13):
        print("Better not tell you now.")
    elif (a == 14):
        print("Cannot predict now.")
    elif (a == 15):
        print("Concentrate and ask again.")
    elif (a == 16):
        print("Don't count on it.")
    elif (a == 17):
        print("My reply is no.")
    elif (a == 18):
        print("My sources say no.")
    elif (a == 19):
        print("Outlook not so good.")
    elif (a == 20):
        print("Very doubtful.")

    print("Do you want to ask again?")
    ans = input("")

if (ans == "no"):                               #If the user does not want to ask another question, they can type in "no" and the program will stop and give a reply "Okay, thank you!" 
    print("Okay, thank you!")

end = input("")                                 #So that the program does not stop working.

###Working of the code- 
# the program takes a statement and then generates a random number from 1-20 and then stores it in variable 'a' and then it runs through 
# the conditional statements and executes the statement which meets the condition and gives the answer. After this, the program asks the user 
# if they want to continue or not. Then the while statement comes in. If the user types "yes" then the while loop executes the code again. 
# If the user types "no" then the program replies with a note and stops.###
