$(function(){
  $('form').submit(function(event){
    var form = $(this);
    $(this).find('.input-required').each(function(){
      if ($(this).val() == ''){
        form.addClass('has-error');
        event.preventDefault();
      }
    });
  });

  $('.ui-autocomplete-input').bind('djselectableselect', function(event, ui) {
    if (ui.item.url != undefined){
      window.location.href = ui.item.url;
    }
  });

});