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
    self.showBasic = false;

    // options for the types of analytics offered
    self.analytics = ['Basic'];

    // take the form data and create an API request
    self.submit = function() {
      self.speech1 = $scope.speeches.first;
      self.speech2 = $scope.speeches.second;

      if ($scope.speeches.analytics === 'Basic') {
        DBService.getBasic($scope.speeches).then(function(promise) {
          console.log(promise);
          self.displayBasic(promise.data);
        });
      }
    };

    // "Basic" analytics -- displays the plain text comparison score
    self.displayBasic = function(data) {
      self.score = data.score;
      self.showBasic = true;
      console.log($scope.basic);
    };


  }]);
