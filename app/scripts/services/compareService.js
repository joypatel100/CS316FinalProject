'use strict';

angular
        .module('projectApp')
        .factory('CompareService',['$http', '$q', function CompareService($http, $q) {
                var service = {};

                // 
                service.getBasic = function(speeches) {
                        var deferred = $q.defer();
                        deferred.resolve({'success': true, 'data': {'speech1': '1', 'speaker1': 'josh', 'speech2': '2', 'speaker2': 'sarah', 'association': 0.5}});
                        return deferred.promise;
                };

                return service;


        }]);

