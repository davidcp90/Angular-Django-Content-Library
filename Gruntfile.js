module.exports = function(grunt) {
    var matches = grunt.file.expand("./content/src/new_js/*.js");
    var requirejsOptions = {};
    if (matches.length > 0) {
        for (var x = 0; x < matches.length; x++) {
            grunt.log.write(x)
            var namefile = matches[x].replace('./content/src/new_js/', '');
            namefile = namefile.replace('.js','');
            requirejsOptions['task' + x ] = {
                                "options": {
                                    'appDir': 'content/src/new_js',
                                    'dir': 'content/build/new_js/' + namefile,
                                    'mainConfigFile': 'content/src/commons/' + namefile + '.js',
                                    'optimize': 'uglify2',
                                    uglify2: {
                                        options:{
                                            banner: '/*! <%= meta.project %> - v<%= meta.version %> - Copyright (c) Digital workers. Build Time: <%= grunt.template.today("dddd, mmmm dS, yyyy, h:MM:ss TT") %> */',
                                            mangle: false,
                                            compress: true
                                        },
                                    },
                                    'normalizeDirDefines': 'skip',
                                    'skipDirOptimize': true,
                                    'modules': [{
                                        'name': namefile,
                                        }
                                    ]
                                },
                        };
        }
        requirejsOptions['compile'] = {
                'options': {
                    'optimize': 'uglify2',
                    'baseUrl': 'content/src/js',
                    'dir': 'content/build/js',
                    'preserveLicenseComments': false,
                    "uglify2":{
                        "mangle": false,
                        "compress": true
                    },
                    paths: {
                        'jquery':'../../components/jquery/jquery.min',
                        'backbone':'../../components/backbone/backbone',
                        'replacemath':'../../components/replacemath/replacemath',
                        'underscore':'../../components/underscore/underscore',
                        'swig':'../../components/swig/swig',
                        'social-spread':'../../components/social-spread/social-spread',
                        'select2':'../../components/select2/select2.min',
                        'select2_locale':'../../components/select2/select2_locale_es',
                        'hogan':'../../components/hogan/web/1.0.0/hogan.min',
                        'parsley':'../../components/parsleyjs/dist/parsley.min',
                        'parsley_langs':'../../components/parsleyjs/i18n/messages.es',
                        'transit':'../../components/jquery.transit/jquery.transit',
                        'placeholder':'../../components/jquery-placeholder/jquery.placeholder.min',
                        'pikaday': '../../components/pikaday/pikaday',
                        'accounting':'../../components/accounting/accounting.min',
                        'icheck': '../../components/iCheck/jquery.icheck.min',
                        'spin': '../../components/spin.js/spin',
                        'fileupload': '../../components/blueimp-file-upload/js/jquery.fileupload',
                        'jquery.ui.widget': '../../components/blueimp-file-upload/js/vendor/jquery.ui.widget',
                        'spinner':'../../components/spin.js/spin',
                        'scroller':'../../components/scroller/nanoscroller',
                        'spinJquery': '../../components/spin.js/jquery.spin',
                        'moment': '../../components/momentjs/moment',
                        'modernizr':'../../components/modernizr/modernizr',
                        'cbpContentSlider':'../../plugins_js/jquery.cbpContentSlider',
                        'filtersView':'../../backbone/views/feed/filters',
                        'bootstrap':'../../components/js-bootstrap/bootstrap',
                        'route_feed':'../../backbone/routers/feed/feed',
                        'fabric':'../../components/fabric/dist/all.min',
                        'dropzone': '../../components/dropzone/dist/dropzone',
                        'angular':'../../components/angular/angular',
                        'angularAMD':'../../components/angularAMD/angularAMD',
                        'angulartics': '../../components/angulartics/dist/angulartics.min',
                        'angulartics_ga': '../../components/angulartics/dist/angulartics-ga.min',
                        'facebook':'../../components/angular-facebook/lib/angular-facebook',
                        'googleapi':'../../angular/google/googleapi',
                        'collection_applications':'../../backbone/collections/feed/applications',
                        'collection_questions':'../../backbone/collections/feed/questions',
                        'collections_questions_applications':'../../backbone/collections/feed/questions_applications',
                        'collections_postulations':'../../backbone/collections/feed/postulations',
                        'collections_my_questions':'../../backbone/collections/feed-students/my_questions',
                        'collections_my_subscriptions':'../../backbone/collections/feed-students/my_subscriptions',
                        'model_answer':'../../backbone/models/feed/answer',
                        'view_answer':'../../backbone/views/feed/answer',
                        'modal_register_student':'../../backbone/views/globals/modal_register_student',
                        'model_application':'../../backbone/models/feed/application',
                        'view_application':'../../backbone/views/feed/application',
                        'model_postulation':'../../backbone/models/feed/postulation',
                        'view_postulation':'../../backbone/views/feed/postulation',
                        'modal_newsletter':'../../backbone/views/escuelapadres/modal_newsletter',
                        'model_question':'../../backbone/models/feed/question',
                        'view_question':'../../backbone/views/feed/question',
                        'model_question':'../../backbone/models/feed/question',
                        'view_question':'../../backbone/views/feed/question',
                        'plan_suggestion': '../../backbone/views/aula/plan_suggestion',
                        'wizard': '../../backbone/views/aula/wizard',
                        'model_reservation':'../../backbone/models/feed/reservation',
                        'view_reservation':'../../backbone/views/feed/reservation',
                        'model_my_question':'../../backbone/models/feed-student/my_question',
                        'view_my_question':'../../backbone/views/feed-student/my_question',
                        'view_answer':'../../backbone/views/tutorteca/answer',
                        'model_my_subscription':'../../backbone/models/feed-student/my_subscription',
                        'view_my_subscription':'../../backbone/views/feed-student/my_subscription',
                        'text':'../../components/text/text',
                        'view_comments':'../../backbone/views/tutorteca/comments',
                        'view_landing_question':'../../backbone/views/landing_questions/question' ,
                        'js_image_slider':'../../src/js/js-image-slider',
                        'calculate_balance':'../../backbone/views/landings/calculate_balance',
                        'rwd_modal_register':'../../backbone/views/globals/rwd_modal_register',
                        'tooltip':'../../src/js/tooltip',
                        'modal_error':'../../backbone/views/modals/modal_error',
                        'loaderSpinner':'../../backbone/views/globals/LoaderSpinner',
                        'feed_student_aside':'../../backbone/views/feed-student/aside',
                        'route_feed_student':'../../backbone/routers/feed-student/feed_student',
                        'create_question':'../../backbone/views/feed-student/create_question',
                        'create_application':'../../backbone/views/feed-student/create_application',
                        'view_virtual_application':'../../backbone/views/feed/virtual_application',
                        'model_virtual_application':'../../backbone/models/feed/virtual_application',
                        'view_student_virtual_application':'../../backbone/views/feed-student/virtual_application',
                        'model_student_virtual_application':'../../backbone/models/feed-student/virtual_application',
                        'Nav':'../../backbone/views/globals/Nav',
                        'view_sec_my_balance':'../../backbone/views/feed/sec_my_balance',
                        'collection_balance_payments': '../../backbone/collections/feed/balance_payments',
                        'model_balance_payment':'../../backbone/models/feed/balance_payment',
                        'view_balance_payment':'../../backbone/views/feed/balance_payment',
                        'tutor_profile':'../../backbone/views/private/tutor/tutor_profile',
                        'v_modal_update_info_aula_st':'../../backbone/views/private/student/modal_update_info_aula',
                        'view_classroom':'../../backbone/views/aula/classroom_sharing_files',
                        'tour_help':'../../backbone/views/tour/tour_help',
                        'feed_student_filters':'../../backbone/views/feed-student/filters',
                        'sec_my_classes':'../../backbone/views/feed-student/sec_my_classes',
                        'dropzone':'../../components/dropzone/dist/dropzone',
                        'view_aside':'../../backbone/views/feed/aside',
                        'app':'../../angular/recharge_account/app',
                        'qrcode': '../../components/jquery.qrcode/dist/jquery.qrcode.min',
                        'modal_encuesta':'../../backbone/views/modals/modal_encuesta',
                        'recharge_account_controllers':'../../angular/recharge_account/controllers',
                        'recharge_account_services':'../../angular/recharge_account/services',
                        'view_modal_confirm_billing_data':'../../backbone/views/recharge/modal_confirm_billing_data',
                        'our_classroom_app':'../../angular/our_classroom/app',
                        'our_classroom_controllers':'../../angular/our_classroom/controllers',
                        'our_tutors_app':'../../angular/our_tutors/app',
                        'our_tutors_controllers':'../../angular/our_tutors/controllers',
                        'interactive_onboarding': '../../backbone/views/onboarding/interactive_onboarding',
                        'app_refer_friend':'../../angular/refer_friend/app',
                        'fbController': '../../angular/facebook/fcControllers',
                        'directives_refer_friend': '../../angular/refer_friend/directives',
                        'modal_update_mobil_phone': '../../backbone/views/globals/modal_update_mobil_phone',
                        'refer_friend_controllers': '../../angular/refer_friend/controllers',
                        'refer_friend_services': '../../angular/refer_friend/services',
                        'ngClip':'../../components/ng-clip/src/ngClip',
                        'require.min': '../../components/requirejs/require',
                        'modal_register_student_answer':'../../backbone/views/globals/modal_register_student_answer',
                    },
                    shim: {
                        'jquery': {
                            exports: 'jQuery'
                        },
                        'underscore':{
                            'exports':'_',
                        },
                        'backbone':{
                            'deps': [ 'jquery' , 'underscore' ],
                            'exports':'Backbone'
                        },
                        'swig':{
                            'exports':'swig'
                        },
                        'placeholder': ['jquery'],
                        'social-spread': ['jquery'],
                        'parsley': ['jquery'],
                        'scroller': ['jquery'],
                        'bootstrap': {
                            deps:['jquery'],
                            exports:'jQuery'
                        },
                        'parsley_langs': [ 'jquery', 'parsley' ],
                        'select2': ['jquery'],
                        'transit': ['jquery'],
                        'pikaday': {
                            exports: 'Pikaday'
                        },
                        'zeroclipboard':{
                            deps:['jquery']
                        },
                        'hogan': {
                            exports: 'hogan'
                        },
                        'accounting': {
                            exports: 'accounting'
                        },
                        'icheck': {
                            exports: 'iCheck',
                            deps: ['jquery']
                        },
                        'fabric': {
                            exports: 'fabric',
                            deps: ['jquery']
                        }
                    },
                    modules: [
                    {
                        name: 'ApplicationForm'
                    },
                    {
                        name: 'VirtualApplication'
                    },
                    {
                        name: 'AcceptingTutors'
                    },
                    {
                        name: 'SaberLanding'
                    },
                    {
                        name: 'ReferFriend'
                    },
                    {
                        name: 'ExpressComments'
                    },
                    {
                        name: 'CalculateBalance'
                    },
                    {
                        name: 'Answer'
                    },
                    {
                        name: 'Nav'
                    },
                    {
                        name: 'Home'
                    },
                    {
                        name: 'Newsletter'
                    },
                    {
                        name: 'OnboardingStudent'
                    },
                    {
                        name: 'Tdu'
                    },
                    {
                        name: 'TutorProfile'
                    },
                    {
                        name: 'LatexGen'
                    },
                    {
                        name: 'Feed'
                    },
                    {
                        name: 'FeedStudent'
                    },
                    {
                        name: 'StudentRequests'
                    },
                    {
                        name: 'TutorLanding'
                    },
                    {
                        name: 'QuestionLanding'
                    },
                    {
                        name: 'QuestionForm'
                    },
                    {
                        name: 'our_classroom',
                    },{
                        name: 'our_tutors',
                    },{
                        name: 'create_user',
                    }
                    ,{
                        name: 'courseslanding',
                    }
                    ]
                }

        }
    }
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        meta: {
            project: 'Tutorya',
            version: '0.4',
            banner: '/*! <%= meta.project %> - v<%= meta.version %> - Copyright (c) Tutorya <%= grunt.template.today("dddd, mmmm dS, yyyy, h:MM:ss TT") %> */'
        },
        uglify: {
            options: {
                banner: '/*! <%= meta.project %> - v<%= meta.version %> - Copyright (c) Tutorya. Build Time: <%= grunt.template.today("dddd, mmmm dS, yyyy, h:MM:ss TT") %> */',
                mangle: false,
                compress: true
            },
            build: {
                files: {
                    'content/build/js/require.min.js': ['content/components/requirejs/require.js'],
                    'content/build/js/Answer.min.js': ['content/src/js/Answer.js'],
                    'content/build/js/Nav.min.js': ['content/src/js/Nav.js'],
                    'content/build/js/ReferFriend.min.js': ['content/src/js/ReferFriend.js'],
                    'content/build/js/Home.min.js': ['content/src/js/Home.js'],
                    'content/build/js/OnboardingStudent.min.js': ['content/src/js/OnboardingStudent.js'],
                    'content/build/js/Tdu.min.js': ['content/src/js/Tdu.js'],
                    'content/build/js/VirtualApplication.min.js': ['content/src/js/VirtualApplication.js'],
                    'content/build/js/Feed.min.js': ['content/src/js/Feed.js'],
                    'content/build/js/CalculateBalance.min.js': ['content/src/js/CalculateBalance.js'],
                    'content/build/js/courseslanding.min.js': ['content/src/js/courseslanding.js'],
                    'content/build/js/Home.min.js': ['content/src/js/Home.js'],
                    'content/build/js/Newsletter.min.js': ['content/src/js/Newsletter.js'],
                    'content/build/js/LatexGen.min.js': ['content/src/js/LatexGen.js'],
                    'content/build/js/FeedStudent.min.js': ['content/src/js/FeedStudent.js'],
                    'content/build/js/ExpressComments.min.js': ['content/src/js/ExpressComments.js'],
                    'content/build/js/TutorLanding.min.js': ['content/src/js/TutorLanding.js'],
                    'content/build/js/StudentRequests.min.js': ['content/src/js/StudentRequests.js'],
                    'content/build/js/TutorProfile.min.js': ['content/src/js/TutorProfile.js'],
                    'content/build/js/AcceptingTutors.min.js': ['content/src/js/AcceptingTutors.js'],
                    'content/build/js/RegisterForm.min.js': ['content/src/js/RegisterForm.js'],
                    'content/build/js/ProfileEdition.min.js': ['content/src/js/ProfileEdition.js'],
                    'content/build/js/ResetPassword.min.js': ['content/src/js/ResetPassword.js'],
                    'content/build/js/TutorPreferences.min.js': ['content/src/js/TutorPreferences.js'],
                    'content/build/js/StudentPreferences.min.js': ['content/src/js/StudentPreferences.js'],
                    'content/build/js/RateTutor.min.js': ['content/src/js/RateTutor.js'],
                    'content/build/js/ApplicationForm.min.js': ['content/src/js/ApplicationForm.js'],
                    'content/build/js/QuestionForm.min.js':['content/src/js/QuestionForm.js'],
                    'content/build/js/QuestionLanding.min.js':['content/src/js/QuestionLanding.js'],
                    'content/build/js/base.min.js':['content/src/js/base.js'],
                    'content/build/js/prototype_extend.min.js':['content/src/js/prototype_extend.js'],
                    'content/build/js/profile_complete.min.js':['content/src/js/profile_complete.js'],
                    'content/build/js/classroom_sharing_files.min.js':['content/src/js/classroom_sharing_files.js'],
                    'content/build/js/RechargeAccount.min.js':['content/src/js/RechargeAccount.js'],
                    'content/build/js/recharge_account.min.js':['content/src/js/recharge_account.js'],
                    'content/build/js/our_classroom.min.js':['content/src/js/our_classroom.js'],
                    'content/build/js/our_tutors.min.js':['content/src/js/our_tutors.js'],
                    'content/build/js/facebook.min.js':['content/src/js/facebook.js'],
                    'content/build/js/ZeroClipboard.min.js':['content/components/zeroclipboard/dist/ZeroClipboard.js'],
                    'content/build/js/create_user.min.js':['content/src/js/create_user.js'],
                    'content/build/js/SaberLanding.min.js':['content/src/js/SaberLanding.js'],
                }
            }
        },
        clean: ['content/build/css', 'content/build/js'],
        compass: {
            dist: {
                options: {
                    config: 'content/config_dev.rb'
                }
            },
            dev: {
                options: {
                    config: 'content/config.rb',
                }
            },
        },
        shell: {
            server: {
                command: './manage.py runserver 0.0.0.0:8000'
            }
        },
        concurrent: {
            options: {
                logConcurrentOutput: true
            },
            dev: {
                tasks: ["watch:compass_dev"]
            }
        },
        sass: {
            options: {
                includePaths: ['content/components/compass-mixins/lib'],
                imagePath: '../../imgs',
                outputStyle: 'nested',
                sourceMap: true,
                indentedSyntax: true,
                sourceComments: false,
            },
            dist: {
                files: [{
                    expand: true,
                    cwd: "content/styles/",
                    src:["**/*.sass",'**/*.scss', '!**/_*.scss'],
                    dest: "content/styles/css",
                    ext: ".css"
                }],
                options:{
                    livereload: true
                }
            }
        },
        watch: {
            compass: {
                files: ['content/**'],
                tasks: ['compass:dev'],
            },
            compass_dev:{
                files: ['content/**'],
                tasks: ['sass:dist'],
                options:{
                    port: 8011,
                    livereload: true
                }
            }
        },
        requirejs: requirejsOptions,


    });
//grunt.loadNpmTasks('grunt-contrib-requirejs');
grunt.loadNpmTasks('grunt-requirejs');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-compass');
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-shell');
grunt.loadNpmTasks('grunt-contrib-clean');
grunt.loadNpmTasks('grunt-concurrent');
grunt.loadNpmTasks('grunt-sass');
grunt.registerTask( 'production', ['clean', 'compass:dist', 'requirejs', 'uglify'] );
grunt.registerTask( 'dev', ['concurrent:dev'] );
grunt.registerTask( 'dev_watch', ['watch:compass'] );
};