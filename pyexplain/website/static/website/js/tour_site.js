DELAY = 3000;

function homeTour(){
  var trip = new Trip([
    {
      sel: $('textarea'),
      content: 'Cole seu código Python aqui',
      position: 's',
      expose: true,
      func: function(obj){
        setTimeout(function(){
          obj.text('from datetime import datetime');
        }, DELAY);
      }
    },
    {
      sel: $('[type=submit]'),
      content: 'Aperte esse botão para inicializar a análise',
      position: 's',
      func: function(obj){
        setTimeout(function(){
          obj.trigger('click')
        }, DELAY);
      }
    },
  ], {
      delay : DELAY,
      onTripChange : function(i, tripData) {
        if (tripData.hasOwnProperty('func')){
          func = tripData['func'];
          obj = tripData['sel'];
          func(obj);
        }
      }
  });

  trip.start();
}

tours = {
  '/': homeTour,
}


function showTour(path){
  if (tours.hasOwnProperty(path)){
    func = tours[path];
    func();
  }
}


$(function(){
  $(document).on('click', '.show_tour', function(){
    path = window.location.pathname;
    showTour(path);
  });
});