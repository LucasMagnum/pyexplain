var mapped_words = 0;


function show_analizer(){
  total_words = $('.kwd, .pln').length;

  words_count = $('#analyzer #words-count');
  mapped_words_progressbar = $('#analyzer #mapped-words .progress-bar');

  // quantidade de palavras
  words_count.text(total_words);

  // porcentagem de palavras mapeadas
  percent_mapped_words = (mapped_words / total_words) * 100;
  mapped_words_progressbar.css('width', percent_mapped_words + '%');
}

function show_links(){
  // mostrar links para palavras mapeadas
  $('.kwd, .pln').each(function(){
    keyword = $(this);
    original_text = $(this).text();
    text = original_text.trim();
    if (keywords.hasOwnProperty(text)){
      url = keywords[text].url;
      desc = keywords[text].desc;
      keyword.html("<a data-toggle='popover' data-placement='bottom' data-title='"+ text +"' data-content='"+ desc +"' data-html=true href='" + url + "' target='_blank'>" + original_text + "</a>");
      mapped_words++;
    };
  });

  show_analizer();
}

$(function(){
  prettyPrint();
  show_links();

  $('a[data-toggle=popover]').hover(function(){
    $(this).popover('show');
  });

  $('a[data-toggle=popover]').mouseout(function(){
    $(this).popover('destroy');
  });

});