define(function(require) {
    'use strict';

    var angular = require("angular"),
        angularroute = require('angular-route'),
        angularAMD = require('angularAMD'),
        djangular = require('djangular'),
        controllers = require("controllers"),
        directives = require("directives"),
        services = require("services");
    var app = angular.module('library', [
            'ngRoute',
            controllers.name,
            services.name,
            directives.name,
        ])
        .config(['$routeProvider', '$interpolateProvider', '$httpProvider',
            function($routeProvider, $interpolateProvider, $httpProvider) {
                $interpolateProvider.startSymbol('{$');
                $interpolateProvider.endSymbol('$}');
                var token = $('input[name=csrfmiddlewaretoken]').val();
                $httpProvider.defaults.headers.post['X-CSRFToken'] = token;
                $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
                $routeProvider
                    .when('/', {
                        templateUrl: '/static/angular/library/views/library.html',
                        controller: 'LibraryController',
                    })
                    .otherwise({
                        redirectTo: '/'
                    })

            }
        ]);


    return angularAMD.bootstrap(app);
});