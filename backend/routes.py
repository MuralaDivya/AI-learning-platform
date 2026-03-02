import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, request, jsonify
from database.models import create_student
from assessment import generate_questions, evaluate_answers

ai_routes = Blueprint("ai_routes", __name__)

@ai_routes.route("/ai/register", methods=["POST"])
def register():
    data = request.json
    return jsonify(create_student(
        data.get("name"),
        data.get("email"),
        data.get("password"),
        data.get("age"),
        data.get("class"),
        data.get("subject_interest")
    ))

@ai_routes.route("/ai/get_exam", methods=["POST"])
def get_exam():
    data = request.json
    questions = generate_questions(data.get("class"), data.get("subject"))
    return jsonify({"questions": questions})

@ai_routes.route("/ai/submit_exam", methods=["POST"])
def submit_exam():
    data = request.json
    result = evaluate_answers(data.get("answers"))
    return jsonify(result)