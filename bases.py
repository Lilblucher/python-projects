#!/usr/bin/env python3


"""
Created on Fri Jun 9 2023

@author: clive
"""

print("""
Welcome  to my number system programme
if you want to know how to use it enter the help command 
enter quit to exit the programme      
""")


def conTobase2(value):
    try:
        numToint = int(value)
        tobase = bin(numToint)
        v1 = len(tobase)
        result = tobase[2:v1]  
        print(f"{numToint} in base2 is {result}") 
    except ValueError:
        print(inputerror)
        

def conTobase8(value):
    try:
        numtoint = int(value)
        tobase8 = oct(numtoint)
        len8 = len(tobase8)
        result8 = tobase8[2:len8]
        print(f"{numtoint} in base8 is {result8}")
    except ValueError:
        print(inputerror)
        

def conTobase16(value16):
    try:
        numtoint16 = int(value16)
        tobase16 = hex(numtoint16)
        len16 = len(tobase16)
        result16 = tobase16[2:len16]
        print(f'{numtoint16} in base16 is {result16}')
    except ValueError:
        print(inputerror)
  

inputerror = "please kindly enter a number"
Main = True 
que = "Enter number you want to convert to "
print("_" * 50)

while Main:
    print("\nWhich number system do you want to enter[base2,base8, or base16]")
    mainfun = input(">")
    
    if mainfun.lower() == "quit":
        print("\nThank you for using my programme")
        print("_" * 55)
        Main = False
    
    
    elif mainfun.lower() == "base2":
        print(f"\n{que}base2")
        Value = input(">> ")
        if Value.lower() == "quit":      
            print("_" * 52)
            Main = False
        else:
            conTobase2(Value)
        
    elif mainfun.lower() == "base8":
        print(f"\n{que}base8")
        Value = input(">> ")
        if Value.lower() == "quit":
            print("_" * 53)
            Main = False
        else:
            conTobase8()
       
    
    elif mainfun.lower() == "base16":
        print(f'\n{que}base16')
        value16 = input('>> ')
        if value16.lower() == "quit":
            print("_" * 52)
            Main = False
        else:
            conTobase16(value16)
    elif mainfun.lower() == "help":
    	print("""
When entering the name of the number system.
Do not leave a space inbetween the word and the number example;
'base2' instead of 'base 2'
If you want to exit the programme, just enter the 'quit' command   
    	 """)
    	print("#" * 54)
    	Main = False
    
    

