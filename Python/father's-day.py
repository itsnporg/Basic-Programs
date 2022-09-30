import time
import random
import colorama
from colorama import init
init()
colors = list(vars(colorama.Fore).values())
while True:
    time.sleep(0.5)
    print(
        " " * random.randint(0, 150)+f"{colorama.Style.BRIGHT}{random.choice(colors)}Happy{random.choice(colors)} Father's{random.choice(colors)} Day", end="",)
    print(" " * random.randint(0, 150) + f"{random.choice(colors)} *", end="")
    print(" " * random.randint(0, 150) + f"{random.choice(colors)} *")