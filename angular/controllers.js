define(function(require) {
  'use strict';
  var angular = require("angular");
  return angular.module('library.controllers', [])
  .controller('LibraryController',
    function($scope, $location) {
      var s=$scope;
      s.course=0;
      s.content_title="";
      s.content_type="";
      s.content_media="";
      s.content_subject="";
      s.content_description="";
      s.content_tutor="";
      s.content_date="";
      s.filter_name="Todos";
      $scope.filterRwd = function(){
        var el=$('#select-'+s.course).addClass('selected');
        s.course=parseInt(s.course);
        console.log(s.course);
        console.log($('#materia').find('option:first-child').val());
      }
      $scope.filterCourse = function(course){
            s.course=course;
            console.log(s.course);
            var el=$('#tab-'+course);
            s.filter_name=el.find('.sbjitem').html();
            var target=$('.week-resources-header');
            var d= target.offset().top;
            d= d-50;
            $('.course-block').removeClass('active');
            el.addClass('active');
            $('html,body').animate({
                      scrollTop: d
            }, 1000);
      }
      $scope.playContent = function(id,auto) {

        var el=document.getElementById(id);
        var tipo=el.getAttribute('data-type');
        if(tipo=='ENLACE'){
          var a = document.createElement("a");
          a.target = "_blank";
          a.href = el.getAttribute('data-url');
          a.click();
        }
        else if(tipo=='DOCUMENTO'){
          var a = document.createElement("a");
          a.target = "_blank";
          a.href ='/media/'+el.getAttribute('data-file');
          a.click();
        }
        else{
          if(auto){
            $location.path('/cursos/recursos/'+el.getAttribute('data-slug'));
            $location.replace();
          }
          $('.course-media-media').empty();
          s.content_title=el.getAttribute('data-name');
          if(tipo=='IMAGEN'){
            var media=el.getAttribute('data-file');
            s.content_media='<img class="img-responsive" src="/media/'+media+'"/>';
            $('.course-media-media').append(s.content_media);
          }
          else if(tipo=='VIDEO'){
            console.log('entro a video');
            var media=el.getAttribute('data-url');
            if (media.indexOf("youtube") > -1){
              media=media.replace('https://www.youtube.com/watch?v=','');
              console.log(media);
              if (auto){
                var html_video='<iframe width="100%" height="389px" src="https://www.youtube.com/embed/'+media+'?autoplay=1&modestbranding=1&showinfo=0&rel=0" frameborder="0" allowfullscreen></iframe>';
              }
              else{
                var html_video='<iframe width="100%" height="389px" src="https://www.youtube.com/embed/'+media+'?autoplay=0&modestbranding=1&showinfo=0&rel=0" frameborder="0" allowfullscreen></iframe>';
              }
              $('.course-media-media').append(html_video);
            }
          }
          if(auto){
            var x = $('#media_player').offset().top - 100; // 100 provides buffer in viewport
            $('html,body').animate({scrollTop: x}, 500);
            $.ajax({
              type: "POST",
              url: 'cursos/mark_resource',
              data: {resource: el.getAttribute('data-resource')},
              success:function  (data) {
                console.log(data);
              },
             }).done(function  () {
              });
          }
          s.content_type=tipo.toLowerCase();
          s.content_subject=el.getAttribute('data-subject');
          s.content_description=el.getAttribute('data-description');
          s.content_tutor=el.getAttribute('data-tutor');
          s.content_date=el.getAttribute('data-date');
      }
        //LibraryService.mark_resource(resource_id).then(function(data){});
    }
}
)
.config(function($locationProvider) {
  $locationProvider.html5Mode(true);
})
.controller('ContentViewController',['$scope',
  function  ($scope) {
  }])
.controller('ResurcesViewController',['$scope',
  function  ($scope) {
  }])
});