'use strict';

/**
 * @ngdoc function
 * @name p2pApp.controller:ItemCtrl
 * @description
 * # ItemCtrl
 * Controller of the p2pApp
 */
angular.module('p2pApp')
  .controller('ItemCtrl', function ($scope, $http) {
    $scope.items = [];
  	$http({method:'GET',url:'https://api.parse.com/1/classes/Items', headers:{'X-Parse-Application-Id':'pQGBjh7rGMjfOYN2Fp1JEJDhRgeFlrGMw1xd8Ri4', 'X-Parse-REST-API-Key':'gAHOAADdijF0JbaNPp9yw82Y8wQIYqpZZKcjJxIQ'}})
      .success(function(data, status) {
        $scope.items = data.results;
        console.log(data);
      });

    $scope.helpBtnClick = function(item) {
      console.log(item.objectId);
      $http({
        method:'PUT',
        url:'https://api.parse.com/1/classes/Items/' + item.objectId,
        headers:{'X-Parse-Application-Id':'pQGBjh7rGMjfOYN2Fp1JEJDhRgeFlrGMw1xd8Ri4', 'X-Parse-REST-API-Key':'gAHOAADdijF0JbaNPp9yw82Y8wQIYqpZZKcjJxIQ'},
        data:{provider: Parse.User.current().attributes.username}
      })
      .success(function(data, status) {
        console.log(data);
      });
    }

  });
