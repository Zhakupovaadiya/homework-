from flask import Flask, jsonify
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)
def my_task():
    result=sum(range(1,1000))
    return result

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

#1
class Player:
    def __init__(self,_id,_name,_hp):
        self._id = _id
        self._name = _name.strip().title()
        self._hp = _hp if _hp >=0 else 0
    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"
    def __del__(self):
        print(f"Player{self._name} удалён")
@app.route("/player")
def get_player():
    p = Player(1, " john ", 120)
    return str(p)
if __name__ == "__main__":
    app.run(port=5000)

#2
class Player:
    def __init__(self,id, name,hp):
        self.id = id
        self.name = name
        self.hp = hp