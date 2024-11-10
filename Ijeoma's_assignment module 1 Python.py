# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:57:39 2024

@author: DELL
"""
"""The random module contains functions and methods that helps generate random integers
and other data structures such as lists"""
import random 

#Create a list containing 500 names using a list comprehension
names = ["Employee_" + str(i) for i in range(1, 501)]
print(names)

#Generating random worker data - gender and salary using the random module using a function.
def generate_data():
    #The choice method randomly selects one value from a collection - numbers or strings
    gender = random.choice(['Female','Male'])
    salary = random.randint(6000, 32000)
    """Minimum salary in the project description is $7,500
       Maximum salary is $30,000"""
    #return a dictionary that contains the names, genders, and salaries of workers
    return {"name":random.choice(names), "gender":gender, "salary":salary}

"""Save the result of the function in a list named employees. It will contain all the information of 400 workers.
The employees variable will store a list of dictionaries"""
employees = [generate_data() for i in range(400)]

#CREATING PAYMENT SLIPS
try:
    #Creating an empty list
    payment_slips = []

    for employee in employees:
        payment_slip = {} #Creating an empty dictionary to store employee name, salary, and level.
        payment_slip["name"] = employee["name"]
        payment_slip["salary"] = employee["salary"]

        # Conditional statements to assign employee levels as described in the project
        if 10000 < employee["salary"] < 20000:
            payment_slip["level"] = "A1"
        if 7500 < employee["salary"] < 30000 and employee["gender"] == "Female":
            payment_slip["level"] = "A5-F"
        #Appending/adding each slip to the payment_slips list
        payment_slips.append(payment_slip)

#This block will only be executed if there's an error processing the try block
except Exception as e:
    print("An error occurred", e)

#View employees and their payment slips
print(employees,"\n\n\n") #After printing the employees variable, create 3 new lines.
print(payment_slips)


"""Why Some Workers Might Not Get Assigned Levels:
*Salary Range:

Workers with salaries less than or equal to $10,000 or greater than or equal to $20,000 do not meet the first 
condition.

Workers with salaries less than or equal to $7,500 or greater than or equal to $30,000 do not meet the second 
condition.

*Gender Requirement:

The second condition only applies to female workers. Male workers with salaries between $7,500 and $30,000 
do not meet the "A5-F" level condition."""