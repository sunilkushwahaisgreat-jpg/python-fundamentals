def calc(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    
    if operation == "sub":
        return num1 - num2
    
    if operation == "mul":
        return num1 * num2
    
    if operation == "div":
        if num2 == 0:
            return "Error! Cannot Divide by Zero"
        return num1 / num2

    return "Invalid operation"

#Q2

def calculate_average(marks):
    """
    Calculates the average of a list.

    This function takes a list of numbers, sums them up, and divides by the 
    total count to find the average.

    Parameters:
    marks (list): A list of integers or floats representing the students marks.

    Returns:
    float: The calculated average of the marks,or 0 if the list is empty.
    """
    if not marks:
        return 0
    
    return sum(marks) / len(marks)

#Q3

def find_topper(students):
    """
    Identifies student with highest marks.

    Parameters:
    students(dict):A dictionary in which key is student_name,
    values is student_marks

    Returns
    str:The name of Topper.
    list:A list of name if there is a tie in marks.
    str:"No Student data available" if dictionary is empty.

    """
    # Handle empty dictionary
    if not students:
        return "No Student data available"
    
    # Find the highest mark value
    max_mark=max(students.values())
    
    # Find all student with highest mark
    toppers=[name for name,mark in students.items() if mark==max_mark]
    
    # Return results based on tie or unique Toppers
    if len(toppers)==1:
        return(toppers[0]) #Returns Just single topper
    else:
        return toppers #Returns multiple toppers
