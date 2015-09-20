'use strict';

/**
 * @ngdoc overview
 * @name p2pApp
 * @description
 * # p2pApp
 *
 * Main module of the application.
 */
angular
  .module('p2pApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'parse-angular',
    'parse-angular.enhance'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/borrow', {
        templateUrl: 'views/borrow.html',
        controller: 'BorrowCtrl',
        controllerAs: 'borrow'
      })
      .when('/itemList', {
        templateUrl: 'views/itemList.html',
        controller: 'ItemCtrl',
        controllerAs: 'item'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .run(function() {
      Parse.initialize("pQGBjh7rGMjfOYN2Fp1JEJDhRgeFlrGMw1xd8Ri4", "TlLtRHz7UWIU0Ne6J2IJ9xaMd2QAsPuqzfGBMjjA");
  });
