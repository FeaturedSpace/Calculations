# Calculations (#001)
# Noah Coetsee
# 09/14/2020


from colorama import Fore #, Back, Style

import helper;
import lexer;
  

print(Fore.LIGHTBLUE_EX + "Welcome to Noah's Calculator!");
print("Write instructions using the 'Noah' syntax.");
print("That is, separate your tokens with spaces so I don't have to do a bunch of boring work.");
print("You can access the last solution calculated via 'ans', and you can view all previous operations via the 'history' command.");
print("\nEx: '1 + 3', '1 * 4', '-43 / 3'");
print("\nSupported Operators: '+', '-', '*', '/', '^', '%'");


exit = False;
ans = None;

history = list();

while not exit:
  # Response Start

  usr_input = input(Fore.WHITE + "Please input a calculation (\"exit\" to quit) ");

  # Response End

  # Quick program-quit check.
  if(usr_input == "exit" or usr_input == "EXIT"):
    exit = True;
    break;

  # Quick history-command check
  if(usr_input == 'history'):
    if(len(history) == 0 or history == None):
      helper.throw("History had not yet been created!");

    print(Fore.LIGHTMAGENTA_EX + "History: ");
    for tt in history:
      print(tt, "\n");
    continue;

  # Parsing Start

  # Replace 'ans' with the last answer
  if('ans' in usr_input):
    try:
      usr_input = usr_input.replace('ans', str(ans));
    except:
      helper.throw("'ans' token was found but no previous solution exists!");
      continue;

  tokens = lexer.lex(usr_input); #usr_input.split(" ");
  print(tokens);

  if len(tokens) != 3:
    helper.throw("Please pass two numbers and an operator (num, operator, num)");
    continue;

  num1 = tokens[0];
  operator = tokens[1];
  num2 = tokens[2];

  try:
    num1 = float(num1);
    num2 = float(num2);
  except:
    print(Fore.RED + "Invalid Syntax. Try again.");
    continue;

  # try:
  #   if num1 == 'ans': 
  #     if(ans != None):
  #       num1 = ans;
  #     else:
  #       print(Fore.RED + 'Error: No previous solution was found.' + Fore.WHITE);
  #       continue;
  #   else:
  #     num1 = float(tokens[0]);

  #   if num2 == 'ans':
  #     if(ans != None):
  #       num2 = ans;
  #     else:
  #       print(Fore.RED + 'Error: No previous solution was found.' + Fore.WHITE);
  #       continue;
  #   else: 
  #     num2 = float(tokens[2]);
  # except:
  #   print(Fore.RED + "Invalid Syntax. Try again." 
  #   + Fore.WHITE);
  #   continue;
  
  # print("First number is: ", num1)
  # print("Second number is: ", num2)

  solution = helper.compute(num1, operator, num2);
  ans = solution;

  history.append((num1, operator, num2, ans))

  print(Fore.GREEN + "Solution: ", solution, "\n" 
  + Fore.WHITE);

  # Parsing End

  if exit: break;

print(Fore.GREEN + "\nProgram complete.");