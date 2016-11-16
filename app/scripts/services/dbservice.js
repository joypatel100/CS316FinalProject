'use strict';

angular.module('projectApp')
  .factory('DBService', ['$http', '$q', 'Config',
    function DBService($http, $q, Config) {
      var service = {};

      service.checkPassword = function(input) {
        console.log(input);
        var deferred = $q.defer();
        $http({
          method: 'GET',
          url: Config.baseUrl + 'users?' +
            'username=' + input.username
        }).then(function successCallback(response) {
          console.log(response);
          console.log(md5(input.password));
          if (response.data.data.length === 0) {
            console.log("error");
          } else {
            console.log(md5(input.password));
            deferred.resolve({
              check: response.data.data[0].password === md5(input.password)
            });
          }
        }, function errorCallback(response) {
          deferred.reject();
          console.log(response);
        });

        return deferred.promise;
      };

      service.getSpeechAssociation = function(speeches) {
        var deferred = $q.defer();

        $http({
          method: 'GET',
          url: Config.baseUrl + 'speechassociation?' +
            'speech_id1=' + speeches.first + '&' +
            'speech_id2=' + speeches.second
        }).then(function successCallback(response) {
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

      service.postUsers = function(user) {
        var deferred = $q.defer();

        $http({
          method: 'POST',
          url: Config.baseUrl + 'users',
          headers: {
            'Content-Type': 'application/json'
          },
          data: {
            username: user.username,
            password: user.password
          }
        }).then(function successCallback(response) {
          console.log(response);
        }, function errorCallback(response) {
          console.log(response);
        });
      };

      return service;
    }
  ]);
