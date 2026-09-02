#School Enrolment Checker
print("school enrolment checker")

#Get the student's information from the user
distance=float(input("How many km do you live from the school?"))
age=int(input("How old are you?"))
right_to_stay=input("Do you have the right to stay in New Zealand? (yes/no):")
international_fees=input("Will you pay international student fees? (yes/no):")

#Check the enrolment eligibility using if, elif and else
if age<18 and international_fees=="yes":
    print("You can enrol.")
elif distance<4 and age<18 and right_to_stay=="yes":
    print("You can enrol.")

#if enrolment conditions are not met, enrolment will be declined
else:
    print("You cannot enrol.")

#Assertion 1 : If age=17, distance=3, right_to_stay=yes, international_fees=no, the output should be "You can enrol."
#Assertion 2 : If age=20, distance=5, right_to_stay=yes, international_fees=yes, the output should be "You cannot enrol."