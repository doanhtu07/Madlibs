from collections import deque
import re

print()
template = input("Input template (or -r to randomize): ")

if template == "-r":
    file = open("pizza", "r")
    template = file.read()

# Collect promptNames
specialStrings: list[str] = re.findall(r"_[a-zA-Z]+_", template)
promptNames = [x[1:len(x)-1] for x in specialStrings]

# Collect inputs
print()
print("--- Prompts ---")
inputs = deque([])
for name in promptNames:
    x = input(f"{name}: ")
    inputs.append(x)
print()

# Replace _sth_ with input
template = re.sub(r"_[a-zA-Z]+_", lambda x: inputs.popleft(), template)

# Print out final result
print("--- Story ---")
print(template)
print()