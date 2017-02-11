/**
 * This uses Javascript to place email address links on the page.
 * This obfuscation is done to prevent spamming scrapers from adding email addresses to their spam lists.
 *
 * To use this script, just add <a> tags with class="mailto".
 */

// The email address to place in the anchor tags, but with @ replaced by $.
var email = 'bcb.transcription$jeroenhd.nl';
$(document).ready(function (event) {
    $(".mailto").prop("href", 'mailto:' + email.replace("$","@"));
});