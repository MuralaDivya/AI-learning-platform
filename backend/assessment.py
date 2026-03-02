import json
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SYLLABUS_PATH = os.path.join(BASE_DIR, "syllabus.json")


def load_syllabus():
    with open(SYLLABUS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# -------------------------------
# QUESTION GENERATION
# -------------------------------
def generate_questions(student_class, subject, total_questions=20):
    syllabus = load_syllabus()

    student_class = str(student_class)

    if student_class not in syllabus:
        return [{
            "q": "No syllabus data for this class yet",
            "options": ["N/A"],
            "a": "N/A",
            "chapter": "N/A"
        }]

    if subject not in syllabus[student_class]:
        return [{
            "q": "No subject data found for this subject",
            "options": ["N/A"],
            "a": "N/A",
            "chapter": "N/A"
        }]

    chapters = syllabus[student_class][subject]  # list

    all_questions = []

    for chapter_obj in chapters:
        chapter_name = chapter_obj.get("chapter", "General")
        qlist = chapter_obj.get("questions", [])

        for q in qlist:
            all_questions.append({
                "q": q["q"],
                "options": q["options"],
                "a": q["a"],
                "chapter": chapter_name
            })

    # remove duplicates
    unique = []
    seen = set()
    for q in all_questions:
        if q["q"] not in seen:
            seen.add(q["q"])
            unique.append(q)

    random.shuffle(unique)

    return unique[:total_questions]


# -------------------------------
# ANSWER EVALUATION
# -------------------------------
def evaluate_answers(questions, user_answers):
    score = 0
    topic_stats = {}

    for i, q in enumerate(questions):
        correct = q["a"]
        user = user_answers[i]
        chapter = q["chapter"]

        if chapter not in topic_stats:
            topic_stats[chapter] = {"correct": 0, "total": 0}

        topic_stats[chapter]["total"] += 1

        if user == correct:
            score += 1
            topic_stats[chapter]["correct"] += 1

    percentage = (score / len(questions)) * 100

    if percentage >= 85:
        level = "Advanced"
    elif percentage >= 60:
        level = "Intermediate"
    else:
        level = "Beginner"

    weak_topics = []
    strong_topics = []

    for topic, data in topic_stats.items():
        acc = (data["correct"] / data["total"]) * 100
        if acc < 50:
            weak_topics.append(topic)
        else:
            strong_topics.append(topic)

    return {
        "score": score,
        "total": len(questions),
        "percentage": round(percentage, 2),
        "level": level,
        "weak_topics": weak_topics,
        "strong_topics": strong_topics
    }


# -------------------------------
# LEARNING PLAN GENERATOR (AI ENGINE)
# -------------------------------
def generate_learning_plan(result_data, student_class, subject):
    level = result_data["level"]
    weak = result_data["weak_topics"]
    strong = result_data["strong_topics"]

    plan = {
        "level": level,
        "daily_plan": [],
        "weekly_plan": [],
        "focus_topics": weak,
        "revision_topics": strong,
        "strategy": ""
    }

    if level == "Beginner":
        plan["strategy"] = "Concept building + basics + slow learning + repetition"
        speed = "Slow"
    elif level == "Intermediate":
        plan["strategy"] = "Concept strengthening + practice + tests"
        speed = "Medium"
    else:
        plan["strategy"] = "Advanced problem solving + mock tests + speed learning"
        speed = "Fast"

    # Daily Plan
    for topic in weak:
        plan["daily_plan"].append({
            "topic": topic,
            "tasks": [
                "Learn concepts",
                "Watch explanation video",
                "Practice basic questions",
                "Solve examples"
            ]
        })

    # Weekly Plan
    for topic in weak:
        plan["weekly_plan"].append({
            "topic": topic,
            "tasks": [
                "Deep learning",
                "Practice set",
                "Mini test",
                "Revision"
            ]
        })

    plan["learning_speed"] = speed
    plan["subject"] = subject
    plan["class"] = student_class

    return plan