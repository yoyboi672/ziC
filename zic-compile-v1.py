from time import sleep

quit_when_error = True
filename = input("Please enter a file name: ")

try:
    with open(f'{filename}.txt', 'r') as file:
        code = file.read()
except FileNotFoundError:
    print(f"The input file '{filename}.txt' was not found.")
    quit()

if code == "":
    print("The input file is empty.")
    quit()

for line in code.split('\n'):
    if line.startswith('//') or line.strip() == "":
        continue
    
    if line.startswith("say "):
        print(line.removeprefix("say "))
    elif line.startswith("delay "):
        sleep(int(line.removeprefix("delay ").strip()))
    elif line.strip() == "quit":
        quit()
    else:
        print("Invalid command:", line)
        if quit_when_error:
            quit()
        else:
            continue