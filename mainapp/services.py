from django.conf import settings
from django.core.cache import cache

from mainapp.models import Category


def get_cached_categories():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        print(key)
        category_list = cache.get(key)
        print(category_list)
        if category_list is None:
            print(Category.objects.all())
            category_list = Category.objects.all()
            print(category_list)
            cache.set(key, category_list)
            return category_list
        return category_list