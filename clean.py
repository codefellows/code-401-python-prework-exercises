import os
import re

def clean_solution_file(filename, source="./solutions", destination="./exercises"):
    with open(source + "/" + filename) as file:
        text = file.read()

    pattern = re.compile(r"### solution:start.*?### solution:end", re.DOTALL)

    cleaned = re.sub(pattern, "pass", text)

    with open(f"{destination}/{filename}","w") as file:
        file.write(cleaned)

files = os.listdir("./solutions")

scripts = [file for file in files if file.endswith(".py")]

for script in scripts:
    clean_solution_file(script)
