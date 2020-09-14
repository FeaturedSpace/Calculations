# Calculations (#001)
# Noah Coetsee
# 09/14/2020


from colorama import Fore #, Back, Style

import helper;
  

print(Fore.LIGHTBLUE_EX + "Welcome to Noah's Calculator!")
print("Write instructions using the 'Noah' syntax.")
print("That is, separate your tokens with spaces so I don't have to do a bunch of boring work.")
print("You can access the last solution calculated via 'ans'")
print("\nEx: '1 + 3', '1 * 4', '-43 / 3'")
print("\nSupported Operators: '+', '-', '*', '/', '^', '%'")


exit = False
ans = None
while not exit:
  # Response Start

  usr_input = input(Fore.WHITE + "Please input a calculation (\"exit\" to quit) ")


  # Response End

  # Quick program-quit check.
  if(usr_input == "exit" or usr_input == "EXIT"):
    exit = True
    break;

  # Parsing Start

  tokens = usr_input.split(" ")
  if len(tokens) != 3:
    helper.throw("Please pass two numbers and an operator (num, operator, num)")
    continue;

  num1 = tokens[0];
  operator = tokens[1]
  num2 = tokens[2];

  try:
    if num1 == 'ans': 
      if(ans != None):
        num1 = ans;
      else:
        print(Fore.RED + 'Error: No previous solution was found.' + Fore.WHITE)
        continue;
    else:
      num1 = float(tokens[0])

    if num2 == 'ans':
      if(ans != None):
        num2 = ans;
      else:
        print(Fore.RED + 'Error: No previous solution was found.' + Fore.WHITE)
        continue;
    else: 
      num2 = float(tokens[2])
  except:
    print(Fore.RED + "Invalid Syntax. Try again." + Fore.WHITE)
    continue;
  
  # print("First number is: ", num1)
  # print("Second number is: ", num2)

  solution = helper.compute(num1, operator, num2)
  ans = solution

  print(Fore.GREEN + "Solution: ", solution, "\n" + Fore.WHITE)

  # Parsing End

  if exit: break;

print(Fore.GREEN + "\nProgram complete.")

