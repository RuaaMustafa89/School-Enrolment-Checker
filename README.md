The School Enrolment Checker program uses KISS (Keep It Simple Stupid) principle, as the program uses if, elif and else statements to check if the student can enrol.
The program also uses 'and' to check multiple conditions at once (DRY principle).
The code is easy to read as it has meaningful variable names such as age, distance, right_to_stay etc.
The program then asks the user to enter information (distance, age, right to stay in New Zealand and about international student fees).
The distance input is 'float' because the distance can contain a decimal.
Once the program collects the user's information, it uses conditional statements to check whether the student meets the enrolment requirements.
If student is under 18 AND will pay international student fees, they can be enrolled. If the student lives less than 4km from the school, is under 18 AND has the right to stay in New Zealand, they can enrol. If neither of these conditions are met, the enrolment is declined. The output is either 'You can enrol' or 'You cannot enrol'.
One improvement would be to place the enrolment inside a function, to make the program easier to reuse and maintain.
