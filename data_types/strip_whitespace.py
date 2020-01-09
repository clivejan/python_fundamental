favourite_language = ' Python '
print(f"My favourite programming language is {favourite_language}.")

# Remove whitespace at rigth side of string temporarily
print(f"My favourite programming language is {favourite_language.rstrip()}.")

# Remove whitespace at left side of string temporarily
print(f"My favourite programming language is {favourite_language.lstrip()}.")

# Remove whitespace at both sides of string temporarily
print(f"My favourite programming language is {favourite_language.strip()}.")

# Remove whitespace at both sides of string permanently
favourite_language = favourite_language.strip()
print(f"My favourite programming language is {favourite_language}.")
