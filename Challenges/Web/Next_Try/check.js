// Check.js checks if an alert occured
//
//
//
// Get the page
var system = require('system');
var page_in = system.stdin.readLine();

// Create webpage
var webPage = require('webpage');
var page = webPage.create();

// Wait for alert
page.onAlert = function(msg) {
  system.stdout.writeLine(msg);
};

// Open page
page.open(page_in, function(status) {
 });
