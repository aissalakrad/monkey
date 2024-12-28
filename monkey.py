import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;: "

print("Your input (use Ctrl+D or Ctrl+Z to submit):")
try:
    import sys
    input = sys.stdin.read().strip()
except EOFError:
    input = ""
output = ""

while True:
    character = random.choice(characters)
    
    print(character, end="")
    output += character

    if input in output:
        print("\nA match was found!")
        break