# This lexer (or tokenizer) is going to allow us to parse input without requiring spaces between operands and parameters.

debug = False;

"""
Parses a passed line into a tuple of (num1, operator, num2)
"""
def lex(passed):
  
  # Note that we will first always expect a number.
  # We will loop through until we find a character that is not a number.
  # We will then immediately assume it's an operator (which are only one char long), and then proceed to the next characters as the second number in the operation.

  # State Storage (stored in strings for ease)
  num1 = str();
  operator = str();
  num2 = str();

  phase = 0; # Will become equal to 1 if we are filling num2, rather than num1.

  if(debug): print("Lexing: " + passed)

  for c in passed:
    # Check for spaces
    if(c == ' '): continue;

    if(c.isdigit()):
      if(phase == 0):
        num1 = num1 + c;
      else: num2 = num2 + c;
    else:
      operator = c;
      phase = 1;
  
  return (num1, operator, num2);