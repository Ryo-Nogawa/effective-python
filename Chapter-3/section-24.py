from time import sleep
from datetime import datetime


def log(message, when=datetime.now()):
    print(f"{when}: {message}")


log("Hi there!")
sleep(0.1)
log("Hi again!")


print("#" * 20)


def log2(message, when=None):
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")


log2("Hi there!")
sleep(0.1)
log2("Hi again!")
