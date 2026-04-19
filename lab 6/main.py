#1
import pandas as pd
df = pd.read_excel(r"C:\Users\Anuar\Desktop\pycharm\lab 6\catalog_products.xlsx")
print("Размер:", df.shape)
print("\nТипы данных:")
print(df.dtypes)
print("\nПропущенные значения по колонкам:")
print(df.isnull().sum())
print("\nПервые 5 строк:")
print(df.head())

#2
df = pd.read_excel(r"C:\Users\Anuar\Desktop\pycharm\lab 6\catalog_products.xlsx")

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")
num_cols = df.select_dtypes(include=["number"]).columns

df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
print(df[num_cols].isnull().sum())
print(df.head())

#3
import numpy as np
df = pd.read_excel(r"C:\Users\Anuar\Desktop\pycharm\lab 6\catalog_products.xlsx")

df["total_value"]=df["col_2"] * df["col_3"]
df["double_stock"]=df["col_4"] * 2
df["log_price"]=np.log(df["col_2"])

print(df[["total_value","double_stock","log_price"]].head())

#4
electronics_expensive = df[
    (df["col_2"] > 500) &
    (df["col_7"] == "Electronics")
]

print(electronics_expensive.head())

#5
grouped = df.groupby("col_7").agg(
    mean_price=("col_2", "mean"),
    max_price=("col_2", "max"),
    total_quantity=("col_3", "sum")
).reset_index()

print(grouped)

#6
cols = [f"col_{i}" for i in range(2, 12)]
df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")
result = pd.DataFrame({
    "column": cols,
    "mean": [df[col].mean() for col in cols],
    "median": [df[col].median() for col in cols],
    "std": [df[col].std() for col in cols]
})

print(result)

#7
df["col_2"] = pd.to_numeric(df["col_2"], errors="coerce")

mean_price = df["col_2"].mean()
std_price = df["col_2"].std()

threshold = mean_price + 3 * std_price

anomalies = df[df["col_2"] > threshold]
print(anomalies.head())

#8
cols = [f"col_{i}" for i in range(2, 12)]

corr_matrix = df[cols].corr()
print(corr_matrix)

#9
import matplotlib.pyplot as plt
df["col_2"] = pd.to_numeric(df["col_2"], errors="coerce")
plt.figure(figsize=(10, 6))
plt.hist(df["col_2"], bins=50, edgecolor="black")

plt.title("Распределение цен товаров")
plt.xlabel("Цена товаров")
plt.ylabel("Количество товаров")
plt.grid(True)
plt.show()
