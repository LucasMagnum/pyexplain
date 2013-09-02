var clean_keywords = {}; // keywords formatados
var category_count = {}; // quantidade de palavras por categoria

function show_analizer(){
  total_words = $('.kwd, .pln').length;
  mapped_words = $('.mapped_words');

  words_count = $('#analyzer #words-count');
  mapped_words_progressbar = $('#analyzer #mapped-words .progress-bar');

  // quantidade total de palavras
  words_count.text(total_words);

  // porcentagem de palavras mapeadas
  percent_mapped_words = (mapped_words.length / total_words) * 100;
  mapped_words_progressbar.css('width', percent_mapped_words + '%');

  // porcentagem por categoria
  for (var i in categorys){
    category_id = categorys[i].id;
    category_progressbar = $('#analyzer [data-id='+ category_id +'] .progress-bar');
    category_words = mapped_words.filter('[data-category_id='+ category_id +']');

    percent_category = (category_words.length / total_words) * 100;
    category_progressbar.css('width', percent_category + '%');
  }


}

function show_links(){
  /* mostrar links para palavras mapeadas */

  // organizar keywords para facilitar a busca
  for (key in keywords){
    codname = keywords[key].codname;
    clean_keywords[codname] = keywords[key];
  }

  $('.kwd, .pln').each(function(){
    keyword = $(this);
    original_text = $(this).text();
    text = original_text.trim();
    if (clean_keywords.hasOwnProperty(text)){
      url = clean_keywords[text].url;
      category_id = clean_keywords[text].category_id;

      keyword.html("<a data-toggle='popover' class='mapped_words' data-placement='bottom' data-title='"+ text +"' data-html=true href='" + url + "' data-category_id='"+ category_id +"' target='_blank'>" + original_text + "</a>");
    };
  });

  show_analizer();
}

$(function(){
  prettyPrint();
  show_links();

  // show popover and destroy popover
  $('a[data-toggle=popover]')
    .hover(function(){
      keyword = $(this).data('title');

      $(this)
        .attr('data-content', clean_keywords[keyword].description)
        .popover('show');
    })
    .mouseout(function(){
      $(this).popover('destroy');
  });

});