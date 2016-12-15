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
                self.isDefault = function(name) {
                        return (name === self.options[0].name);
                }
                // Gonna hardcode the names and descriptions
                // this is not good coding practice, sorry!
                self.options = [ 
                        {'name': 'Keywords', 'description' : 'Take a look at some of the most frequently used keywords in congressional speeches. You can filter the speeches by member of Congress, by date, or by party. The visualization also shows the average sentiment of the speeches you’ve selected.'},
                        {'name': 'Word Counts', 'description' : 'See how much different members of Congress talk. This visualization shows the total word count of all speeches by party, as well as the number of speeches of different lengths. You can filter by member of Congress and by date.'}, 
                        {'name': 'Network', 'description' : 'Explore a network of each member’s longest speeches. Members connected with an edge have some similarity between their longest speeches, and the closer two members are together, the more similar their longest speeches are.'},
                        {'name': 'Timeline', 'description' : 'Congress has talked more or less over time. Take a look at the distribution of Congressional speeches over time from January 2015 until September 2016.'}
                ];
        }]);
