from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Post

# Create your views here.
class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.exclude(date_time_published__isnull=True)
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk = pk)
        return context
