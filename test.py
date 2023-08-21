# Author: Gurmehar Singh
# Student ID: 103510447
# Date created: 17 Aug, 2023

# The valid program to be tested
correct_program = '(A - B) * 2'

# The buggy alternatives to the valid program
invalid_programs = [
  '(A + B) * 2',
  '(A / B) * 2',
  '(A * B) * 2',
  '(A - B) - 2',
  '(A - B) + 2',
  '(A - B) / 2',
  '(A + B) + 2',
  '(A * B) + 2',
  '(A / B) + 2',
  '(A + B) - 2',
  '(A * B) - 2',
  '(A / B) - 2',
  '(A + B) / 2',
  '(A * B) / 2',
  '(A / B) / 2'
]

# evaluate the program with given values of A and B
def evaluate(program, a, b):
  # subsitute A and B with values of a and b
  program = program.replace('A', f"{a}").replace('B', f"{b}")
  try:
    ans = float(eval(program))
  except ZeroDivisionError:
    ans = None
  # can be uncommented to see the working of each test case
  # print(f"{program} = {ans}")
  return ans

# validate test case with values of A and B with expected result by comparing it with output of all buggy programs
def valid_test_case(a, b, res):
  vals = []
  for i in invalid_programs:
    vals.append(evaluate(i, a, b))
  return res not in vals

# get all possible values of A for B given value of a, like (1, B)
# and prints all possible values of B that cannot achieve the testing objective
def get_all_possible_values_for_a(a):
  valid_test_cases = set()
  num_unachieved = 0
  print("Possible values of B that cannot achieve the testing objective:")
  for b in range(-100, 100):
      result = evaluate(correct_program, a, b)
      # check if the test case achieves the testing objective and not already present in the set
      if valid_test_case(a, b, result) and (a, b) not in valid_test_cases:
        valid_test_cases.add((a, b))
      else:
        num_unachieved += 1
        print(f"A= {a}, B= {b}, C= {result}")
  if num_unachieved == 0:
    print("None")
  return valid_test_cases

# get all possible values of A for a given value of B, like (A, 1)
# and prints all possible values of A that cannot achieve the testing objective
def get_all_possible_values_for_b(b):
  valid_test_cases = set()
  num_unachieved = 0
  print("Possible values of A that cannot achieve the testing objective:")
  for a in range(-100, 100):
      result = evaluate(correct_program, a, b)
      # check if the test case achieves the testing objective and not already present in the set
      if valid_test_case(a, b, result) and (a, b) not in valid_test_cases:
        valid_test_cases.add((a, b))
      else:
        num_unachieved += 1
        print(f"A= {a}, B= {b}, C= {result}")
  if num_unachieved == 0:
    print("None")
  return valid_test_cases

def print_test_cases(test_cases):
  # tabulate the test cases
  print("A\tB\tC")
  for i in test_cases:
    print(f"{i[0]}\t{i[1]}\t{evaluate(correct_program, i[0], i[1])}")

def main():
    print("Welcome to the test program")
    # menu driven program provding options to test all valid test cases for a given value of A, B or a single test case with both A and B
    while True:
      print("Choose from the following test options: ")
      print("1. Test for \"given value of A\" and get values of B that cannot achieve the testing objective")
      print("2. Test for \"given value of B\" and get values of A that cannot achieve the testing objective")
      print("3. Test with both A and B")
      print("4. Exit")
      choice = int(input("Enter your choice: "))
      if choice == 1:
        a = eval(input("Enter a value for A: "))
        print(f"Number of possible passing values of B that can achieve testing objective found in range [-100, 100]: {len(get_all_possible_values_for_a(a))}")
      elif choice == 2:
        b = eval(input("Enter a value for B: "))
        print(f"Number of possible passing values of A that can achieve testing objective found in range [-100, 100]: {len(get_all_possible_values_for_b(b))}")
      elif choice == 3:
        a = eval(input("Enter a value for A: "))
        b = eval(input("Enter a value for B: "))
        result = evaluate(correct_program, a, b)
        print(f"Correct result: {result}")
        validity = valid_test_case(a, b, result)
        print(f"Successful! ({a}, {b}) can achieve the testing objective" if validity else f"({a}, {b}) CANNOT achieve the testing objective")
      elif choice == 4:
        break
      else:
        print("Invalid choice")
      print("-"*30)
    

if __name__ == '__main__':
  main()
