// page init
jQuery(function(){
	"use strict";

	initTabSet();
	initTeamTab();
	initAnchors();
	initbackTop();
	initCounter();
	initAjaxLoad();
	initLightBox();
	initCountDown();
	new WOW().init();
	initStickyHeader();
	initFormValidation();
});

jQuery(window).on('load', function() {
	"use strict";

	initIsoTop();
	initPreLoader();
	initStyleChanger();
});

// count down init
function initCountDown() {
	var newDate = new Date(2016, 12, 28);
	
	jQuery("#defaultCountdown").countdown({until: newDate});
}

function initTeamTab(){
	jQuery(".text-box.team3 , .team3-img , .box1").hide();
	jQuery(".text-box.team2 , .team2-img").hide();
	jQuery(".team2-opener").click(function(event){
		event.preventDefault();
		jQuery(".text-box.team2 , .team2-img , .box1 , .box3").show();
		jQuery(".text-box.team3 , .team3-img , .box2").hide();
		jQuery(".text-box.team1 , .team1-img").hide();
	});
	jQuery(".team3-opener").click(function(event){
		event.preventDefault();
		jQuery(".text-box.team3 , .team3-img , .box2 , .box1").show();
		jQuery(".text-box.team2 , .team2-img , .box3").hide();
		jQuery(".text-box.team1 , .team1-img").hide();
	});
	jQuery(".team1-opener").click(function(event){
		event.preventDefault();
		jQuery(".text-box.team1 , .team1-img , .box3 , .box2").show();
		jQuery(".text-box.team2 , .team2-img , .box1").hide();
		jQuery(".text-box.team3 , .team3-img").hide();
	});
}

// ajax load init
function initAjaxLoad(){
	jQuery('.ajax-area').ajaxPopup({
		button: '.btn-load',
		ajaxHold: '#ajax-holder',
		appendToBody: false,
		attr: 'href',
	 	animSpeed: 500
	});
}

// initialize smooth anchor links
function initAnchors() {
	jQuery('#nav-smooth').onePageNav({
		currentClass: 'active',
		changeHash: false,
		scrollSpeed: 750
 	});
}

// sticky header init
function initStickyHeader() {
	var win = jQuery(window),
		stickyClass = 'sticky';

	jQuery('#header.sticky-header').each(function() {
		var header = jQuery(this);
		var headerOffset = header.offset().top || 0;
		var flag = true;

		function scrollHandler() {
			if (win.scrollTop() > headerOffset) {
				if (flag){
					flag = false;
					header.addClass(stickyClass);
				}
			} else {
				if (!flag) {
					flag = true;
					header.removeClass(stickyClass);
				}
			}

			ResponsiveHelper.addRange({
				'..767': {
					on: function() {
						header.removeClass(stickyClass);
					}
				}
			});
		}

		scrollHandler();
		win.on('scroll resize orientationchange', scrollHandler);
	});
}

// Counter init
function initCounter() {
	jQuery('.counter').counterUp();
}

// Counter init
function initTabSet() {
	// tabset init
	jQuery.tabset({
		header: '.info .slider .pagination a',
		content: '.info .slider .slide'
	});
}

// LightBox init
function initLightBox() {
	jQuery('a.lightbox, a[rel*="lightbox"]').fancybox({
		padding: 0,
		loop: false,
		helpers: {
			overlay: {
				css: {background: 'rgba(0, 0, 0, 0.35)'}
			}
		},
		afterLoad: function(current, previous) {
			// handle custom close button in inline modal
			if(current.href.indexOf('#') === 0) {
				jQuery(current.href).find('a.close').off('click.fb').on('click.fb', function(e){
					e.preventDefault();
					jQuery.fancybox.close();
				});
			}
		}
	});
}

// IsoTop init
function initIsoTop() {
	// Isotope init
	var isotopeHolder = jQuery('#masonry-container'),
		win = jQuery(window);
	jQuery('#masonry-container').isotope({
		itemSelector: '.item',
		transitionDuration: '0.6s'
	});
	jQuery('.filter a').click(function(e){
		e.preventDefault();
		
		jQuery('.filter li').removeClass('active');
		jQuery(this).parent('li').addClass('active');
		var selector = jQuery(this).attr('data-filter');
		isotopeHolder.isotope({ filter: selector });
	});
}

