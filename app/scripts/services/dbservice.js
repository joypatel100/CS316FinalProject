'use strict';

angular.module('projectApp')
  .factory('DBService',['$http', '$q', 'Config',
    function DBService($http, $q, Config) {
      var service = {};

                //
      service.getBasic = function(speeches) {
        var deferred = $q.defer();

        $http({
          method: 'GET',
          url: Config.baseUrl + 'speechassociation?' +
                'speech_id1=' + speeches.first + '&' +
                'speech_id2=' + speeches.second
        }).then(function successCallback(response){
          console.log(response);
          deferred.resolve({
            data: response.data.data[0]
          });
        }, function errorCallback(response) {
          deferred.reject();
          console.log(response);
        });
                          // deferred.resolve({'success': true, 'data': {'speech1': '1', 'speaker1': 'josh', 'speech2': '2', 'speaker2': 'sarah', 'association': 0.5}});
        return deferred.promise;
      };

      return service;
}]);
