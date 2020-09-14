from colorama import Fore #, Back, Style

def compute(num1, parse, num2):
  if(parse == '+'):
    return num1 + num2;
  elif(parse == '-'):
    return num1 - num2;
  elif(parse == '*'):
    return num1 * num2;
  elif(parse == '/'):
    return num1 / num2;
  elif(parse == '^'):
    return num1 ** num2;
  elif(parse == '%'):
    return num1 % num2;

  raise NameError(Fore.RED + 'Invalid Operator. Try again.' + Fore.WHITE);

def throw(extra):
  print(Fore.RED + "Invalid Syntax. Try again.");
  if(extra != None): print("\n" + extra);

  print(Fore.WHITE);

possible = ['exit', 'EXIT', 'q', 'quit', 'QUIT'];
def check_quit(usr_input):
  return usr_input in possible;