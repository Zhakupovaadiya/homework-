
from flask import Flask, jsonify
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)
def my_task():
    return sum(range(1,1000))

@app.route("/run-task")
def run_task():
    return jsonify({"status":"ok","result":my_task()})

@app.route("/sum")
def sum_ab():
    a=5
    b=3
    return str(a+b)

@app.route("/")
def home():
    return "Сервер работает"
















#1-2
class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = max(0, hp)
    def __del__(self):
        print(f"Player {self._name} удалён")
    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"
    def __repr__(self):
        return self.__str__()
    @classmethod
    def from_string(cls, data: str):
        parts = [x.strip() for x in data.split(",")]
        if len(parts) != 3:
            raise ValueError("Invalid format")
        return cls(int(parts[0]), parts[1], int(parts[2]))
@app.route("/prvplayer")
def prvplayer():
    p = Player(1, " john ", 120)
    return str(p)

@app.route("/player")
def get_player():
    p = Player.from_string("2, alice , 90")
    return str(p)


#3
class Item:
    def __init__(self,id,name,power):
        self.id = id
        self.name = name.strip().title()
        self.power = power
    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
    def __eq__(self,other):
        return isinstance(other,Item) and self.id == other.id
    def __hash__(self):
        return hash(self.id)
@app.route("/item")
def get_item():
    i = Item(1, " Sword ", 50)
    return str(i)


#4
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        if item.id not in [i.id for i in self.items]:
            self.items.append(item)
    def remove_item(self,item_id: int):
        self.items = [i for i in self.items if i.id != item_id]
    def get_items(self):
        return self.items
    def get_strong_items(self, min_power):
        return [x for x in self.items if x.power >= min_power]
    def unique_items(self):
        return set(self.items)
    def to_dict(self):
        return {item.id: item for item in self.items}
    def __iter__(self):
        return iter(self.items)

@app.route("/inventory")
def inventory_route():
    inv = Inventory()
    inv.add_item(Item(2, "shield", 30))
    inv.add_item(Item(3, "sword", 50))

    result = [str(i) for i in inv.get_items()]
    return "<br>".join(result)

#5
@app.route("/filtered")
def filtered():
    inv=Inventory()
    inv.add_item(Item(2, "shield", 30))
    inv.add_item(Item(3, "sword", 50))
    strong=inv.get_strong_items(40)
    return jsonify([str(i) for i in strong])


