import os
import re

def generate_exercise(filename, source="./solutions", destination="./exercises"):
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

    dest_filename = filename.split("_")[1]

    with open(f"{destination}/{dest_filename}","w") as file:
        file.write(trimmed)
    



def remove_params(test_str):
    regex = r"(^def .*)\(.*\):"

    subst = r"\1():"

    result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

    return result



if __name__ == "__main__":
    files = os.listdir("./solutions")

    scripts = [file for file in files if file.endswith(".py")]

    for script in scripts:
        generate_exercise(script)