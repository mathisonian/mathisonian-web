/* Foundation v2.2.1 http://foundation.zurb.com */
jQuery(document).ready(function ($) {


    $("#slides").slides();

    $('#redactor_content').redactor({minHeight: 100, source: false});
    
    /* Use this js doc for all application specific JS */

    /* TABS --------------------------------- */
    /* Remove if you don't need :) */

    function activateTab($tab) {
        var $activeTab = $tab.closest('dl').find('a.active'),
                contentLocation = $tab.attr("href") + 'Tab';
                
        // Strip off the current url that IE adds
        contentLocation = contentLocation.replace(/^.+#/, '#');

        //Make Tab Active
        $activeTab.removeClass('active');
        $tab.addClass('active');

    //Show Tab Content
        $(contentLocation).closest('.tabs-content').children('li').hide();
        $(contentLocation).css('display', 'block');
    }

    $('dl.tabs').each(function () {
        //Get all tabs
        var tabs = $(this).children('dd').children('a');
        tabs.click(function (e) {
            activateTab($(this));
        });
    });

    if (window.location.hash) {
        activateTab($('a[href="' + window.location.hash + '"]'));
        $.foundation.customForms.appendCustomMarkup();
    }

    /* ALERT BOXES ------------ */
    $(".alert-box").delegate("a.close", "click", function(event) {
    event.preventDefault();
      $(this).closest(".alert-box").fadeOut(function(event){
        $(this).remove();
      });
    });


    /* PLACEHOLDER FOR FORMS ------------- */
    /* Remove this and jquery.placeholder.min.js if you don't need :) */

    $('input, textarea').placeholder();

    /* TOOLTIPS ------------ */
    $(this).tooltips();

    // window.onerror = function(error, url, line) {
    // // controller.sendLog({acc:'error', data:'ERR:'+error+' URL:'+url+' L:'+line});
    // };



    /* UNCOMMENT THE LINE YOU WANT BELOW IF YOU WANT IE6/7/8 SUPPORT AND ARE USING .block-grids */
//  $('.block-grid.two-up>li:nth-child(2n+1)').css({clear: 'left'});
//  $('.block-grid.three-up>li:nth-child(3n+1)').css({clear: 'left'});
//  $('.block-grid.four-up>li:nth-child(4n+1)').css({clear: 'left'});
//  $('.block-grid.five-up>li:nth-child(5n+1)').css({clear: 'left'});



    /* DROPDOWN NAV ------------- */

    var lockNavBar = false;
    $('.nav-bar a.flyout-toggle').live('click', function(e) {
        e.preventDefault();
        var flyout = $(this).siblings('.flyout');
        if (lockNavBar === false) {
            $('.nav-bar .flyout').not(flyout).slideUp(500);
            flyout.slideToggle(500, function(){
                lockNavBar = false;
            });
        }
        lockNavBar = true;
    });
  if (Modernizr.touch) {
    $('.nav-bar>li.has-flyout>a.main').css({
      'padding-right' : '75px'
    });
    $('.nav-bar>li.has-flyout>a.flyout-toggle').css({
      'border-left' : '1px dashed #eee'
    });
  } else {
    $('.nav-bar>li.has-flyout').hover(function() {
      $(this).children('.flyout').show();
    }, function() {
      $(this).children('.flyout').hide();
    });
  }

    var displayError = function(e){
        $('.error-span').text(e.message);
    };


    var initSketch2d = function(p) {
        p.setup = function() {
            p.size($(".sketch").width(), $(".sketch").height());
        };
        i = 0;
        p.draw = function() {
            p.background(0, 255 * p.pow(p.sin(i), 2));
            i += 0.01;
        };
    };

    var initSketch3d = function(p) {
        p.setup = function() {
            p.size($(".sketch").width(), $(".sketch").height(), p.OPENGL);
        };
        // Declare persist variables here
        //
        // e.g. frameCount = 0;
        steps = 250;
        curStep = 0;
         
        // This function gets called
        // every frame
        p.draw = function() {
            try {
              p.noStroke();
              p.background(0, 0, 0, 0);
              p.lights();
              p.translate(p.width/2,
                          p.height/2, 0);
              p.rotateX(2*p.PI / steps * curStep++);
              p.rotateY(-p.PI/3 +
                        210 / p.height * p.PI);
              p.box(45);
              p.translate(0,0, -50);
              p.box(30);
              p.translate(0, 0, -35);
              p.box(17);
            } catch(e) {
                displayError(e);
            }
        };
    };

    var p;

    var updateCanvas = function() {
        try {
            $('.error-span').text("");
            var selection = $.trim(editor.getSelection());
            if(selection !== "") {
                eval(editor.getSelection());
            } else {
                eval(editor.getValue());
            }
            $('.error-span').text("success!");
        } catch(e) {
            $('.error-span').text(e.message);
        }
    };

    var canvas = document.getElementById("sketch2d");
    if(canvas) {
        p = new Processing(canvas, initSketch2d);
    } else {
        canvas = document.getElementById("sketch3d");
        if(canvas) {
            p = new Processing(canvas, initSketch3d);
        }
    }

    /* DISABLED BUTTONS ------------- */
    /* Gives elements with a class of 'disabled' a return: false; */

    if(typeof CodeMirror !== undefined) {
        var editor = CodeMirror.fromTextArea(document.getElementById("code-editor"), {
            mode: "javascript",
            lineNumbers: true,
            autofocus: true,
            extraKeys: {
                "Ctrl-Enter": updateCanvas
            }
        });
    }
  
});
