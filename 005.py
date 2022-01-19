"""Question: Define a class which has at least two methods: getString: to get a string  
from console input printString: to print the string in upper case. Also please include simple test function to test the class methods."""

class StringClass:
    def __init__(self, string: str):
        self.string = string

    def getString(self) -> None:
        self.string = input("Write your String here: ")

    def printString(self) -> None:
        print(f"This is your String: {self.string}")


def main():
    x = StringClass("")
    x.getString()
    x.printString()

if __name__ == "__main__":
    main()
