name = input("Enter student name: ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
reg= input("Enter registration number: ")
dep = input("Enter department: ")
sub1 = float(input("Enter marks in subject 1: "))
sub2 = float(input("Enter marks in subject 2: "))
sub3 = float(input("Enter marks in subject 3: "))
sub4 = float(input("Enter marks in subject 4: "))
sub5 = float(input("Enter marks in subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5
print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("Date of Birth:", dob)
print("Registration Number:", reg)    
print("Department:", dep)
print("\nMarks in 5 subjects:", (sub1, sub2, sub3, sub4, sub5))
print("Total Marks:", total)
print("Percentage:", percentage, "%")
if percentage >= 90:
    print("Grade: Excellent")
elif percentage >= 75:
    print("Grade: Very Good")
elif percentage >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")