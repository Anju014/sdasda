from flask import Flask,jsonify, request
from classifier import  get_prediction

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/predict", methods=["POST"])
def predict_data():
  image = request.files.get("digit")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200



if (__name__ == "__main__"):
    app.run(debug=True)