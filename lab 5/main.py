#1
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name.strip().title()

        email = email.strip().lower()
        if "@" not in email:
            raise ValueError("Invalid email")
        self._email = email

#2
    @classmethod
    def from_string(cls, data: str):
        parts = [x.strip() for x in data.split(",")]
        return cls(int(parts[0]), parts[1], parts[2])

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def __del__(self):
        print(f"User {self._name} deleted")


#an1
u1 = User(1, "john doe", "John@Example.COM")
print(u1)

#an2
u2 = User.from_string("2, Alice Wonderland , alice@wonder.com")
print(u2)

#3
class Product:
    def __init__(self, id: int, name: str, price: float, category: str):
        self.id = id
        self.name = name
        self.price = float(price)
        self.category = category
    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return isinstance(other, Product) and self.id == other.id
    def __hash__(self):
        return hash(self.id)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }
p1=Product(1,"Laptop", 1200, "Electronics")
p2 = Product(2, "Mouse", 25.0, "Electronics")
p3 = Product(1, "Laptop Copy", 1200.0, "Electronics")
print(p1)
print(p1 == p3)

#4
class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self, product):
        self.products[product.id] = product
    def remove_product(self, product_id):
        self.products.pop(product_id, None)
    def get_product(self, product_id):
        return self.products.get(product_id)
    def get_all_products(self):
        return list(self.products.values())
    def unique_products(self):
        return set(self.products.values())
    def to_dict(self):
        return self.products

#5
    def filter_by_price(self, min_price):
        return [p for p in self.products.values() if (lambda x: x >= min_price)(p.price)]
pr1 = Product(1, "Apple", 100, "Fruit")
pr2 = Product(2, "Banana", 80, "Fruit")
pr3 = Product(3, "Orange", 90, "Fruit")
pr4 = Product(1, "Duplicate Apple", 100, "Fruit")


inv = Inventory()
inv.add_product(Product(1, "Laptop", 1200, "Electronics"))
inv.add_product(Product(2, "Mouse", 25, "Electronics"))
print(inv.get_all_products())
print(inv.get_product(1))
inv.remove_product(2)
print(inv.get_all_products())
print([p.name for p in inv.filter_by_price(100)])

#6
from datetime import datetime

class Logger:
    @staticmethod
    def log_action(user, action, product, filename):
        with open(filename, "a") as f:
            line = f"{datetime.now()};{user._id};{action};{product.id}\n"
            f.write(line)
    @staticmethod
    def read_logs(filename):
        logs = []
        with open(filename, "r") as f:
            for line in f:
                t, uid, act, pid = line.strip().split(";")
                logs.append({
                    "timestamp": t,
                    "user_id": int(uid),
                    "action": act,
                    "product_id": int(pid)
                })
        return logs
u = User(1, "John Doe", "john@mail.com")
p = Product(1, "Laptop", 1200, "Electronics")
Logger.log_action(u, "buy", p, "new_log.txt")
print(Logger.read_logs("new_log.txt"))

#7
class Order:
    def __init__(self, id, user, products=None):
        self.id = id
        self.user = user
        self.products = products or []
    def add_product(self, product):
        self.products.append(product)
    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]
    def total_price(self):
        return sum(p.price for p in self.products)
#8
    def most_expensive_products(self, n):
        return sorted(self.products, key=lambda p: p.price, reverse=True)[:n]
    def __str__(self):
        return f"Order(id={self.id}, user={self.user._name}, total={self.total_price()})"

u = User(1, "John Doe", "john@mail.com")
o = Order(1, u)
o.add_product(Product(1, "Laptop", 1200, "Electronics"))
o.add_product(Product(2, "Mouse", 25, "Electronics"))
print(o)
print(o.total_price())

print([p.name for p in o.most_expensive_products(1)])

#9
def price_stream(products):
    for p in products:
        yield p.price
for price in price_stream(o.products):
    print(price)

#10
class OrderIterator:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.orders):
            raise StopIteration
        result = self.orders[self.index]
        self.index += 1
        return result

o2 = Order(2, u, [Product(3, "Monitor", 450, "Electronics")])
orders = [o, o2]
it = OrderIterator(orders)
for order in it:
    print(order)


#11
import numpy as np
products = [
    Product(1, "Laptop", 1200, "Electronics"),
    Product(2, "Mouse", 25, "Electronics"),
    Product(3, "Monitor", 450, "Electronics")
]
prices = np.array([p.price for p in products])
print(prices)

