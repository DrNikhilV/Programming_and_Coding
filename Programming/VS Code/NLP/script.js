let playerName;
let questions;
let currentQuestionIndex = 0;
let score = 0;

function startGame() {
    playerName = document.getElementById("playerName").value;
    if (!playerName) {
        alert("Please enter your name!");
        return;
    }

    // Load questions from external file (questions.js)
    loadQuestions();

    // Display the first question
    showQuestion();
}

function loadQuestions() {
    // Assuming questions.js contains an array of question objects
    // You can structure your questions in a way that suits your needs
    // Example: questions = [...];
    questions = [
        {
            "Course": "Principles of Chemical Science",
            "Topic": "The photoelectric effect",
            "Original question": "A beam of light with an intensity of 15 W is incident on a copper plate (\u03c6 = 7.43 x 10-19 J). Electrons with a minimum wavelength of 3.75 x 10-10 m are ejected from the surface of the copper. Calculate the frequency of the incident light.",
            "Solution": "7.43 * 10^-19 J"
        },
        {
            "Course": "Principles of Chemical Science",
            "Topic": "The photoelectric effect",
            "Original question": "A beam of light with an intensity of 15 W is incident on a copper plate (\u03c6 = 7.43 x 10-19 J). Electrons with a minimum wavelength of 3.75 x 10-10 m are ejected from the surface of the copper. Calculate the maximum number of electrons that can be ejected by a 3.0-second pulse of\nthe incident light. ",
            "Solution": "1.8 * 10^19 electrons"
        },
        // Add more questions as needed
    ];
}    

function showQuestion() {
    if (currentQuestionIndex < questions.length) {
        const currentQuestion = questions[currentQuestionIndex];

        const quizContainer = document.getElementById("quiz-container");
        quizContainer.innerHTML = `
            <h1>${currentQuestion["Course"]}</h1>
            <h2>${currentQuestion["Topic"]}</h2>
            <p>${currentQuestion["Original question"]}</p>
            <label for="userAnswer">Your Answer:</label>
            <input type="text" id="userAnswer">
            <button onclick="checkAnswer()">Submit Answer</button>
            <button onclick="exitGame()">Exit Game</button>
        `;
    } else {
        endGame();
    }
}

function checkAnswer() {
    const userAnswer = document.getElementById("userAnswer").value;
    const currentQuestion = questions[currentQuestionIndex];

    if (userAnswer.toLowerCase() === currentQuestion["Solution"].toLowerCase()) {
        score += 1;
        alert("Correct! +1 point");
    } else {
        score -= 0.25;
        alert("Incorrect! -0.25 points");
    }

    currentQuestionIndex += 1;
    showQuestion();
}

function exitGame() {
    const quizContainer = document.getElementById("quiz-container");
    quizContainer.innerHTML = `
        <h1>Game Over, ${playerName}!</h1>
        <p>Your final score: ${score.toFixed(2)}</p>
        <p>Thanks for playing!</p>
    `;
}
