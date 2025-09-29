# app/routes.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Todo  # ✅ only import the model

todo_bp = Blueprint("todo_bp", __name__)


@todo_bp.route('/',methods=['GET'])
def hello():
    return jsonify({'message':"Its Working"})

@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    return jsonify([t.to_dict() for t in todos])  # ✅ now will work

@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.json
    todo = Todo(text=data.get("text", ""))
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201

@todo_bp.route("/todos/<int:id>", methods=["PATCH"])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.done = request.json.get("done", todo.done)
    db.session.commit()
    return jsonify(todo.to_dict())

@todo_bp.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted"}), 200
