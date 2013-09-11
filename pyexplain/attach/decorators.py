# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied


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
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        obj = self.get_object()
        if obj.added_by == self.request.user or request.user.is_superuser:
            return super(RestrictUpdateMixin, self).dispatch(*args, **kwargs)
        raise PermissionDenied

