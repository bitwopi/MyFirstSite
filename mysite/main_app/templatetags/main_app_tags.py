import os

from django import template
from django.core.paginator import Paginator

from main_app.models import *


register = template.Library()


@register.simple_tag(takes_context=True)
def get_all_posts(context):
    request = context['request']
    posts_per_page = os.environ.get('POSTS_NUMBER_IN_PAGE', 10)

    all_posts = Anime.objects.all()

    paginator = Paginator(all_posts, posts_per_page)
    current_page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(current_page_number)

    return page_obj