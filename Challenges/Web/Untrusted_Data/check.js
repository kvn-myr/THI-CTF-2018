// Check.js checks if an alert occured
//
//
//
// Get page
var system = require('system');
var page_in = system.stdin.readLine();

// Create webpage
var webPage = require('webpage');
var page = webPage.create();

// onAlert
page.onAlert = function(msg) {
  system.stdout.writeLine(msg);
};

// Open page
page.open(page_in, function(status) {
 });
