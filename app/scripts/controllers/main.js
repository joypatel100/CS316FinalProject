'use strict';

/**
 * @ngdoc function
 * @name projectApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the projectApp
 */
angular.module('projectApp')
  .controller('MainCtrl', ['$scope', 'DBService', function($scope, DBService) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    var self = this;
    self.showSearch = false;
    self.noParams = false;

    self.search = function() {
      self.test = {};
      // just for testing purposes
      self.searchResults = [{
        'id': 1,
        'speaker': 'me',
        'keywords': 'blah',
        'date': 'now',
        'party': 'repub'
      }, {
        'id': 2,
        'speaker': 'me',
        'keywords': 'blah',
        'date': 'today',
        'party': 'dem'
      }]

      self.displayResults(self.searchResults);
      // end testing block
      if (!self.query || ((!self.query.speaker) && (!self.query.keywords) && (!self.query.date) && (!self.query.id))) {
        self.noParams = true;
      } else {
        if (self.query.keywords) { // take out commas
          self.query.keywords = self.query.keywords.replace(/,/g, '');
        }
        console.log(self.query);
        DBService.getSearchResults(self.query).then(function(promise) {
          self.showSearch = true;
          console.log(promise);
          self.displayResults(promise.data);
        });
      }
    };

    // "Basic" analytics -- displays the plain text comparison score

    self.displayResults = function(data) {
      self.noParams = false;
      self.searchResults = data;
      self.showSearch = true;
      //console.log(self.searchResults);
    };

  }]);
