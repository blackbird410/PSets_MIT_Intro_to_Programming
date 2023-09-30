from ps5 import *
from datetime import datetime

def main():
    l = read_trigger_config("triggers.txt")
    print(l)


if __name__ == "__main__":
    main()