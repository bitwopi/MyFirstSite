from django.shortcuts import render
from django.views.generic import TemplateView
from main_app.utils import DataMixin


class ProfileView(DataMixin, TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        c_def = super(ProfileView, self).get_user_context(title=self.request.user.username)
        return dict(list(context.items()) + list(c_def.items()))

