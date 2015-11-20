require.config({
  baseUrl:'./',
  waitSeconds: 200,
  paths:{
  'jquery':'../../components/jquery/jquery',
  'angular':'../../components/angular/angular',
  'angularAMD':'../../components/angularAMD/angularAMD',
  'app': '../../angular/library/app',
  'controllers': '../../angular/library/controllers',
  'services': '../../angular/library/services',
  'directives': '../../angular/library/directives',
  'init_dom': '../../angular/library/init_dom',
  'djangular': '../../djangular/js/django-angular',
  'angular-route': '../../components/angular-route/angular-route',
},
shim:{
  'jquery':{
    exports:'jQuery'
  },
  'init_dom':['jquery'],
  'angular': {
            exports: 'angular',
  },
  'angularAMD':['angular'],
  'controllers': ['angular'],
  'services': ['angular'],
  'djangular':['angular'],
  'directives':['angular'],
  'angular-route':['angular'],
  'app':['controllers', 'services', 'directives','angular'],
},
deps:['app','jquery','init_dom']
});
