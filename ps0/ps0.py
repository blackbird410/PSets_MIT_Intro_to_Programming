from math import log2

def main():
    try:
        x = int(input("Enter a number x: "))
        y = int(input("Enter a number y: "))
        print(f"x**y = {x**y}")
        print(f"log(x) = {log2(x)}")
    except:
        print("Entered number format is wrong. Please check your input")


if __name__ == "__main__":
    main()