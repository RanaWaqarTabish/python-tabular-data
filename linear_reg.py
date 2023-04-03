import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def load_iris_data():
    """
    Returns a pandas DataFrame of the iris dataset.
    """
    iris = pd.read_csv('iris.csv',
                       header=None,
                       names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
    return iris

def plot_linear_regression(iris, species):
    """
    Plots a linear regression of petal length versus petal width for a given iris species.
    """
    iris_species = iris[iris['species'] == species]
    x = iris_species.iloc[:, 2] # petal length
    y = iris_species.iloc[:, 3] # petal width
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Petal width (cm)")
    plt.legend()
    plt.savefig("petal_length_width_regress.png")


if __name__ == '__main__':
    iris = load_iris_data()
    species_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    for species_name in species_names:
        plot_linear_regression(iris, species_name)
