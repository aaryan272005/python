'''Write a program to accept marks of the 'n' number of students and display them in a sorted manner '''
# NOTE:On Hold
# Initialize an empty list 
marks = []

# Ask the user how many marks of students they want to list
no_students= int(input("How many marks of students would you like to list? "))

# Use a for loop to get the studnets names from the user
for i in range(no_students):
    students=(input(f"Enter marks of students {i+1}: "))
    students.append(marks)


# Display the list students entered by the user
print(f"The list students you entered is:\t{marks}")
