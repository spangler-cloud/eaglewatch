from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-captured_Date')
    template_name = 'photos.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'photo_full.html'