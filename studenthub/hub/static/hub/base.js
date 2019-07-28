/**
 * Function populates a <select> page text with <options>
 * @param id - page text id
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

/**
 * Adds a tabled leaderboard to table in page based on a table id and a list
 * of json-objects defining the contents of the leaderboard
 * @param topScores a list of json-objects representing table data
 * @param tableID target table element id
 */
function addLeaderboard(topScores, tableID) {
    var table = document.getElementById(tableID)
    // Get keys for json objects
    keyList = Object.keys(topScores[0]);

    // Create Table Header
    var header = document.createElement("thead");
    // Iterate down each row
    for (var i = 0; i < topScores.length; i++) {
        // Create new row
        var newRow = document.createElement("tr");

        // Add attributes for new row
        var rowID = 'row-' + i;
        newRow.setAttribute("id", rowID);

        // populate row - iterate across columns
        for (var j = 0; j < keyList.length; j++) {
            // create text node
            var text = document.createTextNode(topScores[i][keyList[j]]);

            // Add text to table text
            // Second or later row
            var newCol;
            if (i) {
                newCol = document.createElement("td");
            }
            // 1st Row
            else {
                newCol = document.createElement("th");
            }

            // Center text
            newCol.setAttribute("style", "text-align:center; border:1px solid");

            newCol.appendChild(text); // Add text to column text
            // add col text to row
            newRow.appendChild(newCol);
        }

        // Add row to table
        // Second or later row
        if (i) {
            table.appendChild(newRow);
        }
        // First row - table headings
        else {
            header.appendChild(newRow);
            table.appendChild(header);
        }
    }
}