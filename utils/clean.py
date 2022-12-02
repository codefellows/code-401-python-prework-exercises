import os
import re

def clean_solution_file(filename, source="./solutions", destination="./exercises"):
    """
    Generates exercise files from source solution files
    - Replaces solution code with "pass"
    - replaces function parameter list with ()
    """
    with open(source + "/" + filename) as file:
        text = file.read()

    pattern = re.compile(r"### solution:start.*?### solution:end", re.DOTALL)

    cleaned = re.sub(pattern, "pass", text)

    trimmed = remove_params(cleaned)

    with open(f"{destination}/{filename}","w") as file:
        file.write(trimmed)
    



def remove_params(test_str):
    regex = r"(^def .*)\(.*\):"

    # test_str = r"def hello_there(subject=\"stranger\",prefix=\"\"):"

    subst = r"\1():"

    # You can manually specify the number of replacements by changing the 4th argument
    result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

    return result



files = os.listdir("./solutions")

scripts = [file for file in files if file.endswith(".py")]

for script in scripts:
    clean_solution_file(script)