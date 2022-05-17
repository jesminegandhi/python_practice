import random
import string

## Allow user input for how many EC2 instances they want names for
no_of_instances = input("Enter the number of EC2 instances : ")

## Allow user input for their Department name (Providing options for Marketing, Accounting or Finops)
dept_name = input("Enter your Department name (Marketing, Accounting, or FinOps) : ")

## Function for Random Name Generator including 2 characters, numbers and department name
def name_generator(no_of_instances, dept_name):
    list_of_names = []
    dept_name = dept_name.lower()
    
    ## Checking if the user entered a valid number
    if (no_of_instances.isdigit()) :
        no_of_instances = int(no_of_instances)
        
        ## Checking if the user entered from the options provided & giving permissions accordingly
        if(dept_name != 'marketing' and dept_name != 'accounting' and dept_name != 'finops'):
            print("You are not permitted to use Name Generator for your EC2 Instances!")

        else:
            for i in range(no_of_instances):
                name = dept_name + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + str(random.randint(0,1000))
                list_of_names.append(name)
            print(list_of_names)
    else:
        print("Please enter a valid number for EC2 instances")
    
    
## Checking with user input        
name_generator(no_of_instances,dept_name)
## Testcase 1
name_generator('5', 'marketing')
## Testcase 2
name_generator('4', 'support')