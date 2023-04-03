import pandas as pd
from scipy import stats

# df = pd.read_csv("iris.csv")

# print(df)
# type(df)
# print(df.sepal_length_cm)
# print(df.iloc[0])
# print(df.iloc[0:3])
# print(df.iloc[0, 0])
# print(df.iloc[0:3, 0])
# long_flowers = df[df.petal_length_cm > 5.9]
# print(long_flowers)
# versicolor = df[df.species == "Iris_versicolor"]
# print(versicolor)

import matplotlib.pyplot as plt
# plt.scatter(df.petal_length_cm, df.sepal_length_cm)
# plt.xlabel("Petal length (cm)")
# plt.ylabel("Sepal length (cm)")
# plt.savefig("petal_v_sepal_length.png")
# quit()

x = df.petal_length_cm
y = df.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress.png")
quit()


iris = pd.read_csv('iris',
                       header=None,
                       names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
print (iris)