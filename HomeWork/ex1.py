# OS2 Python Programming 2019b
#
# File:ex1.py
# ==============================================================================
# Writen by: Eran Safadel, Batya Pollack
#
# Run: ex1.py using Python interpreter
#%%--------------------------------------------------------------------------%%#
#--------------------foo1-----------------------------
#function takes to numbers and return the sum of digit in number one on a number two
def foo1():
 var1 = input("Insert Number 1\n")
 var2 = input("Insert Number 2\n")
 count = 0
 for i in var1:
  for j in var2:
    if i == j:
     count += 1

 print(count)
#---------------------foo2-------------------------------
#function insert string to stack, delete string on stack and print all stack without the first char
def foo2():
    stack = []           #create stack
    while True:
        c = input("Enter choice\n")
        if c == 'i':
            string = input("Insert string\n")
            string = string[1:]  #The strings without the first character
            stack.append(string)    #Insert the string into the stack
        elif c == 'e':
            if len(stack) > 0:
                stack.pop() #Remove the string from the stack
            else:
                print("Stack is empty")
                exit(0)
        elif c == 'p':
            index = 0
            for n in stack:
                print(index, ": ", stack[index])
                index += 1

        else:
            break
#--------------------foo3---------------------------------------------
#function find last servant
def foo3():
    list = []
    del_cel = 1
    for i in range(1, 101):
        list.append(i)
    while len(list) != 1:
        if max(list) != list[del_cel]:
            list.pop(del_cel)
            del_cel = (del_cel + 1) % len(list)
        else:
            list.pop(del_cel)
            del_cel = 1
    print("The last servant is:",list)
#------------------foo4-----------------------------------------------
#function find caesar cipher
def foo4():
    str = input("Enter a string\n")
    for i in str:
        if i.isalpha():
            if i.isupper():
                i = (chr(ord(i) + 32))
            i = (chr(ord(i) - 84))
            i = (chr(ord(i) % 26))
            i = (chr(ord(i) + 97))
            i = (chr(ord(i)))
            print(i, end="")
        else:
            print(i, end="")
    print()
#---------------------main----------------------------------------------
while True:
    c = input ("Insert number 1-4:")
    if c == '1':
        foo1()
    elif c == '2':
        foo2()
    elif c == '3':
        foo3()
    elif c == '4':
        foo4()
    else:
        break;














