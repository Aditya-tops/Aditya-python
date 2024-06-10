from django.http import HttpResponse
from .models import Post

def create_post(request):
    new_post = Post.objects.create(
        title='My First Post',
        content='This is the content of my first post.'
    )
    return HttpResponse(f'Post created with ID: {new_post.id}')
