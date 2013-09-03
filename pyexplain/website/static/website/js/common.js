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
});