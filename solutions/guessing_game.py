"""  Guessing Game
  write a function that takes a random integer from the 
  user (the player) and compare it to a randomly generated number inside
  the function.
  """
import random
def guessing_game(lower_bound: int, upper_bound: int) -> int:
    """Compares the user's input integer to a randomly
        generated integer from within the function.
        
    Parameters:
        number: int, a random number generated within the function.        
        
    Returns -> str: You Won! (if the user's guess matched the random int)
            ->  str: Try Again (if the user's guess did not match the random int) 
        

"""
lower_bound =input("Enter the lower bound: ")
lower_bound =int(lower_bound)
upper_bound =input("Enter the upper bound: ")
upper_bound = int(upper_bound)
random_number =random.randint(lower_bound, upper_bound)
guess =input(f"Guess a number between {lower_bound} and {upper_bound}: ")
guess =int(guess)

if random_number ==guess:
    print("You Won!")
else:
    print("Try Again")