#12
prices = np.array([1200.0, 25.0, 450.0])
print((np.mean(prices), np.median(prices)))

#13
prices = np.array([1200.0, 25.0, 450.0])
norm = (prices - prices.min()) / (prices.max() - prices.min())
print(norm)

#14
products = [
    Product(1,"Laptop",1200.0,"Electronics"),
    Product(2,"T-Shirt",20.0,"Clothing")
]
cats = np.array([p.category for p in products])
print(cats)

#15
cats = np.array(["Electronics", "Clothing", "Electronics"])
print(len(set(cats)))

#16
products = [
    Product(1,"Laptop",1200.0,"Electronics"),
    Product(2,"Mouse",25.0,"Electronics"),
    Product(3,"Monitor",450.0,"Electronics")
]
prices = np.array([p.price for p in products])
avg = prices.mean()
print([p for p in products if p.price > avg])

#17
arr = np.array([1200.0, 25.0, 450.0])
print(prices * 0.9)

#18
u1 = User(1, "John", "john@mail.com")
u2 = User(2, "Alice", "alice@mail.com")
orders = [
    Order(1, u1, [Product(1,"Laptop",1200.0,"Electronics")]),
    Order(2, u2, [
        Product(2,"Mouse",25.0,"Electronics"),
        Product(1,"Laptop",1200.0,"Electronics")
    ])
]

arr = np.array([[o.total_price()] for o in orders])
print(arr)

#19
arr = np.array([1200.0, 1225.0])
print(np.mean(arr))

#20
arr = np.array([1200.0, 900.0, 1500.0])
print(list(np.where(arr > 1000)[0]))

#21
import pandas as pd
from datetime import date

users = [
    User(1,"John Doe","john@example.com"),
    User(2,"Alice","alice@example.com")
]
df = pd.DataFrame([{
    "id": u._id,
    "name": u._name,
    "email": u._email,
    "registration_date": date.today()
} for u in users])
print(df)

#22
products = [
    Product(1,"Laptop",1200.0,"Electronics"),
    Product(2,"T-Shirt",20.0,"Clothing")
]
df = pd.DataFrame([{
    "id": p.id,
    "name": p.name,
    "category": p.category,
    "price": p.price
} for p in products])
print(df)

#23
users_df = pd.DataFrame({
    "id": [1, 2],
    "name": ["John", "Alice"]
})
orders_df = pd.DataFrame({
    "order_id": [101, 102],
    "user_id": [1, 2],
    "total": [1200, 25]
})
df = pd.merge(users_df, orders_df, left_on="id", right_on="user_id")
df = df[["order_id", "name", "total"]]
df = df.rename(columns={"name": "user_name"})
print(df)

#24
df = pd.DataFrame({
    "order_id": [101, 102],
    "user_name": ["John", "Alice"],
    "total": [1200, 25]
})
value = 100
print(df[df["total"] > value])

#25
df = pd.DataFrame({
    "order_id": [101, 103, 102],
    "user_name": ["John", "John", "Alice"],
    "total": [1200, 500, 25]
})
result = df.groupby("user_name", as_index=False)["total"].sum()
result.columns = ["user_name", "total_sum"]
print(result)

#26
df = pd.DataFrame({
    "order_id": [101, 103, 102],
    "user_name": ["John", "John", "Alice"],
    "total": [1200, 500, 25]
})
result = df.groupby("user_name", as_index=False)["total"].mean()
result.columns = ["user_name", "mean_total"]
print(result)

#27
df = pd.DataFrame({
    "order_id": [101, 103, 102],
    "user_name": ["John", "John", "Alice"],
    "total": [1200, 500, 25]
})
result = df.groupby("user_name", as_index=False)["order_id"].count()
result.columns = ["user_name", "orders_count"]
print(result)

#28
df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Laptop", "Mouse", "Shirt"],
    "category": ["Electronics", "Electronics", "Clothing"],
    "price": [1200, 25, 20]
})
result = df.groupby("category", as_index=False)["price"].mean()
result.columns = ["category", "mean_price"]
print(result)

#29
df = pd.DataFrame({
    "id": [1, 2],
    "name": ["Laptop", "Mouse"],
    "price": [1200, 25]
})
df["discounted_price"] = df["price"] * 0.9
print(df)

