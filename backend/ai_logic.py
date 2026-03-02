def generate_ai_plan(data):

    subject = data.get("subject")
    goal = data.get("goal")
    level = data.get("level")
    speed = data.get("learning_speed")
    weak_topics = data.get("weak_topics", [])
    strong_topics = data.get("strong_topics", [])

    preparation_plan = []
    practice_sets = []
    tests = []

    # Preparation Plan
    for topic in weak_topics:
        preparation_plan.append(f"Revise basics of {topic}")
        preparation_plan.append(f"Concept clarity sessions for {topic}")
        preparation_plan.append(f"Video learning for {topic}")

    for topic in strong_topics:
        preparation_plan.append(f"Advanced problems in {topic}")

    # Practice sets
    for topic in weak_topics:
        practice_sets.append(f"Daily practice set for {topic}")

    # Tests
    for topic in weak_topics:
        tests.append(f"Weekly test on {topic}")

    videos = [
        {"title": f"{subject} syllabus videos", "link": f"https://www.youtube.com/results?search_query={subject}+syllabus"},
        {"title": f"{subject} topic lectures", "link": f"https://www.youtube.com/results?search_query={subject}+lectures"}
    ]

    return {
        "status": "success",
        "subject": subject,
        "goal": goal,
        "level": level,
        "learning_speed": speed,
        "weak_topics": weak_topics,
        "strong_topics": strong_topics,
        "preparation_plan": preparation_plan,
        "practice_sets": practice_sets,
        "tests": tests,
        "videos": videos
    }