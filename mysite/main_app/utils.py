menu = [{'title': "О нас"},
        {'title': "Обратная связь"},
        ]


class DataMixin:
    # filters for anime
    filters = ['type', 'rate', 'category', 'studios']

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context