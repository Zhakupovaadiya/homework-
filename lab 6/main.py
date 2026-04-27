#1
import pandas as pd
df=pd.read_excel(r"C:\Users\Anuar\Desktop\pycharm\lab 6\catalog_products.xlsx")
print("Размер:",df.shape)
print("Типы данных:",df.dtypes)
print("Пропуски: ",df.isnull().sum())
print("Первык 5 строк: ",df.head(5))

#2
num_cols = [col for col in df.columns if col != "col_7"]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

print(df[num_cols].isnull().sum())
print(df.head())

#3
import numpy as np
df.columns = df.columns.str.strip()
df["col_7"] = df["col_7"].astype(str)
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
df['col_3'] = pd.to_numeric(df['col_3'], errors='coerce')
df['col_4'] = pd.to_numeric(df['col_4'], errors='coerce')
df["total_value"]=df["col_2"] * df["col_3"]
df["double_stock"]=df["col_4"] * 2
df["log_price"] = np.log(df["col_2"].replace(0, np.nan))

print(df[["total_value","double_stock","log_price"]].head())

#4
electronic_expensive=df[(df["col_2"]>500) & (df["col_7"] == "Electronics")]
print(electronic_expensive.head())

#5
grouped = df.groupby("col_7").agg(
    mean_price=("col_2", "mean"),
    mean_quantity=("col_2", "max"),
    total_quantity=("col_3", "sum")
    ).reset_index()
print(grouped.head())

#6
cols = [f"col_{i}" for i in range(2, 12) if f"col_{i}" in df.columns and i != 7]
result = pd.DataFrame({
    "column": cols,
    "mean": [df[col].mean() for col in cols],
    "median": [df[col].median() for col in cols],
    "std": [df[col].std() for col in cols]
})
print(result)

#7
mean_price = df["col_2"].mean()
std_price = df["col_2"].std()
threshold = mean_price + 3 * std_price
anomalies = df[df["col_2"] > threshold]
print(anomalies.head())

#8
corr_matrix = df[cols].corr()
print(corr_matrix)

#9
import matplotlib.pyplot as plt
plt.figure()
plt.hist(df["col_2"].dropna(), bins=50)
plt.title("Распределение цены")
plt.show()




#10
import seaborn as sns
sns.set()
plt.figure()
sns.regplot(x=df['col_2'], y=df['col_3'])
plt.show()

#11
plt.figure()
sns.boxplot(x="col_7", y="col_2", data=df)
plt.xticks(rotation=45)
plt.show()

#12
sns.pairplot(df[['col_2','col_3','col_4','col_5','col_6','col_7']], hue='col_7')
plt.show()

#13
plt.figure()
sns.heatmap(corr_matrix, annot=True)
plt.title('Корреляция')
plt.show()

#14
df.to_excel('catalog_analysis.xlsx', index=False)
if 'log_price' not in df.columns:
    import numpy as np
    df['log_price'] = np.log(pd.to_numeric(df['col_2'], errors='coerce'))

#15
category_summary = df.groupby('col_7').agg(
    count=('col_1', 'count'),
    mean_price=('col_2', 'mean'),
    total_quantity=('col_3', 'sum'),
    mean_log_price=('log_price', 'mean')
).reset_index()
print(category_summary.head())

#16
most_expensive = df.loc[df.groupby('col_7')['col_2'].idxmax()]
print(most_expensive[['col_1', 'col_2', 'col_7']])

#17
df['total_value'] = df['col_2'] * df['col_3']
top10 = df.sort_values('total_value', ascending=False).head(10)
print(top10[['col_1','col_2','col_3','total_value']])

#18
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50','50-200','200-500','500-1000','>1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
price_counts = df['price_range'].value_counts()
sns.barplot(x=price_counts.index, y=price_counts.values)
plt.title('Распределение по диапазонам цен')
plt.show()

#19
cat_value = df.groupby('col_7')['total_value'].sum()
print(cat_value.idxmax())
sns.barplot(x=cat_value.index, y=cat_value.values)
plt.xticks(rotation=45)
plt.show()

#20
cat_stats = df.groupby('col_7').agg(
    mean_price=('col_2','mean'),
    mean_quantity=('col_3','mean')
).reset_index()
sns.scatterplot(
    data=cat_stats,
    x='mean_price',
    y='mean_quantity',
    hue='col_7'
)
plt.show()

