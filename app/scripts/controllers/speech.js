'use strict';

/**
 * @ngdoc function
 * @name projectApp.controller:SpeechCtrl
 * @description
 * # SpeechCtrl
 * Controller of the projectApp
 */
angular.module('projectApp')
        .controller('SpeechCtrl', ['$scope', 'DBService', '$routeParams', function($scope, DBService, $routeParams) {
                this.awesomeThings = [
                        'HTML5 Boilerplate',
                        'AngularJS',
                        'Karma'
                ];
                var self = this;
                // just for testing purposes
                self.data = {'speaker': 'donald', 'party': 'Republican', 'date': 'Today', 'text': 'hi there!', 'speechid': '1', 'keywords': 'orange apple', 'sentiment': '1'};
                DBService.getSpeech($routeParams.id).then(function(promise) {
                        console.log(promise);
                        self.data = promise.data;
                });


        }]);
