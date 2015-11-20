define(function  (require) {
    'use strict';

    var $ = require('jquery');

    $(document).ready(function  () {
        $('#user-prefer').click(function(e) {
          if($(this).hasClass('open')){

            $('#dropdown-top').slideUp(100);
            $(this).removeClass('open');

          }else{

            $('#dropdown-top').slideDown(100);
            $(this).addClass('open');

          }
          e.stopPropagation();
        });

        $("#library-main").animate({
                opacity: '1'
            }, 500);
         $("#loaderpage").hide();

    })
})