/* Foundation v2.2.1 http://foundation.zurb.com */
jQuery(document).ready(function ($) {
      $.ajaxSetup({ traditional: true });

      // csrf token support
      $(document).ajaxSend(function(event, xhr, settings) {
          function getCookie(name) {
              var cookieValue = null;
              if (document.cookie && document.cookie != '') {
                  var cookies = document.cookie.split(';');
                  for (var i = 0; i < cookies.length; i++) {
                      var cookie = jQuery.trim(cookies[i]);
                      // Does this cookie string begin with the name we want?
                      if (cookie.substring(0, name.length + 1) == (name + '=')) {
                          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                          break;
                      }
                  }
              }
              return cookieValue;
          }
          function sameOrigin(url) {
              // url could be relative or scheme relative or absolute
              var host = document.location.host; // host + port
              var protocol = document.location.protocol;
              var sr_origin = '//' + host;
              var origin = protocol + sr_origin;
              // Allow absolute or scheme relative URLs to same origin
              return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                  (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                  // or any other URL that isn't scheme relative or absolute i.e relative.
                  !(/^(\/\/|http:|https:).*/.test(url));
          }
          function safeMethod(method) {
              return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
          }

          if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
              xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
          }
      });

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


    var cleanURL = function(url) {
      return url.replace(/\/\/+/g,'\/');
    };


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
            if(typeof p.init === 'function') {
              p.init();
            }
        };

        if (sketchContent) {
            eval(sketchContent);
        } else {
          i=0;
          p.draw = function() {
            p.background(0, 255 * p.pow(p.sin(i), 2));
            i += 0.01;
          };
        }
        
    };

    var initSketch3d = function(p) {

        p.setup = function() {
            p.size($(".sketch").width(), $(".sketch").height(), p.OPENGL);
            if(typeof p.init === 'function') {
              p.init();
            }
        };
        if (sketchContent) {
            eval(sketchContent);
        } else {
            // This function gets called
            // every frame
            steps=250; curStep=0;
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
        }
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
    var has_canvas=false;
    if(canvas) {
        p = new Processing(canvas, initSketch2d);
        has_canvas=true;
    } else {
        canvas = document.getElementById("sketch3d");
        if(canvas) {
            p = new Processing(canvas, initSketch3d);
            has_canvas=true;
        }
    }

    if(has_canvas) {
        $('.save-sketch-3d').click(function() {
          $.ajax({
            type: "POST",
            url: cleanURL('/labs/processing/create/3d/'),
            data: {
                content: editor.getValue()
            },
            success: function(data) {
              window.location = "/labs/processing/3d/" + data.sketch_id;
            }
          });
        });

        $('.version-sketch-3d').click(function() {
          $.ajax({
            type: "POST",
            url: cleanURL('/labs/processing/version/3d/'),
            data: {
                content: editor.getValue(),
                sketch_id: sketch_id
            },
            success: function(data) {
              window.location = "/labs/processing/3d/" + sketch_id + '/' + data.version_number;
            }
          });
        });

        $('.save-sketch-2d').click(function() {
          $.ajax({
            type: "POST",
            url: cleanURL('/labs/processing/create/2d/'),
            data: {
                content: editor.getValue()
            },
            success: function(data) {
              window.location = "/labs/processing/2d/" + data.sketch_id;
            }
          });
        });

        $('.version-sketch-3d').click(function() {
          $.ajax({
            type: "POST",
            url: cleanURL('/labs/processing/version/2d/'),
            data: {
                content: editor.getValue(),
                sketch_id: sketch_id
            },
            success: function(data) {
              window.location = "/labs/processing/2d/" + sketch_id + '/' + data.version_number;
            }
          });
        });
    }

    /* DISABLED BUTTONS ------------- */
    /* Gives elements with a class of 'disabled' a return: false; */

    if(typeof CodeMirror !== 'undefined') {
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
