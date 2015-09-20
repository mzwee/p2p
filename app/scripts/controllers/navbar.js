'use strict';

/**
 * @ngdoc function
 * @name p2pApp.controller:NavCtrl
 * @description
 * # NavCtrl
 * Controller of the p2pApp
 */
angular.module('p2pApp')
  .controller('NavCtrl', function ($scope) {    
    $scope.isSignedIn = function() {
      if(Parse.User.current()) {
        $scope.username = Parse.User.current().getUsername();
        return true;
      }
      return false;
    }
    $scope.logoutBtnClick = function() {
      Parse.User.logOut();
    };
  });
