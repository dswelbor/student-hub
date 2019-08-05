const CORRECT_ID = "correct-text";
const OUT_OF_ID = "total-text";
const SCORE_ID = 'score-text';
const LEADERBOARD_ID = 'leaderboard';

/**
 * Function dynamically populates data from correct, total questions, and weighted
 * score values.
 * @param correct - number of correct answers
 * @param total - numbers of trivia questions in pool
 * @param score - weighted score based on number of questions and difficulty
 */
function addResults(correct, total, score) {
    // dynamically add value for correct answers
    var correctElement = document.createElement("div");
    correctElement.setAttribute("style", "display:inline-block");
    var correctText = document.createTextNode(correct);
    correctElement.appendChild(correctText);
    // correctElement.appendChild(document.createElement("br")); // newline

    // Add correct text to page
    var correctLabel = document.getElementById(CORRECT_ID);
    correctLabel.appendChild(correctElement);
    correctLabel.appendChild(document.createElement("br")); // newline

    // dynamically add value for total # of questions
    var totalElement = document.createElement("div");
    totalElement.setAttribute("style", "display:inline-block");
    var totalText = document.createTextNode(total);
    totalElement.appendChild(totalText);
    // totalElement.appendChild(document.createElement("br")); // newline

    // Add correct text to page
    var totalLabel = document.getElementById(OUT_OF_ID);
    totalLabel.appendChild(totalElement);
    totalLabel.appendChild(document.createElement("br")); // newline

    // dynamically add value for Weighted Score
    var scoreElement = document.createElement("div");
    scoreElement.setAttribute("style", "display:inline-block");
    var scoreText = document.createTextNode(score);
    scoreElement.appendChild(scoreText);
    // scoreElement.appendChild(document.createElement("br")); // newline

    // Add correct text to page
    var scoreLabel = document.getElementById(SCORE_ID);
    scoreLabel.appendChild(scoreElement);
    scoreLabel.appendChild(document.createElement("br")); // newline

    // TODO: Add Ranking
}