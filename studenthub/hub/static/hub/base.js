/**
 * Function populates a <select> page element with <options>
 * @param id - page element id
 * @param elements - list of elements to add
 */
function populateSelectElement(id, elements) {
    var target = document.getElementById(id);

    // append elements to target
    for (var i = 0; i < elements.length; i++) {
        var option = document.createElement("option");
        option.value = elements[i];
        option.text = elements[i];
        target.add(option);
    }
}