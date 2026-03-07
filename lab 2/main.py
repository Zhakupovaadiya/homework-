logs=["2026-02-01;user_1;LOGIN",
"2026-02-01;user_2;LOGIN",
"2026-02-01;user_1;BUY;120",
"2026-02-01;user_3;LOGIN",
"2026-02-01;user_2;BUY;300",
"2026-02-01;user_1;BUY;50",
"2026-02-01;user_2;LOGOUT"
]
with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\shop_logs.txt", "w", encoding="utf-8") as f:
    for line in logs:
        f.write(line)

file = open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\shop_logs.txt", "r")
unique_users = set()
total_buys = 0
total_sum = 0
user_spending = {}
for line in file:
    parts = line.strip().split(";")
    data = parts[0]
    user_id = parts[1]
    action = parts[2]
    sum = parts[3]
    print(user_id)
    unique_users.add(user_id)
    if action == "BUY":
        total_buys += 1
        amount = int(parts[3])
        total_sum += amount

file.close()
#средний чек
if total_buys > 0:
    mean_check = total_sum/total_buys
else:
    mean_check = 0
print(mean_check)

#пользователя, который потратил больше всего
max_user = ""
max_spent = 0
for user in user_spending:
    if user_spending[user]>max_spent:
        max_spent = user_spending[user]
        max_user = user
print(max_user)

with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\report.txt", "w", encoding="utf-8") as report:
    report.write("Уникальных пользователей: " + str(len(unique_users)) + "\n")
    report.write("Всего покупок: " +str(total_buys) + "\n")
    report.write("Общая сумма: " +str(total_sum) + "\n")
    report.write("Самый активный покупатель: " + max_user + "\n")
    report.write("Средний чек: " +str(mean_check) + "\n")


#2
import csv
employees_data=[
    {"name": "Ali","department": "IT","salary": 500000},
    {"name": "Dana","department": "HR","salary": 300000},
    {"name": "Arman","department": "IT","salary": 600000},
    {"name": "Aruzhan","department": "Marketing","salary": 400000},
    {"name": "Dias","department": "IT","salary": 450000}
]
with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\employees.csv", "w",newline="", encoding="utf-8") as f:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for e in employees_data:
        writer.writerow(e)
employees = []
with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\employees.csv",newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["salary"]=int(row["salary"])
        employees.append(row)
#средняя зарплата
total_salary=0
for e in employees:
    total_salary += e["salary"]
average_salary = total_salary/len(employees)
print("средняя зарплата:", average_salary)
#группировка по отделам
#средняя зарплата по каждому отделу
departments = {}
for e in employees:
    dept = e["department"]
    if dept not in departments:
        departments[dept] = {"total": e["salary"],"count": 1}
    else:
        departments[dept]["total"] += e["salary"]
        departments[dept]["count"] += 1
dept_avg = {}
for dept in departments:
    total = departments[dept]["total"]
    count = departments[dept]["count"]
    dept_avg[dept] = total/count
    print(dept, ":", dept_avg[dept])

#отдел с самой высокой средней зарплатой
max_department = None
max_avg_salary = 0
for dept in dept_avg:
    if dept_avg[dept] > max_avg_salary:
        max_avg_salary = dept_avg[dept]
        max_department = dept
print("отдел с самой высокой средней зарплатой:", max_department)

#самого высокооплачиваемого сотрудника
highest_paid = employees[0]
for e in employees:
    if e["salary"] > highest_paid["salary"]:
        highest_paid = e
print("высокооплачиваемый сотрудник:", highest_paid["name"], highest_paid["salary"])

#список сотрудников с зарплатой выше средней
high_salary_emp = []
for e in employees:
    if e["salary"]>average_salary:
        high_salary_emp.append(e)
for e in high_salary_emp:
    print("список сотрудников с зарплатой выше средней:", e["name"], e["salary"])
with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\high_salary.csv", "w",newline="", encoding="utf-8") as f:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for e in high_salary_emp:
        writer.writerow(e)

#3
import json
orders_data = [
  {
    "order_id": 1,
    "user": "Ali",
    "items": ["phone", "case"],
    "total": 300000
  },
  {
    "order_id": 2,
    "user": "Dana",
    "items": ["laptop"],
    "total": 800000
  },
  {
    "order_id": 3,
    "user": "Ali",
    "items": ["mouse", "keyboard"],
    "total": 70000
  }
]
with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\orders.json", "w",newline="", encoding="utf-8") as f:
    json.dump(orders_data, f, ensure_ascii=False, indent=4)
with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\orders.json", "r", encoding="utf-8") as f:
    orders = json.load(f)
total_revenue = 0
user_orders = {}
total_items = 0
item_frequency = {}
top_order_amount = 0
top_user = ""
#общую сумму всех заказов
for order in orders:
    total_revenue += order["total"]
#сколько заказов сделал каждый пользователь
    user = order["user"]
    user_orders[user] = user_orders.get(user, 0) + 1
#сколько всего было продано товаров (количество items)
    total_items += len(order["items"])
#пользователя с самым дорогим заказом
    if order["total"] > top_order_amount:
        top_order_amount = order["total"]
        top_user = order["user"]
#самый популярный товар (встречается чаще всего)
    for item in order["items"]:
        item_frequency[item] = item_frequency.get(item, 0) + 1
most_popular_item = max(item_frequency, key=item_frequency.get) if item_frequency else None

print("Общая сумма заказов:",total_revenue)
print("Заказов по пользователям:",user_orders)
print("Всего продано товаров:",total_items)
print("Пользователь с самым дорогим заказом:",top_user)
print("Самый популярный товар:",most_popular_item)

summary = {
    "total_revenue": total_revenue,
    "top_user": user_orders,
    "most_popular_item": most_popular_item,
    "total_orders": total_items,
}
with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=4)

#4
t_data=[
    ["user_id", "amount"],
    ["user_1", "5000"],
    ["user_2", "10000"],
    ["user_1", "700000"],
    ["user_3", "3000"],
    ["user_2", "900000"],
    ["user_4", "2000"],
]
with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\transactions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(t_data)

suspicious_transactions = []
suspicious_users = set()
user_op_count = {}
total_suspicious = 0

with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\transactions.csv", newline="", encoding="utf-8") as csvf:
    reader = csv.DictReader(csvf)
    for row in reader:
        user_id = row["user_id"]
        amount = int(row["amount"])
        user_op_count[user_id] = user_op_count.get(user_id, 0) + 1
#все подозрительные транзакции
        if amount > 500000:
            suspicious_transactions.append((user_id, amount))
#общую сумму подозрительных операций
            total_suspicious += amount
#всех подозрительных пользователей
            suspicious_users.add(user_id)

for user, count in user_op_count.items():
    if count > 3:
        suspicious_users.add(user)

with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\fraud_report.txt", "w", encoding="utf-8") as f:
    f.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
    f.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
    f.write(f"Список пользователей: {', '.join(suspicious_users)}\n")
    f.write(f"Общая сумма подозрительных операций: {total_suspicious}\n")

with open(r"C:\Users\Anuar\Desktop\pycharm\lab 2\fraud_users.json", "w", encoding="utf-8") as f:
    json.dump(list(suspicious_users), f, ensure_ascii=False, indent=4)

print("Подозрительные транзакции:", suspicious_transactions)
print("Подозрительные пользователи:", suspicious_users)
print("Общая сумма подозрительных операций:", total_suspicious)
