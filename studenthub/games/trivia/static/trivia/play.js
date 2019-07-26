/**
 * Supplemental script to provide prototypes for Questions and functions to
 * dynamically update page content based on Question data
 */

const OPTION = 'question-option-'; // option id string - append `<q#>-<opt#>`
const ANSWER = 'answer-'; // name for selected answer - append `<q#>`
const QUESTION = 'question-'; // name for Question element - append `<q#>`
const QUESTION_CLASS = 'question'; // class assigned to each Question div
const OPTION_CLASS = 'option'; // class assigned to each answer option div tag
const QUESTION_TYPE = 'q-type-'; // name for hidden field qType value

class Question {
    // TODO: Implement a function to decode special characters encoded
    //  as &quot; and others. Evaluating security risk from xss code injection
    //  attacks
    constructor(text, options) {
        this.text = text;
        this.options = options;
    }

    /**
     * Adds the Question object with text and options to a div tag, immediately
     * following the the element with the passed id value
     * @param id of object to insert question after
     * @param questionNo of question - used to generate unique id
     * @return id of generated question block div tag
     */
    addQuestion(id, questionNo) {
        // TODO: break this up into a series of helper methods
        // Create a new element - class=<QUESTION_CLASS>
        var questionElement = document.createElement("div");
        questionElement.setAttribute("class", QUESTION_CLASS);
        questionElement.setAttribute("id", QUESTION + questionNo);
        questionElement.setAttribute("style", 'text-align:left');

        // Add text to questionElement
        var textContent = document.createTextNode(this.text);
        questionElement.appendChild(textContent);

        // line break
        var newline = document.createElement("br");
        questionElement.appendChild(newline);

        // Create hidden field for question value
        var hiddenQuestionText = document.createElement("input");
        hiddenQuestionText.setAttribute("type", "hidden");
        hiddenQuestionText.setAttribute("name", QUESTION + questionNo);
        hiddenQuestionText.setAttribute("value", this.text);
        questionElement.appendChild(hiddenQuestionText);

        // Add radio buttons
        for (var i = 0; i < this.options.length; i++) {
            // Create radio buttons
            var choice = document.createElement("INPUT");
            choice.setAttribute("type", "radio");
            choice.setAttribute("name", ANSWER + questionNo);
            choice.setAttribute("value", this.options[i]);
            choice.setAttribute("id", OPTION + questionNo + '-' + i);

            // add buttons to parent element
            questionElement.appendChild(choice);

            // TODO: Refactor to protect against xss code injection
            // Create choice label
            var choiceLabel = document.createElement("LABEL");
            choiceLabel.setAttribute("for", choice.getAttribute("id"));
            var labelText = document.createTextNode(this.options[i]);
            choiceLabel.appendChild(labelText);

            // Add choice label
            questionElement.appendChild(choiceLabel);

            // Line break
            questionElement.appendChild(document.createElement("br"));
        }

        // Insert question element after page element with passed id
        //var pageElement = document.getElementById(id);
        // Second or later question in block
        //if (questionNo > 0) {
        //    pageElement.insertBefore(questionElement, pageElement);
        //}
        // First question in block
        //else {
        //    pageElement.appendChild(questionElement);
        //}
        var pageElement = document.getElementById(id);
        pageElement.appendChild(questionElement);


        // Final line break
        //questionElement.insertBefore(document.createElement("br"), questionElement.nextSibling);
        pageElement.appendChild(document.createElement("br"));
        // Return id
        return questionElement.getAttribute("id");
    }
}


/**
 * Prototype extends Question data modeling and behavior
 */
class TypedQuestion extends Question {
    constructor(text, options, qType) {
        super(text, options);
        this.qType = qType;
    }

    /**
     * Overrides the parent prototype function. Adds an additional hidden field for
     * question type when the form POSTs
     * @param id of question element created by parent
     * @param questionNo of the question
     * @returns {id} of the question element created by the overriden function
     */
    addQuestion(id, questionNo) {
        var questionID = super.addQuestion(id, questionNo);
        // Add a hidden input field to
        var hiddenTypeField = document.createElement("input");
        hiddenTypeField.setAttribute("type", "hidden");
        hiddenTypeField.setAttribute("name", QUESTION_TYPE + questionNo);
        hiddenTypeField.setAttribute("value", this.qType);

        // Add it to question page element
        var questionElement = document.getElementById(questionID);
        questionElement.appendChild(hiddenTypeField);

        // return the question element id
        return questionID;
    }

    getType() {
        return this.qType;
    }
}







