from ast import Or
from operator import truediv
from tkinter.messagebox import YES
from urllib import response
import os
clear = lambda: os.system('cls')

cis = " 1. Cis deduction" "\n"
income = "2. Income tax & National Insurance" "\n"

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main():
    print("\n")
    print(color.BOLD, color.BLUE +'Hello Jack!' + color.END)
    print("What calculation would you like to complete today?\n") 
    print(cis,"\n",income,"\n")
    
def body():    
    main()
    inputText = input()

    if '1' in inputText.lower():
        print("CIS DEDUCTION - REGISTERED (y) or UNREGISTERED (n)? \n")
        
        inputText = input()
        if  'y' in inputText.lower():
            clear()
            print("\nCIS Deductions - Registered Subcontractor\n")
            cisdeduct = float(input("Please enter your annual taxable income for cis tax deductions: \n£"))
            tax = 0.20
            remainder = cisdeduct - (cisdeduct * tax)
            print("\nCIS DEDUCTIONS at 20% =", "£",cisdeduct * tax)
            print("\nYou have £", remainder, "of your salary left")
            print("Your monthly pay is", color.BOLD, color.BLUE, "£", remainder / 12, color.END)
            print("\n Return to Menu? (y/n)") 
            inputText = input()
            if 'y' in inputText.lower():
                body()
            elif 'n' in inputText.lower():
                print("\n Calculate Correct Deductions")
                earnedyear = float(input("What have you earned this year? \n£"))
                expenses = float(input("Please enter the total amount of allowable expenses: \n£"))
                annualincome = (earnedyear - expenses)
                print(annualincome - (annualincome * 0.20))
###############################################
#### needs to be like above "what have you earned this year", but then run through the next if statements (one for income and NI deductions).
# calculation from that should be taken away from the actual CIS deduction taken


### new idea - use a float input naming convention
# i.e.
# a = floatinput("what have you earned this year")
# b = floatinput("Please enter total amount of allowable expenses")
# c = floatinput("How much have you paid in CIS deductions from 04/22 - 04/23")
# yearlyincome = a - b
# yearlyincome ifs (if yearlyincome <= 12570:
#                                       tax = (yearlyincome *0.0))
# c
                                 
        elif 'n' in inputText.lower():
            clear()
            print("\nCIS Deductions - Unregistered Subcontractor\n")
            cisdeduct = float(input("Please enter your annual taxable income for cis tax deductions: \n£")) 
            tax = 0.30
            remainder = cisdeduct - (cisdeduct * tax)
            print("\nCIS DEDUCTIONS at 20% =", "£",cisdeduct * tax)
            print("\nYou have £", remainder, "of your salary left")
            print("Your monthly pay is", color.BOLD, color.BLUE, "£", remainder / 12, color.END)
            print("\n Return to Menu? (y/n)") 
            inputText = input()
            if 'y' in inputText.lower():
                body()
            
                
    elif '2' in inputText.lower():
            clear()
            income = float(input("Please enter your yearly taxable income for income tax deductions:\n £"))
            tax = 0.0 
        
            if income <= 12570:
                tax = (income * 0.0)
            elif income <= 50270:
                tax = (income - 12569) * 0.1325 + (income - 12570) * (.20)
            elif income <= 150000:
                tax = .40 * (income - 37700) + 5026
            elif income > 150000:
                tax = .45 * (income - 150000) + 44920
            remainder = income - tax    
            print("You pay £",tax, "in income tax and NI deductions\n")
            print("You have £", remainder, "of your annual salary left") 
            print("Your monthly pay is", color.BOLD, color.BLUE, "£", remainder / 12, color.END)
            print("\n Return to Menu? (y/n)") 
            inputText = input()
            if 'y' in inputText.lower():
                body()       
    # National Insurance deductions with header
    
    else:
        f = inputText.lower()
        if f != '1-2':
            clear()
            print(color.BOLD, color.GREEN, "Invalid Selection", color.END)
            body()
body()