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
      .when('/borrow_lend', {
        templateUrl: 'views/borrow_lend.html',
        controller: 'BLCtrl',
        controllerAs: 'bl'
      })
      .when('/lend_item', {
        templateUrl: 'views/lend_item.html',
        controller: 'LendItemCtrl',
        controllerAs: 'lend_item'
      })
      .when('/borrow_upload', {
        templateUrl: 'views/borrow_upload.html',
        controller: 'BorrowUploadCtrl',
        controllerAs: 'borrow-upload'
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
