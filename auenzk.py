import random
import string
import sys


usage = """Usage:\n\t$ python3 auenzk.py {name_length} {names_number}\nExample:\n\t$ python3 auenzk.py 5 3"""

def main(args: list) -> None:
    letters = string.ascii_lowercase
    names = []
    name_length = int(args[0])
    names_number = int(args[1])
    for _ in range(names_number):
        names.append("".join(random.choices(letters, k=name_length)))
    for name in names:
        print(name)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except:
        print(usage)

