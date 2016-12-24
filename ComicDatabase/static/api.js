/**
 * An API object for communicating over JSON
 */


var Server = function () {};

/**
 * Get the lines belonging to a page
 * @param chapter The chapter number
 * @param page The page number
 */
Server.prototype.getLines= function (chapter, page) {
    
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
 * @param lineId The ID of the line to delete
 */
Server.prototype.deleteLine = function (lineId) {

};

/**
 * Add a new line
 * @param chapter The chapter to add to
 * @param page The page to add to
 * @param character The character speaking the line
 * @param order The order number
 * @param line The text of the line itself
 */
Server.prototype.addLine = function (chapter, page, character, order, line) {
    $.ajax({
        url: '/api/v1.0/' + chapter + '/' + page + '/new/' + character.id + '/' + order + '/' + encodeURIComponent(line) + '/',
        success: function (data, textStatus, jqXHR) {
            alert('Hurray: ' + data);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert(errorThrown);
        }
    });
};
