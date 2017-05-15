from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.exclude(date_time_published__isnull=True).order_by('-date_time_published')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context


class NewPostFormView(CreateView):
    template_name = 'post_edit.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_time_published = timezone.localtime(timezone.now())
        return super(NewPostFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']

    def get_object(self):
        post = Post.objects.get(pk=self.kwargs['pk'])
        return post

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class TestView(TemplateView):
    template_name = 'testview.html'
