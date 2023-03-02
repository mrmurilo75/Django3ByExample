from django.core import paginator
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    posts = Post.published.all()

    pagination = paginator.Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = pagination.page(page)
    except paginator.PageNotAnInteger:
        posts = pagination.page(1)
    except paginator.EmptyPage:
        posts = pagination.page(pagination.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             )
    return render(request, 'blog/post/detail.html', {'post': post})