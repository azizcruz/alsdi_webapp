$(document).ready(function(){
    // To get particels js data.
    var BASE_URL = "http://" + location.hostname + ":8000"
    // Initialize all materialize css plugins.
    M.AutoInit();

    // Initialize AOS animation plugin.
    AOS.init();

    // When page is loaded hide the loading.
    $(window).load(function() {
      // Animate loader off screen
      $("#loading-spinner").fadeOut("slow");
    });

    // Initialize navbar stick on scroll.
    $("#sticker").sticky({topSpacing:0});

    // Initialize main page carousel
    $('.carousel').carousel({
      fullWidth: true,
      indicators: true
    });

    particlesJS.load('particles-js', BASE_URL + '/static/js/alsdi/particles.json', function() {
      console.log('callback - particles.js config loaded');
    });  

    // Auto play for main page carousel
    autoplay()
    function autoplay() {
      $('.carousel').carousel('next');
      setTimeout(autoplay, 6000);
    }

    // Initialize counter for main page.
    $('.counter').counterUp({
      delay: 50,
      time: 1500
  });
})


        
