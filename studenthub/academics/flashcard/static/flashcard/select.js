/**
 * Updates modules drop down with valid values.
 */
function updateModules() {
    // remove invalid options
    clearDropDown(moduleDropdown);

    let subject = subjectDropdown.options[subjectDropdown.selectedIndex].value;
    let course = courseDropdown.options[courseDropdown.selectedIndex].value;

    // populate subject list
    let subjectList = [];
    // Filter - all subject
    if (subject == SELECT_TEXT) {
        subjectList = Object.keys(flashcardCat);
    }
    // Filter - singleton subject
    else {
        subjectList.push(subject)
    }

    // populate course list
    let courseList = [];

    // Filter - All courses and their module "children"
    if (course == SELECT_TEXT) {
        // populate course list
        subjectList.forEach(function(subjectKey) {
            let courses = Object.keys(flashcardCat[subjectKey]);
            courseList = courseList.concat(courses);
        });
    }
    // Filter - one course and it's children modules
    else {
        // populate singleton course
        courseList.push(course);
    }

    // populate module drop down
    // iteratively collect all modules "in" selected subset
    let moduleList = [SELECT_TEXT];
    subjectList.forEach(function(subjectKey) {
        courseList.forEach(function(courseKey) {
            // iterate through all modules
            // course "in" subject superset
            if (Object.keys(flashcardCat[subjectKey]).includes(courseKey)) {
                flashcardCat[subjectKey][courseKey].forEach(function (moduleLeaf) {
                    moduleList.push(moduleLeaf)
                });
            }
        });
    });
    // populate module drop down
    populateSelectElement('mod-select', moduleList);
}


/**
 * Updates both course and module drop downs with valid values.
 */
function updateCoursesModules() {
    // remove invalid options
    clearDropDown(courseDropdown);
    clearDropDown(moduleDropdown);

    var subject = subjectDropdown.options[subjectDropdown.selectedIndex].value;
    // Filter - All subjects and their children classifications
    if (subject == SELECT_TEXT) {
        // populate all 2 "sub" menus with default values
        populateSelectElement('course-select', flashcardScheme.course);
        populateSelectElement('mod-select', flashcardScheme.module);
    }
    // Filter - One subject and its children classifications
    else {
        // populate course drop down
        let courseList = Object.keys(flashcardCat[subject]);
        courseList.unshift(SELECT_TEXT);
        populateSelectElement('course-select', courseList);

        // iteratively collect all modules "in" selected subset
        let moduleList = [SELECT_TEXT];
        courseList.shift(); // consume 'SELECT' element
        courseList.forEach(function(courseKey) {
            // iterate through all modules
            flashcardCat[subject][courseKey].forEach(function(moduleLeaf) {
                moduleList.push(moduleLeaf)
            });
        });
        // populate module drop down
        populateSelectElement('mod-select', moduleList);
    }
}



/**
 * Helper function to clear a drop down menu
 * @param dropDown dom select menu to clear
 */
function clearDropDown(dropDown) {
    // remove previous flashcard if any
    while (dropDown.firstChild) {
        dropDown.removeChild(dropDown.firstChild);
    }
}