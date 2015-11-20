define(function  (require) {
   'use strict';

   var angular = require('angular');

   return angular.module('discussions.directives', [])
        .directive('resources',function  () {
            return {
                restrict: 'E',
                 templateUrl: function(elem,attrs) {
                   return '/static/angular/discussions/partialviews/resources.html';
                },
                controller: 'ResourcesViewController',
            }
        })
        .directive('content',function  () {
            return {
                restrict: 'E',
                 templateUrl: function(elem,attrs) {
                   return '/static/angular/discussions/partialviews/content.html';
                },
                controller: 'ContentViewController',
            }
        })

});