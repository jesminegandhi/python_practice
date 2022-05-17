## Python program where a user can enter a numerical grade and then get a letter grade (A, B, C, D, F) returned. 

## Allow user input for numerical percentage/grade
grade = int(input("Enter a numerical percentage/grade :"))

##Checking if grade is between 90-100 & printing corresponding letter grade(A) for it
if grade >= 90 and grade <=100: 
    print("Your Grade is A - Excellent")

##Checking if grade is between 80-89 & printing corresponding letter grade(B) for it    
elif grade >= 80 and grade <= 89:
    print("Your Grade is B - Very Good")

##Checking if grade is between 70-79 & printing corresponding letter grade(C) for it
elif grade >= 70 and grade <= 79:
    print("Your Grade is C - Improvement Needed")

##Checking if grade is between 60-69 & printing corresponding letter grade(D) for it    
elif grade >= 60 and grade <= 69:
    print("Your Grade is D - Close Fail")    

##Checking if grade is between 0-59 & printing corresponding letter grade(F) for it
elif grade >= 0 and grade <= 59:
    print("Your Grade is F - Fail") 

##If numerical value is greater than 100 and less than 0; priting the corresponding error   
else:
    print("Please enter a valid value! \nNumerical percentage/grade should be greater than 0 and less than 100.")
    