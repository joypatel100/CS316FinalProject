'use strict';

angular.module('projectApp')
  .controller('RegisterCtrl', function($scope) {
    $scope.register = {
      username: '',
      password: ''
    };

    $scope.registerClick = function() {
      console.log($scope.register.username);
    };
  });
