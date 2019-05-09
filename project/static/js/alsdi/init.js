$(document).ready(function(){
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

    
    autoplay()
    function autoplay() {
      $('.carousel').carousel('next');
      setTimeout(autoplay, 6000);
    }
})


        
