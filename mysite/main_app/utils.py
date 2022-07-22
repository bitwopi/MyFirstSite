menu = [{'title': "About"},
        {'title': "Feedback"},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context