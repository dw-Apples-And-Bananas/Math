from difflib import get_close_matches
import os
from Basic import *


def run(function, debug=True):
    if not debug:
        try:
            output = eval(function)
        except Exception as e:
            output = f"Error '{e}' has occured.\nRun the 'Help' function for instructions."
        print(output, "\n")
    else:
        print(eval(function), "\n")


funcs = {func.replace("_","-"): func for func in dir() if func[0].isupper()}
matches = []

while True:
    func = input("")
    os.system("clear")

    if func in funcs:
        args = input(f"{func}: ")
        run(f"{funcs[func]}('{args}')")
    elif func == "" and matches != []:
        func = matches[-1]
        args = input(f"{func}: ")
        run(f"{funcs[func]}('{args}')")
        matches = []
    else:
        matches = get_close_matches(func, list(funcs), cutoff=0.2)
        matches.reverse()
        if matches != []:
            if len(matches) > 1: print("\n".join(matches[:-1]))
            print(f"Return for autocomplete '{matches[-1]}'")

