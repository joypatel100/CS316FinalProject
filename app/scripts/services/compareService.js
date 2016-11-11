'use strict';

angular
        .module('projectApp')
        .factory('CompareService',['$http', '$q', function CompareService($http, $q) {
                var service = {};

                // 
                service.getBasic = function(speeches) {
                        var deferred = $q.defer();
                        console.log(speeches);
                        $http.get('/database/rest_models/speechassociation', {'speech_id1': speeches.first, 'speech_id2': speeches.second}).success(function(data){
                                deferred.resolve(data);
                                console.log(data);
                        }).error(function(data, status, headers, config){
                                deferred.reject({"data": data, "status": status, "headers": headers, "config": config});
                        });

                        // deferred.resolve({'success': true, 'data': {'speech1': '1', 'speaker1': 'josh', 'speech2': '2', 'speaker2': 'sarah', 'association': 0.5}});
                        return deferred.promise;
                };

                return service;


        }]);

