import random
money=100
health=100
mood=100
events = ["work","illness","found_money","rest"]

for day in range(1,11):
    print(f"День {day}")
    print(f"Деньги:{money}, Здоровье: {health}, Настроение: {mood}")
    event = random.choice(events)
    print("Событие:", event)

    print("Выбери действие: 1-работать, 2-отдыхать, 3-лечиться")
    choice = input("Твой выбор: ")

    if choice == "1":
        money += 50
        health -= 10
        mood -= 5
    elif choice == "2":
        mood += 10
        health += 5
        health -= 20
    elif choice == "3":
        health += 20
        money -= 30
    else:
        print("Error")

    if event == "work":
        money += 50
        mood -= 10
    elif event == "illness":
        health -= 20
    elif event == "found_money":
        money += 50
    elif event == "rest":
        mood += 20
    if health <= 0 or mood <= 0:
        print("Ты проиграл...")
        break
print(f"GAME OVER")
print(f"Деньги: {money}, Здоровье: {health}, Настроение: {mood}")