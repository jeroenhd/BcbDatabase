/**
 * Handle dropdown selection from the nav bar
 */

$(document).ready(function () {
    /* This part of the website only works if the user has enabled javascript.
     * To accommodate for users without Javascript, this element is invisible by default and made visible using JS
     */
    var select =$('#select_chapter');
    select.css('visibility','visible');
    select.change(function (event) {
       var newChapter = select.val();
       window.location.href = '/c' + newChapter;
    });
});