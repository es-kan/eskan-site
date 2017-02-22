from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.exclude(date_time_published__isnull=True)
        return context
