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
    context = {
        'posts': posts,
    }
    return render(request, 'blog/posts_list.html', context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
    }
    post.increase_views_count()
    return render(request, 'blog/post_detail.html', context)


def category_list(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'blog/categories_list.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published=True)

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category_detail.html', context)
