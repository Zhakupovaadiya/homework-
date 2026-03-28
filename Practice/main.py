with open (r"C:\Users\Anuar\Desktop\pycharm\Practice\data.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
print("hello")

with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\file.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")
with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\file.txt", "r", encoding="utf-8") as f:
    print(f.read())
names=["Anna", "John", "Michael", "David"]
with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\names.txt", "w", encoding="utf-8") as f:
    for name in names:
        f.write(name + "\n")
with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\names.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip().capitalize())



import csv
names = ["Anna", "John", "Michael", "David"]
with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\names.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for name in names:
        writer.writerow([name])
with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\names.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0].capitalize())

with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\file.csv", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")
with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\file.csv", "r", encoding="utf-8") as f:
    print(f.read())

with open(r"C:\Users\Anuar\Desktop\pycharm\Practice\data.csv", "w", encoding="utf-8") as f:
    f.write("how are you?\n")