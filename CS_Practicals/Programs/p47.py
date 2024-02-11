students = {}
students['001'] = {'roll_number': 1, 'name': 'John Doe', 'marks': 85}
students['002'] = {'roll_number': 2, 'name': 'Jane Smith', 'marks': 90}
students['003'] = {'roll_number': 3, 'name': 'Mary Johnson', 'marks': 95}
admission_number = input("Enter an admission number: ")
if admission_number in students:
    print("Admission Number:", admission_number)
    print("Roll Number:", students[admission_number]['roll_number'])
    print("Name:", students[admission_number]['name'])
    print("Marks:", students[admission_number]['marks'])
else:
    print("No student with that admission number was found.")
