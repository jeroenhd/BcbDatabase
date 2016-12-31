/**
 * An API object for communicating over JSON
 */


var Server = function (chapter, page) {
    this.chapterNumber = chapter;
    this.pageNumber = page;
};

Server.VERSION = 'v1.0';

/**
 * Get the lines belonging to a page
 */
Server.prototype.getLines= function () {
    
};

/**
 * Change the order of a line
 * @param lineId The ID of the line
 * @param difference The difference (+1/-1)
 */
Server.prototype.changeOrder = function (lineId, difference) {

};

/**
 * Get a list of characters
 */
Server.prototype.getCharacters = function () {

};

/**
 * Change a line
 * @param lineId The line ID
 * @param character The character ID
 * @param line The contents of the line
 */
Server.prototype.changeLine = function (lineId, character, line) {

};

/**
 * Delete a line
 * @param lineId int The ID of the line to delete
 * @param cleanup function The function to call after success
 */
Server.prototype.deleteLine = function (lineId, cleanup) {
    var postUrl = '/api/' + Server.VERSION + '/lines/delete/'+ lineId + '/';

    $.ajax({
        url: postUrl,
        success: function (data, textStatus, jqXHR) {
            if (data.Result === 'Fail')
            {
                console.error('Failed to delete line ' + lineId + ': ' + data.reason);
            } else {
                if (undefined != cleanup)
                {
                    cleanup();
                }
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {

        }
    });
};

/**
 * Add a new line
 * @param character The character speaking the line
 * @param line The text of the line itself
 * @param cleanup function The function to call afterward to clean up
 */
Server.prototype.addLine = function (character, line, cleanup) {
    var postUrl = '/api/' + Server.VERSION + '/lines/' + this.chapterNumber + '/' + this.pageNumber + '/new/' + character.id + '/' + encodeURIComponent(line) + '/';
    $.ajax({
        url: postUrl,
        success: function (data, textStatus, jqXHR) {
            if (undefined != cleanup)
            {
                cleanup(data);
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert(errorThrown);
        }
    });
};
