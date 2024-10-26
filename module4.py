def initiate_input():
    N = int(input("Enter input for N: "))
    input_number = []
    for _ in range(N):
        input_number.append(int(input("Enter input data:")))
    X = int(input("Enter input for X: "))
    return input_number.index(X) + 1 if X in input_number else -1


if __name__ == "__main__":
    print(initiate_input())
