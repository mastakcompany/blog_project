from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from blog_app.models import Post, Category


def index(request):
    posts = Post.objects.filter(published=True)[:5]

    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def posts_list(request):
    posts = Post.objects.filter(published=True)
    content = '<h1>Опубликованные статьи</h1><br><br>'
    content += '<ul>'

    for post in posts:
        content += f'<li><a href="/posts/{post.slug}/">{post.title}</a> ({post.created_at})</li><br>'

    content += '</ul>'
    return HttpResponse(content)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def category_list(request):
    categories = Category.objects.all()

    content = '<h1>Список всех категорий</h1><br><br>'
    content += '<ul>'

    for category in categories:
        content += f'<li><a href="/categories/{category.id}/">{category.title}</a></li><br>'

    content += '</ul>'

    return HttpResponse(content)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published=True)

    content = f'<h1>{category.title}</h1><br><br>'
    content += '<ul>'

    for post in posts:
        content += f'<li><a href="/posts/{post.slug}/">{post.title}</a> ({post.created_at})</li><br>'

    content += '</ul>'
    content += '<br><hr><br><a href="/categories/">Назад к категориям</a>'

    return HttpResponse(content)
