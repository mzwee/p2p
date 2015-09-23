'use strict';

/**
 * @ngdoc function
 * @name p2pApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the p2pApp
 */
angular.module('p2pApp')
  .controller('BorrowUploadCtrl', function ($scope, $http) {
  	$scope.temp = {};

  	$scope.requestBtnClick = function() {
      console.log(Parse.User.current().attributes.username);
  		$http({
        method:"POST",
        url:"https://api.parse.com/1/classes/Items", 
        dataType: "jsonp",
        headers:{
          "X-Parse-Application-Id":"pQGBjh7rGMjfOYN2Fp1JEJDhRgeFlrGMw1xd8Ri4",
          "X-Parse-REST-API-Key":"gAHOAADdijF0JbaNPp9yw82Y8wQIYqpZZKcjJxIQ"},
        data:{"ItemName": $scope.temp.ItemName, "Brand": $scope.temp.Brand, "Category": $scope.temp.Category, requester: Parse.User.current().attributes.username}})
          .success(function(data, status) {
            console.log(data);
          })
          .error(function(error) {
            console.log(error);
          });
  	};
  });
