#1
import pandas as pd
df = pd.read_excel(r"C:\Users\Anuar\Desktop\pycharm\lab 7\catalog_products.xlsx")
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

#2
import numpy as np
for col in df.select_dtypes(include=["int64", "float64"]).columns:
    df[col] = df[col].astype(float)
df = df.fillna(df.mean(numeric_only=True))
df = df.dropna(subset=["col_1", "col_7"])
print("после очистки:", df.shape)

#3
df["total_value"] = df["col_2"]*df["col_3"]
df["log_price"]=np.log(df["col_2"])
df["double_stock"]=df["col_3"]*2
print("признаки:", df[["total_value","log_price","double_stock"]].head())

#4
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(df["col_2"], bins=30)
plt.show()
sns.scatterplot(x=df["col_3"], y=df["col_2"])
plt.show()
sns.boxplot(x=df["col_7"], y=df["col_2"])
plt.xticks(rotation=45)
plt.show()

#5
mean = df["col_2"].mean()
std = df["col_2"].std()
anomalies = df[(df["col_2"] > mean + 3*std) | (df["col_2"] < mean - 3*std)]
df = df.drop(anomalies.index)
print("аномалий:", anomalies.shape)

#6
df = pd.get_dummies(df, drop_first=True)
print("One-Hot Encoding:",df.shape)

#18
def price_class(p):
    if p<100:
        return 0
    elif p<=500:
        return 1
    return 2
df["price_class"] = df["col_2"].apply(price_class)

#7
from sklearn.model_selection import train_test_split
X = df.drop(columns=["col_2", "price_class"])
y=df["col_2"]
print("OBJECT COLUMNS:", X.select_dtypes(include="object").columns)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#8
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
model_basic = LinearRegression()
model_basic.fit(X_train, y_train)
y_pred = model_basic.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

#9

y_pred = model_basic.predict(X_test)

#10
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color = "red")
plt.xlabel("True")
plt.ylabel("Predicted")
plt.show()

#11
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
num_cols = ["col_3", "total_value", "double_stock", "log_price"]
df[num_cols] = scaler.fit_transform(df[num_cols])

#12
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor()
tree.fit(X_train, y_train)
importance = pd.Series(tree.feature_importances_, index=X.columns)
importance.sort_values().plot(kind = "barh")
plt.show()

#13
from sklearn.preprocessing import PolynomialFeatures
X = df.drop(columns=["col_2", "price_class"])
poly = PolynomialFeatures(degree = 2, include_bias=False)
X_poly = poly.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y, test_size=0.2, random_state=42
)
model_poly = LinearRegression()
model_poly.fit(X_train, y_train)
y_pred = model_poly.predict(X_test)

#14
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

#15
from sklearn.metrics import mean_absolute_error
for col in [c for c in df.columns if "col_7_" in c]:
    subset = df[df[col] == 1]
    if len(subset) > 10:
        X_sub = subset.drop(columns=["col_2", "price_class"])
        y_sub = subset["col_2"]
        X_train_sub, X_test_sub, y_train_sub, y_test_sub = train_test_split(
            X_sub, y_sub, test_size=0.2, random_state=42
        )
        model_basic.fit(X_train_sub, y_train_sub)
        pred = model_basic.predict(X_test_sub)
        print(col, mean_absolute_error(y_test_sub, pred))
#16
print("sizes:", len(y_test), len(y_pred))
if len(y_test) != len(y_pred):
    y_pred = model_poly.predict(X_test)
errors = abs(y_test - y_pred)
worst = errors.sort_values(ascending=False).head(10)
print(df.loc[worst.index])

#17
from sklearn.model_selection import cross_val_score
X_full = df.drop(columns=["col_2", "price_class"])
X_full_poly = poly.transform(X_full)
y_full = df["col_2"]
scores = cross_val_score(
    model_basic,
    X_full,
    y_full,
    cv=5,
    scoring="neg_mean_squared_error"
)
print("MSE:", -scores.mean())


#19
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
clf = DecisionTreeClassifier()
clf.fit(X_train, df.loc[y_train.index, "price_class"])
pred = clf.predict(X_test)
y_test_class = df.loc[y_test.index, "price_class"]
cm = confusion_matrix(y_test_class, pred)
sns.heatmap(cm, annot=True)
plt.show()

#20
X_full = df.drop(columns=["col_2", "price_class"])
X_full_poly = poly.transform(X_full)
df["predicted_price"] = model_poly.predict(X_full_poly)

df.to_excel(r"C:\Users\Anuar\Desktop\pycharm\lab 7\catalog_ml_predictions.xlsx", index=False)