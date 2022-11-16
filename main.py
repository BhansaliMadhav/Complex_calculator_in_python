# Importing required modules and created functions to get functions like decimal and maths
import datetime
import sys
import addition
import countprime
import division
import exponential
import hcf
import inversetrigonometric
import lcm
import log
import nthroot
import primefactors
import subtraction
import multiplication
import trigonometric
import factorial

user_input_calculation = ""
condition = "False"
# General introduction about program

print("Hello welcome ")
# Printing date and time
print(f"Today is {datetime.date.today()}")
# Defining the purpose and supported calculation
print("This is a calculator for two numbers and supports addition, subtraction, multiplication, division, logarithmic, exponential, root(nth), trigonometric, inverse trigonometric, factorial, HCF(Highest common factor), LCM(least common multiple)")
# Asking for support
print("This program is created by Madhav Vijay Bhansali if you liked the program support the creator 😊")


# Defining main function for calculation


def calculation_to_be_executed(type_of_calculation):
    # Using at  time user input so that the user could be specifically told what and how must the values be entered and thus making program more user-friendly
    global condition
    try:
        if type_of_calculation.upper() == "EXIT":
            sys.exit(0)
        # Condition for addition
        elif type_of_calculation.upper() == "ADDITION":
            addition.addition()

        # Condition for subtraction
        elif type_of_calculation.upper() == "SUBTRACTION":
            subtraction.subtraction()

        # Condition for multiplication
        elif type_of_calculation.upper() == "MULTIPLICATION":
            multiplication.multiplication()

        # Condition for division
        elif type_of_calculation.upper() == "DIVISION":
            division.division()

        # Condition for log
        elif type_of_calculation.upper() == "LOGARITHMIC" or type_of_calculation.upper() == "LOG":
            log.log()

        # Condition for exponential calculation
        elif type_of_calculation.upper() == "EXPONENTIAL" or type_of_calculation.upper() == "EXPONENT":
            exponential.exponential()

        # Condition for root supports even  decimal roots which are really difficult to calculate
        elif type_of_calculation.upper() == "ROOT":
            nthroot.nthroot()

        # Condition for trigonometric calculation
        elif type_of_calculation.upper() == "TRIGONOMETRIC":
            trigonometric.trigonometric()

        elif type_of_calculation.upper() == "INVERSE TRIGONOMETRIC":
            inversetrigonometric.inversetrigonometric()

        # Condition for calculation of factorial
        elif type_of_calculation.upper() == "FACTORIAL":
            factorial.factorial()
        # Code to find the greatest common factor
        elif type_of_calculation.upper() == "HCF":
            hcf.hcf()
        elif type_of_calculation.upper() == "LCM":
            lcm.lcm()
        elif type_of_calculation.upper() == "COUNT PRIME":
            countprime.count()
        elif type_of_calculation.upper() == "PRIME FACTORS" or type_of_calculation == "primefactors":
            primefactors.prime_factors()
        else:
            print("The given function is not supported")
            execution()
    # Exceptions to prevent application from crashing
    except ValueError:
        print("Enter appropriate values only")
    except IndexError:
        print("Enter only two values separated by comma")
    except OverflowError:
        print("Enter only in supported range you know that the number is too big")


# Using while loop so that user need not open program again and again


def execution():
    global user_input_calculation
    while user_input_calculation != "exit" or user_input_calculation != "Exit" or user_input_calculation != "EXIT":
        user_input_calculation = input("Enter calculation to be processed\n")
        # Condition to continue  the program
        calculation_to_be_executed(user_input_calculation)
        change_calculation()


def change_calculation():
    # While loop to ask user whether he wants to change type of calculation
    while True:
        user_change_type_of_calculation = input("Do you want to change type of calculation[y/n]")
        if user_change_type_of_calculation == "n":
            print("Thankyou for using my program if you like it please support for more such exciting and useful programs")
            calculation_to_be_executed(user_input_calculation)
        elif user_change_type_of_calculation == "y":
            print("To exit program type exit or enter new variables")
            print("Thankyou for using my program if you like it please support for more such exciting and useful programs")
            execution()
# Starting the execution of the program


execution()
# Program would be improved later on and more functions would be added
