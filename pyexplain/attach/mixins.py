# coding: utf-8
import json

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


class LoginRequiredMixin(object):
    """
        Só permite acesso a views para usuários logados
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class RestrictUpdateMixin(object):
    """
        Só permite editar a view se for quem criou o objeto
        ou um superuser.
    """
    can_delete_obj = True

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if obj.added_by == self.request.user or self.request.user.is_superuser:
            return super(RestrictUpdateMixin, self).dispatch(*args, **kwargs)
        raise PermissionDenied

    def get_context_data(self, *args, **kwargs):
        context = super(RestrictUpdateMixin, self).get_context_data(*args, **kwargs)
        context['can_delete_obj'] = self.can_delete_obj
        return context


class ContentTypeMixin(LoginRequiredMixin):
    _action = 'criado'  # action que irá compor mensagem

    @property
    def valid_message(self):
        verbose = self.model._meta.verbose_name.title
        return '%s %s com sucesso.' % (verbose, self._action)

    def get_content_object(self):
        obj_id = self.kwargs.pop('obj_id')
        content = ContentType.objects.get(**self.kwargs)
        return content.get_object_for_this_type(pk=obj_id)


class ModalContentTypeMixin(ContentTypeMixin):
    """
        Responsável pelo tratamento das views de criar, editar e remover
        ContentType utilizando modal forms.
    """
    template_name = 'attach/modal_form.html'

    _target = None  # HTML selector que será atualizada após a execução
    _delete_obj = False  # Flag para determinar se irá apagar ou não o obj

    @property
    def target(self):
        """ Selector que será atualizado ao finalizar execução """
        if self._target is None:
            raise NotImplementedError(u'É necessário informar o target.')
        return self._target

    def get_context_data(self, *args, **kwargs):
        """ Adiciona o model no context """
        context = super(ModalContentTypeMixin, self).get_context_data(*args, **kwargs)
        context['model'] = self.model
        return context

    def form_valid(self, form):
        """
            Ao criar algum item, já relacionar seu content type baseado na url.
        """
        if form.instance.id:
            self._action = 'atualizado'
        else:
            form.instance.added_by = self.request.user
            form.instance.content_object = self.get_content_object()

        form.instance.save()

        if self._delete_obj:
            self._action = 'removido'
            form.instance.delete_by(self.request.user)

        return self.json_response()

    def json_response(self):
        """ Retornar json com resposta valida"""
        data = {
            'message': self.valid_message,
            'status': 200,
            'success': True,
            'target': self.target,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

    def post(self, request, *args, **kwargs):
        """ Verificar se o submit foi para deletar """
        self._delete_obj = '_delete' in request.POST
        return super(ModalContentTypeMixin, self).post(request, *args, **kwargs)
