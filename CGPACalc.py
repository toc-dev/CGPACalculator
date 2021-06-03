import csv

while True:
    course_codes = []
    unit_loads = []
    course_grades = []
    
    student_name = (input("What is your name: "))
    #print(student_name)
    
    

    try:
        NoOfCourses = int(input("Enter number of courses: "))
    except ValueError:
        print("Please Enter A valid Value!")

    else:
        if NoOfCourses <= 0:
            print("enter a valid value:")
        else:
            CreditUnit = {}
            Grade = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
            points = []
            units = []

            for i in range(1, NoOfCourses+1):
                if i == 1:
                    oder = "st"

                elif i == 2:
                    oder = "nd"
                elif i == 3:
                    oder = "rd"
                elif i > 3:
                    oder = "th"
                

                while True:
                    course_code = input("Please type in the course title for " + str(i) + oder + " course: ")
                    course_codes.append(course_code)

                    grade_response = str(input('Enter Your grade for ' + course_code.upper() + ": ").upper())
                    course_grades.append(grade_response)
                    if (grade_response == 'A') or (grade_response == 'B') or (grade_response == 'C') \
                            or (grade_response == 'D') or (grade_response == 'E') or (grade_response == 'F'):
                        while True:

                            try:
                                unit_response = int(input("Enter the unit load: "))
                                unit_loads.append(unit_response)
                                if unit_response > 0:
                                    break
                                else:
                                    print("Zero Values are not allowed!")

                            except ValueError:
                                    print("Enter A valid Value (only numerals)")
                    else:
                        print("Err")

                    if grade_response == 'A':

                        point = Grade['A'] * unit_response
                        points.append(point)
                        units.append(unit_response)
                        break

                    if grade_response == 'B':
                        units.append(unit_response)
                        point = Grade['B'] * unit_response
                        points.append(point)
                        break

                    if grade_response == 'C':
                        units.append(unit_response)
                        point = Grade['C'] * unit_response
                        points.append(point)
                        break

                    if grade_response == 'D':
                        units.append(unit_response)
                        point = Grade['D'] * unit_response
                        points.append(point)
                        break

                    if grade_response == 'E':
                        units.append(unit_response)
                        point = Grade['E'] * unit_response
                        points.append(point)
                        break

                    if grade_response == 'F':
                        units.append(unit_response)
                        point = Grade['F'] * unit_response
                        points.append(point)
                        break

            # print(points)
            # print(units)
            TOTAL = sum(points)/sum(units)
            rounded_total = str(round(TOTAL, 2))

            print("Your CGPA is: " + str(round(TOTAL, 2)))
            with open(f"{student_name}.csv", 'w') as file:
                student_file = csv.writer(file)
                student_file.writerow([f'COURSE BREAKDOWN FOR {student_name.upper()}'])
                student_file.writerow(['Course_Code', 'Unit_Load', 'Grade'])
                for c in range(NoOfCourses):
                    student_file.writerow([course_codes[c].upper(), unit_loads[c], course_grades[c]])
                student_file.writerow([f"Your CGPA is {rounded_total}"])

            break
