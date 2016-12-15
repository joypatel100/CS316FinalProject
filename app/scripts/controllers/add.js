'use strict';

/**
 * @ngdoc function
 * @name projectApp.controller:AddCtrl
 * @description
 * # AddCtrl
 * Controller of the projectApp
 */
angular.module('projectApp')
  .controller('AddCtrl', ['$scope', 'DBService', '$routeParams', function($scope, DBService, $routeParams) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    var self = this;
    self.addButton = true;
    self.addSpeech = function() {
      // just for testing
      self.successMessage();
      //
      DBService.addSpeech(self.speech).then(function(promise) {
        console.log(promise);
        self.successMessage();
      });
    }

    self.successMessage = function() {
      console.log(self.speech);
      self.displaySuccessMessage = true;
      self.addButton = false;
    };

    self.reset = function() {
      self.displaySuccessMessage = false;
      console.log(self.speech);
      self.speech = {};
      self.addButton = true;
      //$scope.speechForm.$setPristine();
      //$scope.speechForm.$setUntouched();
    }

  }]);