// sticky header init
function initbackTop() {
	var jQuerybackToTop = jQuery("#back-top");
	jQuery(window).on('scroll', function() {
		if (jQuery(this).scrollTop() > 100) {
			jQuerybackToTop.addClass('active');
		} else {
			jQuerybackToTop.removeClass('active');
		}
	});
	jQuerybackToTop.on('click', function(e) {
		jQuery("html, body").animate({scrollTop: 0}, 500);
	});
}

// PreLoader init
function initPreLoader() {
	jQuery('#pre-loader').delay(400).fadeOut();
}



// form validation init
function initFormValidation() {
	//if submit button is clicked
	$('#submit,#submit2').click(function () {

        //Get the data from all the fields
        var name = $('input[name=text-field-required]');
        var email = $('input[name=Emailfield]');
        var comment = $('textarea[name=textarea]');
        var returnError = false;

        //Simple validation to make sure user entered something
        //Add your own error checking here with JS, but also do some error checking with PHP.
        //If error found, add hightlight class to the text field
        if (name.val()=='') {
            name.addClass('error');
            returnError = true;
        } else name.removeClass('error');

        if (email.val()=='') {
            email.addClass('error');
            returnError = true;
        } else email.removeClass('error');

        if (comment.val()=='') {
            comment.addClass('error');
            returnError = true;
        } else comment.removeClass('error');

        // Highlight all error fields, then quit.
        if(returnError == true) {
            return false;	
        }

        //organize the data
        var data = 'name=' + name.val() + '&email=' + email.val() + '&comment='  + encodeURIComponent(comment.val());

        //disabled all the text fields
        $('.wpcf7-form-control').attr('disabled','true');

        //show the loading sign
        $('.loading').show();

        //start the ajax
        $.ajax({
            //this is the php file that processes the data and sends email
            url: "inc/process.php",	

            //GET method is used
            type: "GET",

            //pass the data	
            data: data,	

            //Do not cache the page
            cache: false,

            //success
            success: function (html) {	
            //if process.php returned 1/true (send mail success)
                if (html==1) {	
                //hide the form
                $('.f-contact-form').fadeOut('slow');	

                //show the success message
                $('.done-massage2').fadeIn('slow');

                //if process.php returned 0/false (send mail failed)
                } else alert('Sorry, unexpected error. Please try again later.');	
            }	
        });

        //cancel the submit button default behaviours
        return false;
	});
	//if submit button is clicked
	$('#contact-submit').click(function () {

        //Get the data from all the fields
        var name = $('input[name=name]');
        var phone = $('input[name=phone]');
        var email = $('input[name=email]');
        var comment = $('textarea[name=comment]');
        var returnError = false;

        //Simple validation to make sure user entered something
        //Add your own error checking here with JS, but also do some error checking with PHP.
        //If error found, add hightlight class to the text field
        if (name.val()=='') {
            name.addClass('error');
            returnError = true;
        } else name.removeClass('error');

        if (email.val()=='') {
            email.addClass('error');
            returnError = true;
        } else email.removeClass('error');

        if (comment.val()=='') {
            comment.addClass('error');
            returnError = true;
        } else comment.removeClass('error');

        // Highlight all error fields, then quit.
        if(returnError == true) {
            return false;	
        }

        //organize the data
        var data = 'name=' + name.val() + '&phone=' + phone.val() + '&email=' + email.val() + '&comment='  + encodeURIComponent(comment.val());

        //disabled all the text fields
        $('.wpcf7-form-control').attr('disabled','true');

        //show the loading sign
        $('.loading').show();

        //start the ajax
        $.ajax({
            //this is the php file that processes the data and sends email
            url: "inc/process2.php",	

            //GET method is used
            type: "GET",

            //pass the data	
            data: data,	

            //Do not cache the page
            cache: false,

            //success
            success: function (html) {	
            //if process.php returned 1/true (send mail success)
                if (html==1) {	
                //hide the form
                $('#contactform').fadeOut('slow');	

                //show the success message
                $('.done-massage3').fadeIn('slow');

                //if process.php returned 0/false (send mail failed)
                } else alert('Sorry, unexpected error. Please try again later.');	
            }	
        });

        //cancel the submit button default behaviours
        return false;
	});
}

