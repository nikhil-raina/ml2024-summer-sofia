
class NumberFinder:
    def __init__(self):
        self.N = 0
        self.X = None
        self.input_numbers = []

    def initiate_input(self):
        self.N = int(input("Enter input for N: "))
        while self.N < 0:
            self.N = int(input("Please enter a positive number for N: "))
        for _ in range(self.N):
            self.input_numbers.append(int(input("Enter input data: ")))
        self.X = int(input("Enter input for X: "))

    def find_X(self):
        return self.input_numbers.index(self.X) + 1 if self.X in self.input_numbers else -1


if __name__ == "__main__":
    number_finder = NumberFinder()
    number_finder.initiate_input()
    print(number_finder.find_X())
