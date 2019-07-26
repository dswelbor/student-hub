const CORRECT_ID = "correct-text";
const OUT_OF_ID = "total-text";
function addResults(correct, total) {
    // TODO: Add id's to correct and total value elements
    // dynamically add value for correct answers
    var correctElement = document.createElement("div");
    correctElement.setAttribute("style", "display:inline-block");
    var correctText = document.createTextNode(correct);
    correctElement.appendChild(correctText);
    // correctElement.appendChild(document.createElement("br")); // newline

    // Add correct element to page
    var correctLabel = document.getElementById(CORRECT_ID);
    correctLabel.appendChild(correctElement);
    correctLabel.appendChild(document.createElement("br")); // newline

    // dynamically add value for total # of questions
    var totalElement = document.createElement("div");
    totalElement.setAttribute("style", "display:inline-block");
    var totalText = document.createTextNode(total);
    totalElement.appendChild(totalText);
    // totalElement.appendChild(document.createElement("br")); // newline

    // Add correct element to page
    var totalLabel = document.getElementById(OUT_OF_ID);
    totalLabel.appendChild(totalElement);
    totalLabel.appendChild(document.createElement("br")); // newline
}