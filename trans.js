function delay (URL) {
    setTimeout( function() { window.location = URL }, 800 );
}

$(function() {
  var main = $('#main');
  var about = $('#about');
  about.on('click', function(){
    main.toggleClass('active');
    
  });
});



$(function() {
  var main = $('#main');
  var about = $('#title');
  about.on('click', function(){
    main.toggleClass('active');
    
  });
});

$(function() {
  var main = $('#main');
  var about = $('#home');
  about.on('click', function(){
    main.toggleClass('active');
    
  });
});

$(function() {
  var main = $('#main');
  var about = $('#contact');
  about.on('click', function(){
    main.toggleClass('active');
    
  });
});

$(function() {
  var main = $('#main');
  var about = $('#circ2');
  about.on('click', function(){
    main.toggleClass('active');
    
  });
});


$(function() {
  var main = $('#main');
  var cdslk = $('#peek');
  cdslk.on('click', function(){
    main.toggleClass('active');
    
  });
});

$(function() {
  var main = $('#main');
  var cdslk = $('#lakk');
  cdslk.on('click', function(){
    main.toggleClass('active');
    
  });
});

$(function() {
  var main = $('#main');
  var cdslk = $('#zill');
  cdslk.on('click', function(){
    main.toggleClass('active');
    
  });
});



$(function() {
  var one = $('#main');
  var two = $('#circ3');
  two.on('click', function(){
    one.toggleClass('active');
  
  });
});

$(function() {
  var one = $('#main');
  var two = $('#circ4');
  two.on('click', function(){
    one.toggleClass('active');
  
  });
});


