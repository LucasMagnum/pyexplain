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

function explainTour(){
  var trip = new Trip([
    {
      sel: $('pre.prettyprint'),
      content: 'Aqui é onde seu código Python, \
              é analisado. Basta passar o mouse sobre \
              alguma palavra para visualizar as informações sobre ela.',
      position: 's',
      expose: true,
    },
    {
      sel: $('#analyzer dl'),
      content: 'Aqui estão algumas informações sobre seu código',
      position: 's',
      expose: true,
    },
    {
      sel: $('#analyzer dl dt:first'),
      content: 'O total de palavras que foram encontradas no seu código',
      position: 's',
      expose: true,
    },
    {
      sel: $('#analyzer dl dt:nth(1)'),
      content: 'Quantas palavras do seu código estão mapeadas no sistema',
      position: 's',
      expose: true,
    },
    {
      sel: $('#analyzer dl dt:gt(1)'),
      content: 'Aqui está a distribuição de palavras mapeadas em suas categorias.',
      position: 'n',
      expose: true,
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
  '/explain/': explainTour,
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