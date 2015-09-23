'use strict';

/**
 * @ngdoc function
 * @name p2pApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the p2pApp
 */
angular.module('p2pApp')
  .controller('MainCtrl', function ($scope, $location) {
  	$scope.regUser = {};
    $scope.loginUser = {};
  	$scope.regBtnClick = function() {
  		Parse.User.signUp($scope.regUser.username, $scope.regUser.password);
      $scope.regUser = {};
    };

    $scope.regLoginClick = function() {
      Parse.User.logIn($scope.loginUser.username, $scope.loginUser.password);
      $scope.loginUser = {};
      $location.path('/borrow_lend');
      console.log(Parse.User.current().getSessionToken());
    };
  });
