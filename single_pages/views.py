from django.shortcuts import render

from blog.models import Post


# Create your views here.
def about_me(request):
    return render(
        request,
        "single_pages/about_me.html",
        {},
    )


def landing(request):
    posts = Post.objects.order_by("-pk")[:3]
    return render(
        request,
        "single_pages/landing.html",
        {
            "posts": posts,
        },
    )
