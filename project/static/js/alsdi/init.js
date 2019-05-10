$(document).ready(function(){
    var BASE_URL = "http://localhost:8000/"

    M.AutoInit();
    AOS.init();
    $(window).load(function() {
      // Animate loader off screen
      $("#loading-spinner").fadeOut("slow");
    });


    $('.carousel').carousel({
      fullWidth: true,
      indicators: true
    });

    particlesJS.load('particles-js', BASE_URL + 'static/js/alsdi/particles.json', function() {
      console.log('callback - particles.js config loaded');
    });  

    autoplay()
    function autoplay() {
      $('.carousel').carousel('next');
      setTimeout(autoplay, 6000);
    }

    $('.counter').counterUp({
      delay: 50,
      time: 1500
  });
})


        
