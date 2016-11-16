'use strict';

angular.module('projectApp')
  .controller('SignInCtrl', ['$scope', 'DBService', function($scope, DBService) {
    $scope.signin = {
      username: '',
      password: ''
    };

    $scope.signinClick = function() {
      DBService.checkPassword({
        username: $scope.signin.username,
        password: $scope.signin.password
      }).then(function(promise) {
        console.log(promise);
      });
    };
  }]);
