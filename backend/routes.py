from flask import Blueprint, request, jsonify
from database.models import create_student
from assessment import generate_questions, evaluate_answers, generate_learning_plan

ai_routes = Blueprint("ai_routes", __name__)

# -------------------------
# Health Check
# -------------------------
@ai_routes.route("/")
def home():
    return jsonify({"status": "AI Personalized Learning Platform Backend Running"})


# -------------------------
# Register
# -------------------------
@ai_routes.route("/ai/register", methods=["POST"])
def register():
    data = request.json
    return jsonify(create_student(
        data["name"],
        data["email"],
        data["password"],
        data["age"],
        data["class"],
        data["subject_interest"]
    ))


# -------------------------
# Get Assessment
# -------------------------
@ai_routes.route("/ai/get_exam", methods=["POST"])
def get_exam():
    data = request.json
    questions = generate_questions(data["class"], data["subject"])
    return jsonify({"questions": questions})


# -------------------------
# Submit Assessment
# -------------------------
@ai_routes.route("/ai/submit_exam", methods=["POST"])
def submit_exam():
    data = request.json

    questions = data["questions"]
    answers = data["answers"]
    student_class = data["class"]
    subject = data["subject"]

    result = evaluate_answers(questions, answers)
    plan = generate_learning_plan(result, student_class, subject)

    return jsonify({
        "result": result,
        "learning_plan": plan
    })