#21
std_price = df.groupby('col_7')['col_2'].std()
sns.barplot(x=std_price.values, y=std_price.index)
plt.title('Разброс цен по категориям')
plt.show()

#22
zero_stock = df[df["col_3"] == 0]
print(zero_stock[["col_1", "col_7", "col_2"]].head(10))

#23
cat_counts = df["col_7"].value_counts().head(5)
print(cat_counts)

sns.barplot(x=cat_counts.index, y=cat_counts.values)
plt.xticks(rotation=45)
plt.title("Топ-5 категорий по количеству товаров")
plt.show()

#24
top_stock = df.sort_values("col_3", ascending=False).head(10)
print(top_stock[["col_1", "col_3"]])

sns.barplot(x=top_stock["col_3"], y=top_stock["col_1"])
plt.title("Топ-10 товаров по запасу")
plt.show()

#25
bins = [0, 50, 200, 500, 1000, float("inf")]
labels = ["0-50","50-200","200-500","500-1000",">1000"]

df["price_range"] = pd.cut(df["col_2"], bins=bins, labels=labels)
pivot = pd.pivot_table(
    df,
    values="col_1",
    index="col_7",
    columns="price_range",
    aggfunc="count"
)
print(pivot)

sns.heatmap(pivot, annot=True, fmt=".0f")
plt.title("Распределение товаров")
plt.show()

#36
cat_stats = df.groupby("col_7").agg(
    mean_price=("col_2", "mean"),
    mean_quantity=("col_3", "mean")
).reset_index()
sns.scatterplot(
    data=cat_stats,
    x="mean_price",
    y="mean_quantity",
    hue="col_7"
)
plt.title("Цена vs запас по категориям")
plt.show()

#37
std_price = df.groupby("col_7")["col_2"].std()
sns.barplot(x=std_price.values, y=std_price.index)
plt.title("Разброс цен по категориям")
plt.show()

#38
zero_stock = df[df["col_3"] == 0]
print(zero_stock[["col_1", "col_7", "col_2"]].head(10))

#39
cat_counts = df.groupby("col_7")["col_1"].count().sort_values(ascending=False).head(5)
print(cat_counts)

sns.barplot(x=cat_counts.values, y=cat_counts.index)
plt.title("Топ-5 категорий по количеству товаров")
plt.xlabel("Количество")
plt.ylabel("Категория")

plt.show()

#40
top_stock = df.sort_values("col_3", ascending=False).head(10)
print(top_stock[["col_1", "col_3"]])
sns.barplot(x=top_stock["col_3"], y=top_stock["col_1"])

plt.title("Топ-10 товаров по запасу")
plt.xlabel("Количество")
plt.ylabel("Товар")
plt.show()

#41
bins = [0, 50, 200, 500, 1000, float("inf")]
labels = ["0-50", "50-200", "200-500", "500-1000", ">1000"]

df["price_range"] = pd.cut(df["col_2"], bins=bins, labels=labels)
pivot = df.pivot_table(
    values="col_1",
    index="col_7",
    columns="price_range",
    aggfunc="count"
)
print(pivot)
sns.heatmap(pivot, annot=True, fmt=".0f")

plt.title("Распределение товаров по категориям и ценам")
plt.xlabel("Диапазон цены")
plt.ylabel("Категория")
plt.show()

#42
sns.regplot(x=df["col_2"], y=df["col_5"])

plt.xlabel("Цена")
plt.ylabel("Рейтинг")
plt.title("Цена vs рейтинг")
plt.show()

#43
sns.pairplot(
    df[["col_2","col_3","col_4","col_5","col_6","col_7"]],
    hue="col_7"
)
plt.show()

#44
mean_price = df["col_2"].mean()
std_price = df["col_2"].std()
mean_stock = df["col_3"].mean()
std_stock = df["col_3"].std()

extreme_items = df[
    (df["col_2"] > mean_price + 3 * std_price) |
    (df["col_3"] > mean_stock + 3 * std_stock)
]
print(extreme_items.head())

#45

top_value = df.sort_values("total_value", ascending=False).head(10)

summary = df.groupby("col_7").agg(
    mean_price=("col_2", "mean"),
    total_quantity=("col_3", "sum")
).reset_index()

with pd.ExcelWriter(r"C:\Users\Anuar\Desktop\pycharm\lab 6\catalog_final_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Data", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)
    top_stock.to_excel(writer, sheet_name="Top_Stock", index=False)
    top_value.to_excel(writer, sheet_name="Top_Value", index=False)