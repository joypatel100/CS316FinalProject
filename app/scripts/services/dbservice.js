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

      //@TODO given a speech's id, retrive the speaker, id, date, speaker's party, keywords, sentiment score, and content
      service.getSpeech = function(id) {
        var deferred = $q.defer();

        $http({ 
          method: 'GET',
          url: Config.baseUrl + 'info?' + 'speech_id=' + id 
        }).then(function successCallback(response) {
          console.log(response);
          deferred.resolve({
            data: response.data
          });
        }, function errorCallback(response) {
          deferred.reject();
          console.log(response);
        });
        return deferred.promise;
      };

      //@TODO query has speaker, keyword, party, speechid (optional)...return speeches filtered by these parameters
      service.getSearchResults = function(query) {
        var deferred = $q.defer();
        console.log(query);
        var params = '';
        if (query.speechid && query.speechid !== '') {
                params = 'speech_id=' + query.speechid;
        }
        else {
                if (query.speaker) params += 'speaker=' + query.speaker;
                if (query.speaker_party) {
                        if (params.length > 0) params+='&';
                        params += 'speaker_party=' + query.party;
                }
                if (query.keywords) {
                        if (params.length > 0) params+='&';
                        params += 'keywords=' + query.keywords;
                }
        }
        console.log(params);
        $http({ 
          method: 'GET',
          url: Config.baseUrl + 'search?' + params
        }).then(function successCallback(response) {
          console.log(response);
          deferred.resolve({
            data: response.data.data
          });
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
