
# d = {
#         101: "A",
#         102: "B",
#         103: "C",
#         104: "D",
#         105: "E",

#     }
# choices = """ 
# 101,102,103,104,105
#  """
# user_inp = int(input("Enter a choice:- "))
# val = d.get(user_inp)
# print(val)


def addition(x, y):
    """ ADDITION """
    return x + y

def subtraction(x, y):
    """ SUBTRACTION """
    if x < y:
        return("First number should be greater than Second number")
    else:
        return x - y

def multiplication(x, y):
    """ MULTIPLICATION """
    return x * y

def division(x, y):
    """ DIVISION """
    try:
        return x / y
    except ZeroDivisionError:
        return("Denominator cannot be zero")

def no_negative_value(x,y):
    """ NO NEGATIVE VALUES ARE ALLOWED """
    if x < 0 or y < 0:
        print("No negative values are allowed")
    else:
        final_res = r(a1, a2)
        print("Final result is:- ", final_res)



dict_football_clubs = {1:"Arsenal", 2:"Man City", 3:"Liverpool", 4:"Chelsea", 5:"Man U", 6:"Tottenham"}

def get_val(val):
    """ GET KEY FROM VALUE """
    for key, value in dict_football_clubs.items():
        if val == value:
            return key

   
class Student():
    """ STUDENT DETAILS """
    def __init__(self) :
        self.Name = input("Enter name:- ")
        self.Age =  int(input("Enter age:- "))
        self.student_details()

    def student_details(self):
        """ Show Student Detials """
        print (f""" 
        Name :- {self.Name}
        Age :-  {self.Age}
         """)


                # METHOD 1


dict_of_operation = {1:addition, 2:subtraction, 3:multiplication, 4:division, 5:Student, 6:get_val}
while True:
    print(""" 
    Please select one of the choices:-
    1.addition
    2.subtraction
    3.multiplication
    4.division
    5.Student
    6.Get Key Form Value
    7.Exit
     """)
    
    user_inp = int(input("Enter a choice:- "))

    r = dict_of_operation.get(user_inp)
    
    if r:
        if user_inp == 1:
            a1 = float(input("Enter first number:- "))
            a2 = float(input("Enter second number:- "))
            no_negative_value(a1,a2)
            addition(a1,a2)
            
        elif user_inp == 2:
            a1 = float(input("Enter first number:- "))
            a2 = float(input("Enter second number:- "))
            no_negative_value(a1,a2)
            subtraction(a1,a2)
        elif user_inp == 3:
            a1 = float(input("Enter first number:- "))
            a2 = float(input("Enter second number:- "))
            no_negative_value(a1,a2)
            multiplication(a1,a2)

        elif user_inp == 4:
            a1 = float(input("Enter first number:- "))
            a2 = float(input("Enter second number:- "))
            no_negative_value(a1,a2)
            division(a1,a2)

        # Student Details are created and shown
        elif user_inp == 5:
            Stud_obj = r()
            
        # Get key from value
        elif user_inp == 6:
            val = input("Enter a Football Club Name :-")
            a = get_val(val)
            if a:
                print(f"Value:- {val} is present at Key:-{a}")
            else:
                print("Fotball Club name not present in the dictionary..!")

    # Exit
    else: 
        user_inp == 7
        print("Thank you for using switchcase....!")
        break



                # METHOD -2

dict_of_operation = {1:addition, 2:subtraction, 3:multiplication, 4:division, 5:Student,6:get_val}
while True:
    print(""" 
    Please select one of the choices:-
    1.addition
    2.subtraction
    3.multiplication
    4.division
    5.Student
    6.Get Key Form Value
    7.Exit
     """)

    user_inp = int(input("Enter a choice:- "))

    r = dict_of_operation.get(user_inp)

    # Student Details are created and shown
    if r:
        if user_inp == 5:
            Stud_obj = r()
     # Get key from value
        elif user_inp == 6:
            val = input("Enter a Football Club Name :-")
            a = get_val(val)
            if a:
                print(f"Value:- {val} is present at Key:-{a}")
            else:
                print("Fotball Club name not present in the dictionary..!")


    # Addition ,Subtraction, Multiplication,Division, NO NEGATIVE VALUES ALLOWED
        else:
            a1 = float(input("Enter first number:- "))
            a2 = float(input("Enter second number:- "))
            if a1 < 0 or a2 < 0:
                print("No negative values are allowed")
            else:
                final_res = r(a1, a2)
                print("Final result is:- ", final_res)
    # Exit
    if user_inp == 7:
        print("Thank you for using switchcase....!")
        break


""" 
-------------------------------OUTPUT METHOD 1---------------------------------------------
		ADDITION
Enter first number:- 5
Enter second number:- -5
No negative values are allowed

Enter a choice:- 1
Enter first number:- 5
Enter second number:- 5
Final result is:-  10.0

	SUBTRACTION
Enter a choice:- 2
Enter first number:- 5
Enter second number:- 6
Final result is:-  First number should be greater than Second number

Enter a choice:- 2
Enter first number:- 6
Enter second number:- 5
Final result is:-  1.0

	MULTIPLICATION
Enter a choice:- 3
Enter first number:- 54
Enter second number:- 54
Final result is:-  2916.0

	DIVISION
Enter a choice:- 4
Enter first number:- 1
Enter second number:- 0
Final result is:-  Denominator cannot be zero

Enter first number:- 7
Enter second number:- 3
Final result is:-  2.3333333333333335

	STUDENT 
Enter a choice:- 5
Enter name:- Abhijeet
Enter age:- 26

        Name :- Abhijeet
        Age :-  26
		
	GET KEY
Enter a choice:- 6
Enter a Football Club Name :-Man City
Value:- Man City is present at Key:-2

	Exit
Enter a choice:- 7
Thank you for using switchcase....!

--------------------------------------OUTPUT METHOD 2----------------------------------------------------------
	ADDITION
Enter a choice:- 1
Enter first number:- 4
Enter second number:- -5
No negative values are allowed

Enter a choice:- 1
Enter first number:- -5
Enter second number:- -5
No negative values are allowed

Enter a choice:- 1
Enter first number:- 54
Enter second number:- 24
Final result is:-  78.0

	SUBTRACTION
Enter a choice:- 2
Enter first number:- 5
Enter second number:- 6
Final result is:-  First number should be greater than Second number

Enter a choice:- 2
Enter first number:- -5
Enter second number:- -5
No negative values are allowed

Enter a choice:- 2
Enter first number:- 58
Enter second number:- 47
Final result is:-  11.0

	MULTIPLICATION
Enter a choice:- 3
Enter first number:- -5
Enter second number:- 6
No negative values are allowed

Enter a choice:- 3
Enter first number:- 5
Enter second number:- 5
Final result is:-  25.0

	DIVISION
Enter a choice:- 4
Enter first number:- 1
Enter second number:- 0
Final result is:-  Denominator cannot be zero

Enter a choice:- 4
Enter first number:- 5
Enter second number:- 2
Final result is:-  2.5

	STUDENT 
Enter a choice:- 5
Enter name:- Aniket
Enter age:- 32

        Name :- Aniket
        Age :-  32
		
	GET KEY
Enter a choice:- 6
Enter a Football Club Name :-Man U
Value:- Man U is present at Key:-5

Enter a choice:- 6
Enter a Football Club Name :-fesfds
Fotball Club name not present in the dictionary..!

	EXIT
Enter a choice:- 7
Thank you for using switchcase....!





 """

   

    
    
        
   

    

