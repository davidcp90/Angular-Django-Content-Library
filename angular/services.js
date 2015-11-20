define(function(require) {
    'use strict';

    return angular.module('library.services', [])
        .factory('LibraryService', ['$http', '$q',
            function($http, $q) {
                function mark_resource(id) {
                    var deferred = $q.defer();
                    $http({
                        method: 'POST',
                        url: '/cursos/mark_resource',
                        params:{
                            resource: id,
                        }
                    }).success(function(data) {
                        deferred.resolve(data);
                    });
                    return deferred.promise;
                }
                return {
                    mark_resource: mark_resource,
                }
            }

        ])
});