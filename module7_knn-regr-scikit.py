import numpy as np
from sklearn.neighbors import KNeighborsRegressor

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

        model = KNeighborsRegressor(n_neighbors=self.k_neighbours)
        model.fit(self.points[:, 0].reshape(-1, 1), self.points[:, 1])
        prediction = model.predict(np.array([[x]]))
        return prediction[0]

def main():
    N = int(input("Enter the value of N (positive integer): "))
    while N <= 0:
        N = int(input("Please enter a positive integer for N: "))

    k = int(input("Enter the value of k (positive integer): "))
    while k <= 0:
        k = int(input("Please enter a positive integer for k: "))

    knn = KNNRegression(k)
    points = np.zeros((N, 2))
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        points[i] = [x, y]

    knn.add_points(points)
    y_values = points[:, 1]
    variance = np.var(y_values)
    print(f"Variance of y values: {variance}")
    X = float(input("Enter the X value for prediction: "))

    result = knn.predict(X)
    print(f"Predicted Y value: {result}")

if __name__ == "__main__":
    main()
