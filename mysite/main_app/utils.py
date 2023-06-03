menu = [{'title': "Аниме", 'url_name': "home"},
        {'title': "Манга", 'url_name': "catalog-manga"},
        ]


class DataMixin:
    # filters for anime
    filters = ['type', 'rate', 'category', 'studios']

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context