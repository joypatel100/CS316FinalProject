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
                // just for testing purposes
                self.addSpeech = function() {
                        self.data = {'speaker': 'donald', 'party': 'Republican', 'date': 'Today', 'text': 'hi there!', 'speechid': '1'};
                        self.successMessage();
                        DBService.addSpeech(self.data).then(function(promise) {
                                console.log(promise);
                                self.successMessage();
                        });
                }

                self.successMessage = function() {
                        self.displaySuccessMessage = true; 
                };

                self.reset = function() {
                        self.displaySuccessMessage = false;
                        console.log($scope.speechForm);
                        $scope.speech = {};
                        //$scope.speechForm.$setPristine();
                        //$scope.speechForm.$setUntouched();
                }

        }]);
