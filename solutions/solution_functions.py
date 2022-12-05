"""
Test File: tests/test_functions.py
Reference: https://developers.google.com/edu/python/introduction#user-defined-functions
"""
def hello():
    """
    Tests:
      - test_hello
    """
    ### solution:start
    return "Hello"
    ### solution:end



def hello_there(subject="stranger",prefix=""):
    """
    Tests: 
      - test_hello_there_positional_argument
      - test_hello_there_default_argument
      - test_hello_there_prefix
      - test_hello_there_multiple_positional_arguments
      - test_hello_there_key_word_arguments
    """
    ### solution:start
    if prefix:
        prefix += " "
        
    # TODO: Add reference link
    return f"Hello, {prefix}{subject}"
    ### solution:end

def knock_knock(short, long):
    """
    Tests:
      - test_knock_knock
    """
    ### solution:start
    import textwrap
    return textwrap.dedent(f"""
    knock knock.
    Who's there?
    {short}.
    {short} who?
    {short} {long}""").strip()
    ### solution:end
    
    
    