from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from blog_app.models import Post, Category


def index(request):
    return HttpResponse('<h1>Hello world</h1>')


def posts_list(request):
    posts = Post.objects.filter(published=True)

    content = '<h1>Опубликованные статьи</h1><br><br>'

    for post in posts:
        content += f'<a href="/posts/{post.slug}/">{post.title}</a> ({post.created_at})<br>'

    return HttpResponse(content)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    content = f'''
    <h1>{post.title}</h1>
    <p>Автор: {post.autor}</p>
    <div>{post.content}</div>
    <hr>
    <a href="/posts/">Назад к статьям</a>
    '''

    return HttpResponse(content)


def category_list(request):
    categories = Category.objects.all()

    content = '<h1>Список всех категорий</h1><br><br>'

    for category in categories:
        content += f'<ul><a href="/categories/{category.id}/">{category.title}</a></ul>'

    return HttpResponse(content)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published=True)

    content = f'<h1>{category.title}</h1><br><br>'

    for post in posts:
        content += f'<a href="/posts/{post.slug}/">{post.title}</a> ({post.created_at})<br>'

    content += '<br><hr><br><a href="/categories/">Назад к категориям</a>'

    return HttpResponse(content)
