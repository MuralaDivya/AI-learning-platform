let currentQuestions = [];

function startAssessment() {
    const studentClass = document.getElementById("class").value;
    const subject = document.getElementById("subject").value;

    fetch("http://127.0.0.1:5000/ai/get_exam", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            class: studentClass,
            subject: subject
        })
    })
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("questionBox");
        container.innerHTML = "";
        currentQuestions = data.questions;

        data.questions.forEach((q, index) => {
            const div = document.createElement("div");
            div.className = "question";

            div.innerHTML = `
                <p><b>Q${index + 1}.</b> ${q.q}</p>
                <input type="text" id="ans_${index}" placeholder="Your answer" />
            `;

            container.appendChild(div);
        });
    })
    .catch(err => {
        alert("Server error: " + err);
    });
}

function submitAssessment() {
    let answers = [];

    currentQuestions.forEach((q, index) => {
        const userAns = document.getElementById(`ans_${index}`).value;
        answers.push({
            question: q.q,
            correct: q.a,
            user: userAns,
            topic: q.topic
        });
    });

    fetch("http://127.0.0.1:5000/ai/submit_exam", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            answers: answers
        })
    })
    .then(res => res.json())
    .then(result => {
        localStorage.setItem("assessment_result", JSON.stringify(result));
        window.location.href = "recommendations.html";
    })
    .catch(err => {
        alert("Submit Error: " + err);
    });
}