import numpy as np


class KNNRegression:
    def __init__(self, k_neighbours):
        self.k_neighbours = k_neighbours
        self.points = np.array([])

    def add_points(self, new_points):
        if self.points.size == 0:
            self.points = new_points
        else:
            self.points = np.vstack((self.points, new_points))

    def predict(self, x):
        if len(self.points) < self.k_neighbours:
            return "Error: k cannot be greater than the number of available points (N)."

        distances = np.abs(self.points[:, 0] - x)
        nearest_indices = np.argsort(distances)[: self.k_neighbours]
        nearest_points = self.points[nearest_indices]
        return np.mean(nearest_points[:, 1])


def main():
    N = int(input("Enter input for N: "))
    while N <= 0:
        N = int(input("Please enter a positive integer for N: "))

    k = int(input("Enter input for k: "))
    while k <= 0:
        k = int(input("Please enter a positive integer for k: "))

    knn = KNNRegression(k)
    points = []
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        points.append([x, y])

    knn.add_points(np.array(points))

    X = float(input("Enter the X value for prediction: "))
    result = knn.predict(X)
    print(f"Predicted Y value: {result}")


if __name__ == "__main__":
    main()
