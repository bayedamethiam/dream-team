(function($){
	"use strict";
	jQuery(document).on('ready', function () {
		
		// Mean Menu
		jQuery('.mean-menu').meanmenu({
			meanScreenWidth: "991"
        });

        // Header Sticky
		$(window).on('scroll',function() {
            if ($(this).scrollTop() > 120){  
                $('.navbar-area').addClass("is-sticky");
            }
            else{
                $('.navbar-area').removeClass("is-sticky");
            }
        });

        // Search Popup JS
        $('.close-btn').on('click',function() {
            $('.search-overlay').fadeOut();
            $('.search-btn').show();
            $('.close-btn').removeClass('active');
        });
        $('.search-btn').on('click',function() {
            $(this).hide();
            $('.search-overlay').fadeIn();
            $('.close-btn').addClass('active');
        });

        // Home Slides
		$('.home-slides').owlCarousel({
			loop: true,
			nav: true,
            dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 750,
            items: 1,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
        });
        $('.home-slides-two').owlCarousel({
			loop: true,
			nav: true,
            dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 750,
            items: 1,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
        });
        $(".home-slides, .home-slides-two").on("translate.owl.carousel", function(){
            $(".main-banner-content h1").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content p").removeClass("animated fadeInUp").css("opacity", "0");
            $(".main-banner-content .btn").removeClass("animated fadeInUp").css("opacity", "0");
        });
        $(".home-slides, .home-slides-two").on("translated.owl.carousel", function(){
            $(".main-banner-content h1").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content p").addClass("animated fadeInUp").css("opacity", "1");
            $(".main-banner-content .btn").addClass("animated fadeInUp").css("opacity", "1");
        });
		
		// Services Slides
		$('.services-slides').owlCarousel({
			loop: true,
			nav: false,
			dots: true,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
			responsive: {
                0: {
                    items: 1,
                },
                768: {
                    items: 2,
                },
                1200: {
                    items: 3,
				}
            }
        });

        // MixItUp Shorting
		$(function(){
            $('.shorting').mixItUp();
        });
        
        // Partner Slides
		$('.partner-slides').owlCarousel({
			loop: true,
			nav: false,
            dots: false,
            margin: 30,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
			responsive: {
                0: {
                    items: 2,
                },
                576: {
                    items: 3,
                },
                768: {
                    items: 4,
                },
                1200: {
                    items: 5,
				}
            }
        });

        // Partner Slides Two
		$('.partner-slides-two').owlCarousel({
			loop: true,
			nav: false,
            dots: false,
            margin: 30,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
			responsive: {
                0: {
                    items: 2,
                },
                768: {
                    items: 4,
                },
                1200: {
                    items: 7,
				}
            }
        });

        // Partner Slides Three
		$('.partner-slides-three').owlCarousel({
			loop: true,
			nav: false,
            dots: false,
            margin: 30,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
			responsive: {
                0: {
                    items: 2,
                },
                768: {
                    items: 4,
                },
                1200: {
                    items: 5,
				}
            }
        });

        // Nice Select JS
        $('select').niceSelect();

        // Testimonials Slides
		$('.testimonials-slides').owlCarousel({
			loop: true,
			nav: true,
            dots: false,
			autoplayHoverPause: true,
            autoplay: true,
            items: 1,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
        });

        // Popup Video
		$('.popup-youtube').magnificPopup({
			disableOn: 320,
			type: 'iframe',
			mainClass: 'mfp-fade',
			removalDelay: 160,
			preloader: false,
			fixedContentPos: false
        });

        // Go to Top
        $(function(){
            // Scroll Event
            $(window).on('scroll', function(){
                var scrolled = $(window).scrollTop();
                if (scrolled > 600) $('.go-top').addClass('active');
                if (scrolled < 600) $('.go-top').removeClass('active');
            });  
            // Click Event
            $('.go-top').on('click', function() {
                $("html, body").animate({ scrollTop: "0" },  500);
            });
        });

        // Services Details Image Slides
		$('.services-details-image-slides').owlCarousel({
			loop: true,
			nav: false,
            dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 750,
            items: 1,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
        });

        // Testimonials Vertical Slider
        $('.testimonials-vertical-slider').slick({
            dots: true,
            vertical: true,
            slidesToShow: 3,
            slidesToScroll: 3,
            verticalSwiping: true,
            loop: true,
            prevArrow: false,
            nextArrow: false,
            responsive: [
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 2,
                        infinite: true,
                        dots: true
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
            ]
        });

        // Feedback Slides
        $('.feedback-slides').owlCarousel({
			loop: true,
			nav: false,
            dots: true,
			autoplayHoverPause: true,
            autoplay: true,
            smartSpeed: 750,
            items: 1,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
        });

        // Feedback Mobile Slides Three
		$('.feedback-mobile-slides').owlCarousel({
			loop: true,
			nav: false,
            dots: true,
            margin: 30,
			autoplayHoverPause: true,
			autoplay: true,
            navText: [
                "<i class='flaticon-left'></i>",
                "<i class='flaticon-right'></i>"
            ],
			responsive: {
                0: {
                    items: 1,
                },
                768: {
                    items: 2,
                },
                1200: {
                    items: 2,
				}
            }
        });

        // Timeline Slides
        $('.timeline-nav').slick({
            slidesToShow: 12,
            slidesToScroll: 1,
            asNavFor: '.timeline-slider',
            centerMode: false,
            focusOnSelect: true,
            mobileFirst: true,
            arrows: false,
            autoplay: false,
            infinite:false,
            draggable: false,
            responsive: [
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 7,
                    }
                },
                {
                    breakpoint: 0,
                    settings: {
                        slidesToShow: 4,
                        slidesToScroll: 2,
                    }
                }
            ]
        });
        $('.timeline-slider').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,
            asNavFor: '.timeline-nav',
            centerMode: true,     
            cssEase: 'ease',
            edgeFriction: 0.5,
            mobileFirst: true,
            draggable: false,
            speed: 500,
            autoplay: false,
            responsive: [
                {
                    breakpoint: 0,
                    settings: {
                        centerMode: false
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        centerMode: true
                    }
                }
            ]
        });

        // Subscribe form
		$(".newsletter-form").validator().on("submit", function (event) {
			if (event.isDefaultPrevented()) {
			// handle the invalid form...
				formErrorSub();
				submitMSGSub(false, "Please enter your email correctly.");
			} else {
				// everything looks good!
				event.preventDefault();
			}
		});
		function callbackFunction (resp) {
			if (resp.result === "success") {
				formSuccessSub();
			}
			else {
				formErrorSub();
			}
		}
		function formSuccessSub(){
			$(".newsletter-form")[0].reset();
			submitMSGSub(true, "Thank you for subscribing!");
			setTimeout(function() {
				$("#validator-newsletter").addClass('hide');
			}, 4000)
		}
		function formErrorSub(){
			$(".newsletter-form").addClass("animated shake");
			setTimeout(function() {
				$(".newsletter-form").removeClass("animated shake");
			}, 1000)
		}
		function submitMSGSub(valid, msg){
			if(valid){
				var msgClasses = "validation-success";
			} else {
				var msgClasses = "validation-danger";
			}
			$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
		}
		// AJAX MailChimp
		$(".newsletter-form").ajaxChimp({
			url: "https://envytheme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
			callback: callbackFunction
        });
        
        // FAQ Accordion
        $(function() {
            $('.accordion').find('.accordion-title').on('click', function(){
                // Adds Active Class
                $(this).toggleClass('active');
                // Expand or Collapse This Panel
                $(this).next().slideToggle('fast');
                // Hide The Other Panels
                $('.accordion-content').not($(this).next()).slideUp('fast');
                // Removes Active Class From Other Titles
                $('.accordion-title').not($(this)).removeClass('active');		
            });
        });
        
        // Count Time 
        function makeTimer() {
            var endTime = new Date("September 30, 2020 17:00:00 PDT");			
            var endTime = (Date.parse(endTime)) / 1000;
            var now = new Date();
            var now = (Date.parse(now) / 1000);
            var timeLeft = endTime - now;
            var days = Math.floor(timeLeft / 86400); 
            var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
            var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
            var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
            if (hours < "10") { hours = "0" + hours; }
            if (minutes < "10") { minutes = "0" + minutes; }
            if (seconds < "10") { seconds = "0" + seconds; }
            $("#days").html(days + "<span>Days</span>");
            $("#hours").html(hours + "<span>Hours</span>");
            $("#minutes").html(minutes + "<span>Minutes</span>");
            $("#seconds").html(seconds + "<span>Seconds</span>");
        }
        setInterval(function() { makeTimer(); }, 1000);
        
        // Products Details Image Slides
        $('.product-page-gallery-main').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: true,
            autoplay: true,
            fade: true,
            asNavFor: '.product-page-gallery-preview',
        });
        $('.product-page-gallery-preview').slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            asNavFor: '.product-page-gallery-main',
            dots: false,
            centerMode: false,
            focusOnSelect: true,
            arrows: false,
            autoplay: true,
        });

        // Input Plus & Minus Number JS
        $('.input-counter').each(function() {
            var spinner = jQuery(this),
            input = spinner.find('input[type="text"]'),
            btnUp = spinner.find('.plus-btn'),
            btnDown = spinner.find('.minus-btn'),
            min = input.attr('min'),
            max = input.attr('max');
            
            btnUp.on('click', function() {
                var oldValue = parseFloat(input.val());
                if (oldValue >= max) {
                    var newVal = oldValue;
                } else {
                    var newVal = oldValue + 1;
                }
                spinner.find("input").val(newVal);
                spinner.find("input").trigger("change");
            });
            btnDown.on('click', function() {
                var oldValue = parseFloat(input.val());
                if (oldValue <= min) {
                    var newVal = oldValue;
                } else {
                    var newVal = oldValue - 1;
                }
                spinner.find("input").val(newVal);
                spinner.find("input").trigger("change");
            });
        });

        // Tabs
        (function ($) {
            $('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
            $('.tab ul.tabs li a').on('click', function (g) {
                var tab = $(this).closest('.tab'), 
                index = $(this).closest('li').index();
                tab.find('ul.tabs > li').removeClass('current');
                $(this).closest('li').addClass('current');
                tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
                tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
                g.preventDefault();
            });
        })(jQuery);

    });

    // Odometer
    jQuery(document).on('ready', function() {
		$('.odometer').appear(function(e) {
			var odo = $(".odometer");
			odo.each(function() {
				var countNumber = $(this).attr("data-count");
				$(this).html(countNumber);
			});
		});
    });
    
    // Preloader Area
	jQuery(window).on('load', function() {
	    $('.preloader').fadeOut();
    });
    
}(jQuery));