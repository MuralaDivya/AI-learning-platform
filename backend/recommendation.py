<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Learning Recommendations</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <h1>AI Personalized Learning System</h1>
    <p class="subtitle">Your Intelligent Study Plan</p>

    <div class="form-box" id="aiBox">

        <h3>📘 Student Learning Profile</h3>
        <p><strong>Subject:</strong> <span id="r_subject"></span></p>
        <p><strong>Goal:</strong> <span id="r_goal"></span></p>
        <p><strong>Weak Area:</strong> <span id="r_weak"></span></p>
        <p><strong>Skill Level:</strong> <span id="r_skill"></span></p>
        <p><strong>Learning Speed:</strong> <span id="r_speed"></span></p>
        <p><strong>Preferred Format:</strong> <span id="r_format"></span></p>

        <hr>

        <h3>📚 What to Learn</h3>
        <ul id="what_list"></ul>

        <h3>🧠 How to Learn</h3>
        <ul id="how_list"></ul>

        <h3>🗓 Daily Study Plan</h3>
        <ul id="daily_list"></ul>

        <h3>📖 Learning Resources</h3>
        <ul id="resource_list"></ul>

        <h3>🎥 Video Learning</h3>
        <ul id="video_list"></ul>

        <h3>✍ Practice Strategy</h3>
        <ul id="practice_list"></ul>

        <button onclick="goToProgress()">Track Learning Progress</button>

    </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function(){

    const aiDataRaw = localStorage.getItem("ai_data");

    if(!aiDataRaw){
        document.getElementById("aiBox").innerHTML = "<h3>No AI Data Found. Complete Assessment First.</h3>";
        return;
    }

    const aiData = JSON.parse(aiDataRaw);

    // Basic profile
    document.getElementById("r_subject").innerText = aiData.subject;
    document.getElementById("r_goal").innerText = aiData.goal;
    document.getElementById("r_weak").innerText = aiData.weak_area;
    document.getElementById("r_skill").innerText = aiData.skill_level;
    document.getElementById("r_speed").innerText = aiData.learning_speed;
    document.getElementById("r_format").innerText = aiData.preferred_format;

    function fillList(id, data){
        const ul = document.getElementById(id);
        ul.innerHTML = "";
        data.forEach(item=>{
            const li = document.createElement("li");
            li.innerText = item;
            ul.appendChild(li);
        });
    }

    fillList("what_list", aiData.what_to_learn);
    fillList("how_list", aiData.how_to_learn);
    fillList("daily_list", aiData.daily_plan);
    fillList("resource_list", aiData.resources);
    fillList("video_list", aiData.videos);
    fillList("practice_list", aiData.practice);

});

function goToProgress(){
    window.location.href = "progress.html";
}
</script>

</body>
</html>