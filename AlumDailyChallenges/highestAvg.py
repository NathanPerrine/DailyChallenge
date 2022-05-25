def highest_avg(students):
    '''students should be a list of lists, [0] should be the name and [1] should be the grade'''
    best_student, best_average = "", 0

    student_dict = {}
    # Calculate averages for all students
    for student in students:
        # Student already seen at least once
        if student[0] in student_dict:
            student_dict[student[0]]['grades'].append(int(student[1]))
            average = sum(student_dict[student[0]]['grades']) / len(student_dict[student[0]]['grades'])
            student_dict[student[0]]['avg'] = average 

            if average > best_average:
                best_average = average 
                best_student = student[0]

        else:
            student_dict[student[0]] = {'avg' : student[1], 'grades' : [int(student[1])]}

    return (best_student, student_dict[best_student])


students_list = [["Mark", "100"], ["Jacob", "90"], ["Mark", "22"], ["Jake", "81"]]
print(highest_avg(students_list))