#30
df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Laptop", "Mouse", "Monitor"],
    "price": [1200, 25, 450]
})
df = df.sort_values(by="price", ascending=False)
print(df)

#31
df = pd.DataFrame({
    "order_id": [101, 102],
    "product_name": ["Laptop", "Mouse"],
    "price": [1200, 25]
})
df["quantity"] = 1
print(df)

#32
df = pd.DataFrame({
    "order_id": [101, 102],
    "product_name": ["Laptop", "Mouse"],
    "price": [1200, 25],
    "quantity": [1, 2]
})
df["total_price"] = df["price"] * df["quantity"]
print(df)

#33
df = pd.DataFrame({
    "product_name": ["Laptop", "T-Shirt"],
    "category": ["Electronics", "Clothing"],
    "price": [1200, 20]
})
result = df[df["category"] == "Electronics"]
print(result)

#34
df = pd.DataFrame({
    "product_name": ["Laptop", "Mouse", "Shirt"],
    "category": ["Electronics", "Electronics", "Clothing"]
})
result = df.groupby("category", as_index=False)["product_name"].count()
result.columns = ["category", "count"]
print(result)

#35
df = pd.DataFrame({
    "product_name": ["Laptop", "Mouse", "Shirt"],
    "category": ["Electronics", "Electronics", "Clothing"],
    "price": [1200, 25, 20]
})
result = df.groupby("category", as_index=False)["price"].mean()
result.columns = ["category", "mean_price"]
print(result)

#36
df = pd.DataFrame({
    "order_id": [101, 102],
    "total_price": [1200, 50]
})
df = df.sort_values(by="total_price", ascending=False)
print(df)

#37
df = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "total_price": [1200, 50, 500, 1500]
})
result = df.sort_values(by="total_price", ascending=False).head(3)
print(result)

#38
users = pd.DataFrame({
    "user_id": [1, 2],
    "user_name": ["John", "Alice"]
})

orders = pd.DataFrame({
    "order_id": [101, 102],
    "user_id": [1, 2],
    "total_price": [1200, 50]
})
df = pd.merge(users, orders, on="user_id")
df = df[["order_id", "user_name", "total_price"]]
print(df)

#39
df = pd.DataFrame({
    "user_name": ["John", "John", "Alice"],
    "total_price": [1200, 500, 50]
})
result = df.groupby("user_name", as_index=False)["total_price"].mean()
result.columns = ["user_name", "mean_total"]
print(result)

#40
df = pd.DataFrame({
    "user_name": ["John", "John", "Alice"],
    "order_id": [101, 103, 102]
})
result = df.groupby("user_name", as_index=False)["order_id"].count()
result.columns = ["user_name", "orders_count"]
print(result)

#41
df = pd.DataFrame({
    "user_name": ["John", "John", "Alice"],
    "total_price": [1200, 500, 50]
})
result = df.groupby("user_name", as_index=False)["total_price"].max()
result.columns = ["user_name", "max_order"]
print(result)

#42
df = pd.DataFrame({
    "user_name": ["John", "John", "John", "Alice"],
    "category": ["Electronics", "Electronics", "Clothing", "Clothing"]
})
result = df.groupby("user_name", as_index=False)["category"].nunique()
result.columns = ["user_name", "unique_categories"]
print(result)

#43
df = pd.DataFrame({
    "user_name": ["John", "Alice"],
    "total_sum": [1700, 25]
})
df["VIP"] = df["total_sum"] > 1000
print(df)

#44
df = pd.DataFrame({
    "user_name": ["John", "Alice", "Bob"],
    "total_sum": [1700, 25, 1700],
    "mean_total": [850, 25, 600]
})
df = df.sort_values(by=["total_sum", "mean_total"], ascending=[False, True])
print(df)

#45
df = pd.DataFrame({
    "user_name": ["John", "John", "Alice"],
    "order_id": [101, 103, 102],
    "total_price": [1200, 500, 25],
    "category": ["Electronics", "Clothing", "Clothing"]
})
report = df.groupby("user_name").agg(
    total_orders=("order_id", "count"),
    total_sum=("total_price", "sum"),
    mean_total=("total_price", "mean"),
    max_order=("total_price", "max"),
    unique_categories=("category", "nunique")
).reset_index()
report["VIP"] = report["total_sum"] > 1000
print(report)