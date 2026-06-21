from django.shortcuts import get_object_or_404, render, redirect

from blog_app.models import Post, Category

from blog_app.forms import PostForm, SearchForm, CategoryForm

from slugify import slugify


def index(request):
    search_form = SearchForm(request.GET)
    posts = Post.objects.filter(published=True)

    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(title__icontains=query)

    posts = posts[:5]

    context = {
        'posts'      : posts,
        'search_form': search_form
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
        'posts'   : posts,
    }
    return render(request, 'blog/category_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('blog:index_page')
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', context={'form': form})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(category.title)
            category.save()
            return redirect('blog:category_list')
    else:
        form = CategoryForm()

    return render(request, 'blog/category_create.html', context={'form': form})
