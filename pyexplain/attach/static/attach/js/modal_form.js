var keyword_modal = $('<div class="modal" role="dialog"></div>');
$(function(){

  $(document).on('click', '.open-modal', function(event){
    var url = $(this).attr('href');
    event.preventDefault();

    keyword_modal.load(url, function(){
      $(this).modal('show');
    });

  });

  $(document).on('click', '[name=_delete]', function(event){
    /* Ao clicar em deletar adicionar hidden field '_delete' */
    form = $(this).parents('form');
    delete_field = $('<input type="hidden" name="_delete" value="">');
    form.append(delete_field);
  });

  $(document).on('submit', '.modal-form', function(event){
    /* Ao submitar um modal form */
    $.ajax({
      type: $(this).attr('method'),
      url: this.action,
      data: $(this).serialize(),
      context: this,
      success: function(data, status, xhr) {
        if (!data['success']){
          keyword_modal.html(data);
        } else {
          target = data['target'];
          $(target).load(window.location.href + ' ' + target);
          keyword_modal.modal('hide');
        }
      },
      error: function(){
        alert('Não foi possível enviar sua solicitação. Tente novamente mais tarde.');
        keyword_modal.modal('hide');
      }
    });
    event.preventDefault();
  });

});