# backend/assessment.py

import random

# 📚 CLASS-WISE SYLLABUS DATABASE
SYLLABUS = {
    "1": {
        "Math": ["Addition", "Subtraction", "Counting"],
        "Science": ["Plants", "Animals", "Body Parts"]
    },
    "2": {
        "Math": ["Addition", "Subtraction", "Multiplication"],
        "Science": ["Living Things", "Water", "Air"]
    },
    "3": {
        "Math": ["Addition", "Subtraction", "Multiplication", "Division"],
        "Science": ["Plants", "Animals", "Soil"]
    },
    "4": {
        "Math": ["Fractions", "Multiplication", "Division"],
        "Science": ["Human Body", "Energy", "Matter"]
    },
    "5": {
        "Math": ["Fractions", "Decimals", "LCM", "HCF"],
        "Science": ["Plants", "Animals", "Ecosystem"]
    },
    "6": {
        "Math": ["Integers", "Algebra Basics", "Fractions"],
        "Science": ["Food", "Materials", "Motion"]
    },
    "7": {
        "Math": ["Algebra", "Ratio", "Proportion"],
        "Science": ["Nutrition", "Respiration", "Transportation"]
    },
    "8": {
        "Math": ["Linear Equations", "Mensuration"],
        "Science": ["Force", "Friction", "Sound"]
    },
    "9": {
        "Math": ["Polynomials", "Trigonometry"],
        "Science": ["Motion", "Atoms", "Tissues"]
    },
    "10": {
        "Math": ["Quadratic Equations", "Trigonometry"],
        "Science": ["Electricity", "Magnetism", "Chemistry Basics"]
    },
    "11": {
        "Math": ["Calculus", "Permutations"],
        "Physics": ["Kinematics", "Laws of Motion"],
        "Chemistry": ["Atomic Structure", "Thermodynamics"]
    },
    "12": {
        "Math": ["Integrals", "Probability"],
        "Physics": ["Electrostatics", "Optics"],
        "Chemistry": ["Organic Chemistry", "Electrochemistry"]
    },
    "BTech": {
        "AI": ["Machine Learning", "Neural Networks", "Data Science"],
        "DBMS": ["SQL", "Normalization", "Transactions"],
        "Math": ["Linear Algebra", "Probability"],
        "OS": ["Processes", "Memory Management"]
    }
}

# ==============================
# 🧠 QUESTION GENERATION ENGINE
# ==============================
def generate_questions(student_class, subject):
    student_class = str(student_class)
    subject = subject.strip().title()

    if student_class not in SYLLABUS:
        return [{"q": "Invalid class level", "a": "NA", "topic": "NA"}]

    if subject not in SYLLABUS[student_class]:
        return [{"q": f"No syllabus data for {subject} in Class {student_class}", "a": "NA", "topic": "NA"}]

    topics = SYLLABUS[student_class][subject]
    questions = []

    for i in range(10):  # 10 questions
        topic = random.choice(topics)

        if subject == "Math":
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            q = f"{a} + {b} = ?"
            ans = a + b

        elif subject == "Science":
            q = f"What is {topic}?"
            ans = "Descriptive"

        elif subject in ["AI", "DBMS", "OS", "Physics", "Chemistry"]:
            q = f"Explain {topic}"
            ans = "Conceptual"

        else:
            q = f"Describe {topic}"
            ans = "Conceptual"

        questions.append({
            "topic": topic,
            "q": q,
            "a": ans
        })

    return questions


# ==============================
# 🎯 EVALUATION ENGINE
# ==============================
def evaluate_answers(answers):
    score = 0
    weak_topics = {}
    strong_topics = {}

    for ans in answers:
        correct = str(ans["correct"]).strip().lower()
        user = str(ans["user"]).strip().lower()
        topic = ans["topic"]

        if user == correct:
            score += 1
            strong_topics[topic] = strong_topics.get(topic, 0) + 1
        else:
            weak_topics[topic] = weak_topics.get(topic, 0) + 1

    total = len(answers)
    percentage = (score / total) * 100 if total > 0 else 0

    ability = "Beginner"
    if percentage >= 80:
        ability = "Advanced"
    elif percentage >= 50:
        ability = "Intermediate"

    return {
        "score": score,
        "total": total,
        "percentage": round(percentage, 2),
        "ability_level": ability,
        "weak_topics": weak_topics,
        "strong_topics": strong_topics
    }