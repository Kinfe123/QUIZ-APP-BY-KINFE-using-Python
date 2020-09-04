
import datetime
now = datetime.datetime.now()
time = now.strftime(" %H:%M:%S")

score = 0
ques_len = 10
print(f"You have started at : {time}")
print("\t\t\tWelcome To KinFish Quiz!!!!")
import sys 
from time import sleep

def animate():
    animation = "|/-\\-->"
    
    for i in range(len(animation)):
        sleep(0.25)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        
        


name = input("Enter your name: ")
confirm = input("Are you ready to take the quiz? /yes/no/  ").upper()
if confirm == "YES":
    print("\t\tYou have successfully get in to Quiz Zone!!...Here the there are 10 quiz and 1 bonus below!!")
    quiz1 = input("1.What is the name of the langauge that i programmed this quiz?  ").upper()
    print("Checking the answer......")
    animate()
    if quiz1 == "PYTHON":
       
        print("CORRECT")
        score+=1
    else:
        print("INCORRECT")
    
    quiz2 = input("2.Which of the following is an extention name for the python language? \n(a).py \n(b).html \n(c).cs \n(d).cpp\nAnswer: ").lower()
    print("Checking the answer......")
    animate()
    if quiz2 == "a":
        score+=1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
    
    quiz3 = input("3.What general purpose built-in method that help us to know the length of the elements in th list and character inside of string? ").upper()
    print("Checking the answer......")
    animate()
    if quiz3 == "LEN":
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
    quiz4 = input("4.Which of the following is unordered collection of the unique items? \n(a)List\n(b)Dictionary\n(c)Set\n(d)Arrays\nAnswer: ").lower()
    print("Checking the answer......")
    animate()
    if quiz4 == "c":
        score+=1
        print("CORRECT!!")
    else:
        print("INCORRECT!")
    quiz5 = input("5.What is the data structure with in immutable version of the set: ").upper()
    print("Checking the answer......")
    animate()
    if quiz5 == "FROZEN SET":
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT")
    quiz6 = input("6.Can Tuple be used as Key value in the dict? \n(a)True\n(b)False\nAnswer: ").lower()
    print("Checking the answer......")
    animate()
    if quiz6 == "a":
        score+=1
        print("CORRRECT!!") 
    else:
        print("INCORRECT!!")
    quiz7 =input("7.What symbole help us to unpack multiple elements from tuples: ")
    print("Checking the answer......")
    animate()
    if quiz7 == "*":
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
    quiz8 = input("8.Which one of the collection data type is immutable? \n(a)Tuples\n(b)Lists\n(c)Dictionaries\n(d)Arrays\nAnswer: ").lower()
    print("Checking the answer......")
    animate()
    if quiz8 == "a":
        score+=1
        print("CORRRECT")
    else:
        print("INCORRECT")
    quiz9 = input("9.What reserved keyword help us to create a class: ").lower()
    print("Checking the answer......")
    animate()
    if quiz9 == "class":
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT")
    quiz10 = input("10.Which one specifies a set of the rule for writing Python code for maximum readability?\n(a)DRY\n(b)PEP\n(c)OPP\n(d)PHS\nAnswer: ").lower()
    print("Checking the answer......")
    animate()
    if quiz10 == "b":
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT")
    print("\t\t\tBonus Question!") 
    quiz11 = input("11.Which one is help us to create an instance of the actual class? \n(a)Class\n(b)Dict\n(c)Object\n(d)this\nAnswer: ").lower()
    print("Checking the answer......")
    animate()
    if quiz11 == "c":
        score+=1
        print("CORRECT!!")
        
    else: 
        print("INCORRECT!!")
        
    print("Calculating the result........")
    animate()
    print(f"Hey {name}, You got {score} / {ques_len}")
    mark = (score/ques_len)*100
    print(f"MARK: {mark}")
    if mark >= 50:
        print(f"Hey {name}...You have passed the Exam!!")
    else:
        print("You failed!!!")
    print(f"Thanks for using our QUIZ app by Python!!...From Developer: KINFE MICHAEL TARIKU!") 
else:
    print(f"Hey {name}, You can over anytime to take the test!!!")
    
