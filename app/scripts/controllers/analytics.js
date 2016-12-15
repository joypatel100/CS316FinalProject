'use strict';

/**
 * @ngdoc function
 * @name projectApp.controller:AnalyticsCtrl
 * @description
 * # AnalyticsCtrl
 * Controller of the projectApp
 */
angular.module('projectApp')
        .controller('AnalyticsCtrl', ['$scope', 'DBService', function($scope, DBService) {
                this.awesomeThings = [
                        'HTML5 Boilerplate',
                        'AngularJS',
                        'Karma'
                ];
                var self = this;
                // Gonna hardcode the names and descriptions
                // this is not good coding practice, sorry!
                self.options = [ 
                                 {'name': 'one', 'description' : 'hi'},
                                 {'name': 'two', 'description' : 'hi'}, 
                                 {'name': 'three', 'description' : 'hi'}
                ]
        }]);