#6
from datetime import datetime
class Event:
    def __init__(self,type,data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()
    def __str__(self):
        return f"Event(type={self.type}, data={self.data}, timestamp={self.timestamp})"
    def __repr__(self):
        return self.__str__()

@app.route("/event")
def get_event():
    e = Event("ATTACK", {"damage": 20})
    return str(e)


#7
class EventPlayer(Player):
    def __init__(self,_id,name,hp):
        super().__init__(_id,name,hp)
        self._inventory = []
    def handle_event(self, event):
        if event.type == "ATTACK":
            self._hp -= event.data.get("damage", 0)
        elif event.type == "HEAL":
            self._hp += event.data.get("heal", 0)
        elif event.type == "LOOT":
            self._inventory.append(event.data.get("item"))
    def __str__(self):
        return f"{self._name}(hp={self._hp})"
class Warrior(EventPlayer):
    def handle_event(self, event):
        if event.type == "ATTACK":
            self._hp -= event.data.get("damage", 0)*0.9
        else:
            super().handle_event(event)
class Mage(EventPlayer):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power *=1.1
            super().handle_event(event)
@app.route("/eventpl")
def eventpl():
    p = Warrior(1, "john", 100)
    e = Event("ATTACK", {"damage": 50})
    p.handle_event(e)
    return str(p)

#8-9
class Logger:
    @staticmethod
    def log(event,player,filename):
        with open(filename,"a",encoding="utf-8") as f:
            f.write(f"{event.timestamp};{player._id};{event.type};{event.data}\n")
    @staticmethod
    def read_logs(filename):
        events = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                ts, pid, etype, data = line.strip().split(";")
                events.append(Event(etype, eval(data)))
        return events
@app.route("/task8")
def task8():
    p = Player(1, "john", 100)
    e = Event("ATTACK", {"damage": 20})
    Logger.log(e, p, "log.txt")
    return "Logged"
@app.route("/read")
def read():
    events = Logger.read_logs("log.txt")
    return "<br>".join(str(e) for e in events)


#10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        val = self.events[self.index]
        self.index += 1
        return val
@app.route("/itera")
def itera():
    events = [Event("ATTACK", {"damage": 10}), Event("HEAL", {"heal": 5})]
    it = EventIterator(events)
    return "<br>".join(str(e) for e in it)


#11
def damage_stream(events):
    for e in events:
        if e.type == "ATTACK":
            yield e.data.get("damage", 0)
@app.route("/damage")
def damage():
    events = [Event("ATTACK", {"damage": 10}), Event("HEAL", {"heal": 5})]
    return str(list(damage_stream(events)))

#12
import random
def generate_events(players, items, n):
    types = ["ATTACK", "HEAL", "LOOT"]
    events = []
    for _ in range(n):
        for p in players:
            t = random.choice(types)
            if t == "ATTACK":
                events.append(Event(t, {"damage": random.randint(5, 20)}))
            elif t == "HEAL":
                events.append(Event(t, {"heal": random.randint(5, 20)}))
            else:
                events.append(Event(t, {"item": random.choice(items)}))
    return events
@app.route("/sim")
def sim():
    players = [Player(1, "john", 100)]
    items = [Item(1, "sword", 50)]
    events = generate_events(players, items, 2)
    return "<br>".join(str(e) for e in events)


#13
def analyze_logs(events):
    total_damage = sum(e.data.get("damage", 0) for e in events if e.type == "ATTACK")
    event_types = [e.type for e in events]
    most_common = max(set(event_types), key=event_types.count)
    return {
        "total_damage": total_damage,
        "most_common_event": most_common
    }
@app.route("/analyze")
def analyze():
    events = [Event("ATTACK", {"damage": 10}), Event("ATTACK", {"damage": 20})]
    return jsonify(analyze_logs(events))


#14
decide_action = lambda hp, inv: "HEAL" if hp < 30 else ("LOOT" if not inv else "ATTACK")
@app.route("/AI")
def AI():
    return decide_action(20, [])


#15 7 сияқты
#16
class PlayerEncaps:
    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name
        self.__hp = hp
    @property
    def hp(self):
        return self.__hp
    def take_damage(self, dmg):
        self.__hp -= dmg
@app.route("/prv")
def prv():
    p = PlayerEncaps(1, "john", 100)
    p.take_damage(20)
    return str(p.hp)

#17
@app.route("/dele")
def dele():
    p = Player(1, "john", 100)
    del p
    return "deleted"


#18
@app.route("/task18")
def task18():
    inv = Inventory()
    inv.add_item(Item(1, "sword", 50))
    return "<br>".join(str(i) for i in inv)


#19
def analyze_inventory(inventories):
    all_items = [item for inv in inventories for item in inv.items]
    unique = set(all_items)
    top = max(all_items, key=lambda x: x.power)
    return {
        "unique_items": len(unique),
        "top_power": str(top)
    }
@app.route("/task19")
def task19():
    inv = Inventory()
    inv.items.append(Item(1, "sword", 50))
    inv.items.append(Item(2, "axe", 70))

    return jsonify(analyze_inventory([inv]))


#20
@app.route("/final")
def final():
    players = [EventPlayer(1, "john", 100)]
    items = [Item(1, "sword", 50)]
    events = generate_events(players, items, 3)
    for e in events:
        for p in players:
            p.handle_event(e)
    stats = analyze_logs(events)
    return jsonify({
        "players": [str(p) for p in players],
        "stats": stats
    })
if __name__ == "__main__":
    app.run(port =5000,debug=True)



