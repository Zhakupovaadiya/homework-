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
import matplotlib.pyplot as plt
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