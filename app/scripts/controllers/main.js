'use strict';

/**
 * @ngdoc function
 * @name projectApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the projectApp
 */
angular.module('projectApp')
  .controller('MainCtrl', [ '$scope', 'CompareService', function ($scope, CompareService) {
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
                if ($scope.speeches.analytics === 'Basic') {
                        CompareService.getBasic($scope.speeches).then(function(data){
                                if (data.success) {
                                        self.displayBasic(data.data);
                                } else {
                                        // @TODO
                                }                    
                        });
                } 
        };

        // "Basic" analytics -- displays the plain text comparison score
        self.displayBasic = function(data) {
                self.speech1 = data.speech1;
                self.speaker1 = data.speaker1;
                self.speech2 = data.speech2;
                self.speaker2 = data.speaker2;
                self.association = data.association;
                self.showBasic = true;
                console.log($scope.basic);
        };


  }]);
