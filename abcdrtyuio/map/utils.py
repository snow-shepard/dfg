from .models import *


class DataMixin:
    def get_user_context(self, **keargs):
        context = keargs
        cats = Category.objects.all()
        context['cats'] = cats
        if 'cat_slected' not in context:
            context['cat_selected'] = 0
        return context
        