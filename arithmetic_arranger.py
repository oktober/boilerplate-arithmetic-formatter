def arithmetic_arranger(problems, solutions=False):
  arranged_problems = ""
  # if there are more than 5 problems, return an error
  if len(problems) > 5:
    return "Error: Too many problems."
    
  first_operand, operator, second_operand = [], [], []  
  for item in problems:
    # break the individual problem into pieces using the space
    pieces = item.split(" ")
    
    # if there are incorrect operators, return an error
    if pieces[1] not in ("+", "-"):
      return "Error: Operator must be '+' or '-'."
    # if there is anything other than digits in the operands, return an error
    elif not pieces[0].isdigit() or not pieces[2].isdigit():
      return "Error: Numbers must only contain digits."
    # if any operand is more than 4 digits, return an error
    elif len(pieces[0]) > 4 or len(pieces[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
      
    # add the pieces to their appropriate lists  
    first_operand.append(pieces[0])
    operator.append(pieces[1])
    second_operand.append(pieces[2])
    
  # the first line
  for index in range(len(problems)):
    # output 2 spaces
    arranged_problems += " " * 2
    # if the first_operand item is longer than the second_operand item
    if len(first_operand[index]) >= len(second_operand[index]):
      # output first_operand[index]
      arranged_problems += first_operand[index]
    else:
      # otherwise, output a number of spaces equal to the difference between the larger number (second_operand) and the smaller one (first_operand)
      arranged_problems += " " * (len(second_operand[index]) - len(first_operand[index]))
      # output the first_operand value
      arranged_problems += first_operand[index]
    # output 4 spaces if this isn't the last value
    if index < len(problems) - 1:
      arranged_problems += " " * 4
      
  # output a new line
  arranged_problems += "\n"

  # the second line
  for index in range(len(problems)):
    # output the operator plus 1 space
    arranged_problems += operator[index] + " "
    # if the second_operand has more digits than the first_operand:
    if len(second_operand[index]) >= len(first_operand[index]):
      # output the second_operand value
      arranged_problems += second_operand[index]
    else:
      # otherwise, output a number of spaces equal to the difference between the larger number (first_operand) and the smaller one (second_operand)
      arranged_problems += " " * (len(first_operand[index]) - len(second_operand[index]))
      # output the second_operand value
      arranged_problems += second_operand[index]
    # output 4 spaces if this isn't the last value
    if index < len(problems) - 1:
      arranged_problems += " " * 4
            
    # output a new line
  arranged_problems += "\n"

  # the third line
  for index in range(len(problems)):
    # output dashes equal to (2 + the length of the longest operand)
    arranged_problems += '-' * (2 + max(len(first_operand[index]), len(second_operand[index])))
    # output 4 spaces if this isn't the last value
    if index < len(problems) - 1:
      arranged_problems += " " * 4

 # if the solutions flag is True
  if solutions:
    # output a new line
    arranged_problems += "\n"
    
    # loop over the problems
    for index in range(len(problems)):
      # output one space
      arranged_problems += " "
            
      solution = 0
      # calculate the solution
      if operator[index] == "+":
        solution = int(first_operand[index]) + int(second_operand[index])
      else:
        solution = int(first_operand[index]) - int(second_operand[index])
                    
      # find the longest operand
      longest_operand = max(len(first_operand[index]), len(second_operand[index]))
      
      # if the length of the solution is smaller than the longest operand
      if len(str(solution)) <= longest_operand:
        # add an extra space
        arranged_problems += " "
        # add any additional spaces
        arranged_problems += " " * (longest_operand - len(str(solution)))
        
      # output the solution
      arranged_problems += str(solution)
      # output 4 spaces if this isn't the last value
      if index < len(problems) - 1:
        arranged_problems += " " * 4
        
  return arranged_problems
