# run test_hello in test_functions.py

# Modify the hello function to take in no arguments and return the string "Hello"
def hello():
    return "Hello"

"""
Write a function hello_there that takes in a subject and returns "Hello, Mario" if "Mario" was the given argument

Reference: https://developers.google.com/edu/python/introduction#user-defined-functions

"""

def hello_there(subject="stranger",prefix=""):
    if prefix:
        prefix += " "
        
    return f"Hello, {prefix}{subject}"

# Modify function hello_there that now will take in an optional subject 
# and returns "Hello, stranger" if no argument supplied. 
# Otherwise return "Hello, " + the supplied argument.

def knock_knock(short, long):
    import textwrap
    return textwrap.dedent(f"""
    knock knock.
    Who's there?
    {short}.
    {short} who?
    {short} {long}""").strip()
    
    
    