// style changer
function initStyleChanger() {
	var element = jQuery('#style-changer');

	if(element) {
		$.ajax({
			url: element.attr('data-src'),
			type: 'get',
			dataType: 'text',
			success: function(data) {
				var newContent = jQuery('<div>', {
					html: data
				});

				newContent.appendTo(element);
				jQuery(".changer-opener").click(function(event){
					event.preventDefault();
					jQuery("body").toggleClass("changer-active");
				});
				
				var sheet,
					darkSheet,
					sheetName,
					darkSheetName = 'dark',
					sheetAdded = false,
					darkStylesAdded = false;

				jQuery('.list-color li').each(function() {
					var item = jQuery(this),
						link = item.find('a').eq(0);

					link.on('click', function(e) {
						e.preventDefault();
						sheetName = item.attr('class');

						if(!sheetAdded) {
							sheet = jQuery('<link>').attr('rel','stylesheet')
										.attr('type','text/css')
										.attr('href', 'css/color/' + sheetName + '.css')
										.appendTo('head');

							sheetAdded = true;
						} else {
							sheet.attr('href', 'css/color/' + sheetName + '.css');
						}
					});
				});
			}
		});
	}
}




/*
 * jQuery SlideMenu plugin
 */
;(function($){
	function AjaxPopup(options){
		this.options = $.extend({
			holder: null,
			button: '.btn-more',
			holderBox: 'body',
			ajaxHold: '#ajax-holder',
			appendToBody: false,
			attr: 'href',
			animSpeed: 500
		}, options);

		this.init();
	}
	AjaxPopup.prototype = {
		init: function(){
			this.findElements();
			this.makeCallback('onInit', this);
			this.attachEvents();
		},
		findElements: function(){
			this.holder = jQuery(this.options.holder);
			this.button = this.holder.find(this.options.button);
			this.ajaxHold = this.holder.find(this.options.ajaxHold);

		},
		attachEvents: function(){
			var self = this;
			this.clickHandler = function(e){
				e.preventDefault();
				var attr = self.button.attr(self.options.attr);
				if(attr != '#'){
					e.preventDefault();
					self.ajaxLoad(attr).done(function(data){
						var content = jQuery(data).filter('.blogs-block').css({opacity: 0});
						var btnAjax = jQuery(data).filter('.btn-load');

						if(self.options.appendToBody) content.appendTo(jQuery(self.options.holderBox));
						else content.appendTo(self.ajaxHold);

						if(btnAjax.length) self.button.attr('href', btnAjax.attr('href')); 
						else self.button.hide();
					
						content.stop().animate({opacity: 1}, self.options.animSpeed);
						self.makeCallback('onChange', self);
					});
				}
			};
			this.button.on('click', this.clickHandler);
		},
		ajaxLoad: function(url){
			var d = jQuery.Deferred();
			jQuery.ajax({
				url: url,
				type: 'get',
				cache: false,
				dataType: "html",
				success: function(data){
					d.resolve(data);
				},
				error: function(jqXHR, textStatus, errorThrown){
					d.reject(jqXHR, textStatus, errorThrown);
				}
			});
			return d;
		},
		makeCallback: function(name) {
			if(typeof this.options[name] === 'function') {
				var args = Array.prototype.slice.call(arguments);
					args.shift();
					this.options[name].apply(this, args);
				}
			}
		};

	$.fn.ajaxPopup = function(options){
		return this.each(function(){
			$(this).data('AjaxPopup', new AjaxPopup($.extend(options, {holder:this})));
		});
	};
})(jQuery);