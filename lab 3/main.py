#1
check = lambda x: "положительное" if x > 0 else ("отрицательное" if x < 0 else "ноль")
print(check(5))
print(check(-3))
print(check(0))
#положительное
#отрицательное
#ноль

#2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
result = sorted(words, key=lambda w: (len(w), w[0]))
print(result)
#['дом', 'кот', 'арбуз', 'ананас', 'машина']

#3
numbers = [5,12,7,20,33,8]
result = list(filter(lambda x: x%2==0 and x>10, numbers))
print(result)
#[12, 20]

#4
numbers = [1,2,3,4,5,6]
result = list(map(lambda x: x**2 if x%2==0 else x*3, numbers))
print(result)
#[3, 4, 9, 16, 15, 36]

#5
compare = lambda a,b: "a больше" if a>b else ("b больше" if b>a else "равны")
print(compare(10,7))
print(compare(3,5))
print(compare(4,4))
#a больше
#b больше
#равны

#6
numbers = [0,-3,5,-7,8]
result = [(lambda x: "положительное" if x>0 else ("отрицательное" if x<0 else "ноль"))(x) for x in numbers]
print(result)
#['ноль', 'отрицательное', 'положительное', 'отрицательное', 'положительное']


#генераторы
#1
def even_numbers(n):
    for i in range(1,n+1):
        if i%2==0:
            if i%4==0:
                yield "кратно 4"
            else:
                yield i
for x in even_numbers(10):
    print(x)
#2
#кратно 4
#6
#кратно 4
#10


#2
def filter_words(words):
    for w in words:
        if len(w)>4:
            if "а" in w:
                yield "с а"
            else:
                yield w
words = ["кот","машина","арбуз","дом"]
for w in filter_words(words):
    print(w)
#с а
#с а

#3
def infinite_numbers():
    n = 1
    while True:
        if n%3==0 and n%5==0:
            yield "FizzBuzz"
        elif n%3==0:
            yield "Fizz"
        elif n%5==0:
            yield "Buzz"
        else:
            yield n
        n += 1
gen = infinite_numbers()
for _ in range(10):
    print(next(gen))
#1
#2
#Fizz
#4
#Buzz
#Fizz
#7
#8
#Fizz
#Buzz


#4
def squares(n):
    for i in range(1,n+1):
        sq = i*i
        if sq%2==0:
            yield "чётный квадрат"
        else:
            yield sq
for x in squares(5):
    print(x)
#1
#чётный квадрат
#9
#чётный квадрат
#25


#Итераторы и Comprehension
#1
result = [x*x for x in range(1,21) if x%2==0]
print(result)
#[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


#2
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = [(lambda row: row[0]*row[1]*row[2])(row) for row in matrix]
print(result)
#[6, 120, 504]


#3
words = ["кот","машина","ананас","дом"]
result = [w for w in words if len(w)>4 and "а" not in w]
print(result)
#[]


#4
numbers = [1,2,3,4,5]
result = {x:("чётное" if x%2==0 else "нечётное") for x in numbers}
print(result)
#{1: 'нечётное', 2: 'чётное', 3: 'нечётное', 4: 'чётное', 5: 'нечётное'}


#5
matrix = [[1,2],[3,4],[5,6]]
result = [x for row in matrix for x in row]
print(result)
#[1, 2, 3, 4, 5, 6]


#6
result = ["FizzBuzz" if x%3==0 and x%5==0 else
          "Fizz" if x%3==0 else
          "Buzz" if x%5==0 else x
          for x in range(1,21)]
print(result)
#[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']


#Смешанные задачи
#1
def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
def special_numbers(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            yield "FizzBuzz"
        elif i%3==0:
            yield "Fizz"
        elif i%5==0:
            yield "Buzz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i
for x in special_numbers(15):
    print(x)
#1
#простое
#Fizz
#4
#Buzz
#Fizz
#простое
#8
#Fizz
#Buzz
#простое
#Fizz
#простое
#14
#FizzBuzz


#2
words = ["кот","машина","арбуз","дом","ананас"]
result = [(lambda w:
           (w.upper()+"*" if "а" in w else w.upper()) if len(w)>4
           else ("short*" if "а" in w else "short"))(w)
          for w in words]
print(result)
#['short', 'МАШИНА*', 'АРБУЗ*', 'short', 'АНАНАС*']


#3
def process_numbers(numbers):
    filtered = filter(lambda x: x>=0, numbers)
    mapped = map(lambda x: x/2 if x%2==0 else x*3+1, filtered)
    for x in mapped:
        yield x
numbers = [5,-2,8,0,-7,3]
for x in process_numbers(numbers):
    print(x)
#16
#4.0
#0.0
#10


#4
students = [("Иван",85),("Анна",72),("Пётр",90),("Мария",60)]
grade = lambda x: "Отлично" if x>=90 else ("Хорошо" if x>=70 else "Удовлетворительно")
result = {name:grade(score) for name,score in students}
print(result)
#{'Иван': 'Хорошо', 'Анна': 'Хорошо', 'Пётр': 'Отлично', 'Мария': 'Удовлетворительно'}


#5
def matrix_transform(matrix):
    for row in matrix:
        for x in row:
            if x%2==0 and x%3==0:
                yield "кратно 6"
            elif x%2==0:
                yield "чётное"
            elif x%3==0:
                yield "кратно 3"
            else:
                yield x
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
for x in matrix_transform(matrix):
    print(x)
#1
#чётное
#кратно 3
#чётное
#5
#кратно 6
#7
#чётное
#кратно 3

#map and filter
#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

#2
words = ["кот", "машина", "арбуз", "дом"]
result = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))
print(result)

#3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#4
numbers = [0, 5, 12, 7, 20, -3, 8]
result = list(map(lambda x: x/2 if x % 2 == 0 else x*3,
filter(lambda x: x > 5, numbers)))
print(result)